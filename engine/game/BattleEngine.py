from random import randint

from engine.game import InputHandler
from engine.game.BattleDisplay import displayPlayers, displayBattleGameState, displayUsedMove, \
    displaySwitch, displayEndOfBattle
from engine.pkmn.types.TypesBaseRuleSet import TypesBaseRuleSet
from models.game.battle.BattleGameState import BattleGameState
from models.pkmn.PokemonModel import PokemonModel
from models.pkmn.moves.PokemonMove import PokemonMove, MoveCategory
from models.pkmn.stats.StatsDict import StatsDict


class BattleEngine:

    def __init__(self, battleGameState: BattleGameState, typesRuleSet: TypesBaseRuleSet):
        self.gameState = battleGameState
        self.typesRuleSet = typesRuleSet

    def startGame(self) -> bool:
        displayPlayers(self.gameState)
        # Lead Phase
        player_pkmn_selection = InputHandler.pkmnSelection(self.gameState.player.team)
        self.gameState.setPlayerActivePkmn(player_pkmn_selection)

        # Battle Phase
        self.__battlePhase()

        win = not self.gameState.player.hasLost()
        displayEndOfBattle(win, self.gameState)
        return win

    def __battlePhase(self):
        while not self.gameState.player.hasLost() and not self.gameState.opponent.hasLost():
            # Move Selection Phase
            if self.gameState.getPlayerActivePkmn().isKO():
                self.__switchPlayerPokemon()
            if self.gameState.getOpponentActivePkmn().isKO():
                self.__switchOpponentPokemon()

            displayBattleGameState(self.gameState)
            plyr_move, plyr_switch = InputHandler.turnDecision(self.gameState.getPlayerActivePkmn(),
                                                               self.gameState.player.team)
            rand = randint(0, len(self.gameState.getOpponentActivePkmn().moves) - 1)
            opponent_move = self.gameState.getOpponentActivePkmn().moves[rand]
            self.gameState.setTurnState(plyr_move=plyr_move, opponent_move=opponent_move)

            if plyr_switch:
                self.__switchPlayerPokemon(plyr_switch)

            first, second = self.__getMoveOrder()
            self.__useMove(first[0], first[1], second[0])
            if not second[0].isKO() and second[1] is not None:
                self.__useMove(second[0], second[1], first[0])
            self.gameState.turn += 1

    def __useMove(self, caster: PokemonModel, caster_move: PokemonMove, trgt: PokemonModel) \
            -> bool:
        damage = 0
        type_effectiveness = 1
        if caster_move.category != MoveCategory.Support:
            offensive_stat = caster.stats.atk if caster_move.category == MoveCategory.Physical \
                else caster.stats.spe_atk
            defensive_stat = trgt.stats.phys_def if caster_move.category == MoveCategory.Physical \
                else trgt.stats.spe_def
            damage = (((2 * caster.level / 5 + 2) * caster_move.power * offensive_stat / defensive_stat) / 50 + 2)
            type_effectiveness = self.typesRuleSet.getEffectiveness(caster_move.type, trgt.type)
            modifier = (1.5 if caster_move.type == caster.type else 1) \
                       * type_effectiveness \
                       * randint(85, 100) / 100 \
                       * (1 if randint(0, 100) <= caster_move.accuracy else 0)
            damage = int(damage * modifier)

        if damage != 0:
            trgt.takeDamage(damage)
        displayUsedMove(caster, caster_move, trgt, type_effectiveness, damage)

        if randint(0, 100) <= caster_move.stat_mod_rate:
            for stat_key in StatsDict.__dict__.keys():
                caster.stats[stat_key] *= caster_move.self_stat_mod[stat_key]
                trgt.stats[stat_key] *= caster_move.trgt_stat_mod[stat_key]

        return True

    def __switchPlayerPokemon(self, selection: int = None):
        out = self.gameState.getPlayerActivePkmn()
        coming_in = self.gameState.setPlayerActivePkmn(InputHandler.pkmnSelection(self.gameState.player.team)) \
            if selection is None else selection
        displaySwitch(player_name=self.gameState.player.name, out=out, coming_in=coming_in)

    def __switchOpponentPokemon(self):
        out = self.gameState.getOpponentActivePkmn()
        coming_in = self.gameState.sendNextOpponentActivePkmn()
        displaySwitch(player_name=self.gameState.opponent.name, out=out, coming_in=coming_in)

    def __getMoveOrder(self) -> ((PokemonModel, PokemonMove), (PokemonModel, PokemonMove)):
        move_order = self.gameState.getTurnState()
        (plyr_pkmn, plyr_move), (opponent_pkmn, opponent_move) = move_order
        if plyr_move is None:
            return move_order[1], move_order[0]

        if plyr_move.priority == opponent_move.priority:
            if plyr_pkmn.stats.spd == opponent_pkmn.stats.spd:
                if randint(0, 1) == 1:
                    move_order = move_order[1], move_order[0]
            else:
                if plyr_pkmn.stats.spd < opponent_pkmn.stats.spd:
                    move_order = move_order[1], move_order[0]
        else:
            if plyr_move.priority < opponent_move.priority:
                move_order = move_order[1], move_order[0]

        return move_order

    def __getActivePkmns(self):
        return self.gameState.getPlayerActivePkmn(), self.gameState.getOpponentActivePkmn()
