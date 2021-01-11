from models.game.trainer.PokemonTrainer import PokemonTrainer
from models.pkmn.PokemonModel import PokemonModel
from models.pkmn.moves.PokemonMove import PokemonMove


class BattleGameState:

    def __init__(self, player: PokemonTrainer, opponent: PokemonTrainer):
        self.turn = 1
        self.player = player.makeCopy()
        self.__player_active_pkmn_slot = 0
        self.player_move_selection = None
        self.opponent = opponent.makeCopy()
        self.opponent_move_selection = None
        self.__opponent_active_pkmn_slot = 0

    def getPlayerActivePkmn(self) -> PokemonModel:
        return self.player.team[self.__player_active_pkmn_slot]

    def setPlayerActivePkmn(self, index: int) -> PokemonModel:
        self.__player_active_pkmn_slot = index
        return self.player.team[self.__player_active_pkmn_slot]

    def getOpponentActivePkmn(self) -> PokemonModel:
        return self.opponent.team[self.__opponent_active_pkmn_slot]

    def setOpponentActivePkmn(self, index: int) -> PokemonModel:
        self.__opponent_active_pkmn_slot = index
        return self.opponent.team[self.__opponent_active_pkmn_slot]

    def sendNextOpponentActivePkmn(self) -> PokemonModel:
        self.__opponent_active_pkmn_slot += 1
        return self.opponent.team[self.__opponent_active_pkmn_slot]

    def getTurnState(self):
        return (self.getPlayerActivePkmn(), self.player_move_selection),\
               (self.getOpponentActivePkmn(), self.opponent_move_selection)

    def setTurnState(self, plyr_move: PokemonMove, opponent_move: PokemonMove):
        self.player_move_selection = plyr_move
        self.opponent_move_selection = opponent_move
