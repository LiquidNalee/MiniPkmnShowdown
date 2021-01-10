from re import sub, M
from models.game.battle.BattleGameState import BattleGameState
from models.pkmn.PokemonModel import PokemonModel
from models.pkmn.moves.PokemonMove import PokemonMove

__separation_line = '-'.join('' for _ in range(150))


def __shiftDisplayBox(box: str, shift: int):
    return sub("^", "\t".join("" for _ in range(shift)), box, flags=M)


def displayPlayers(battleGameState: BattleGameState):
    print(__shiftDisplayBox(str(battleGameState.opponent), 20))
    print(str(battleGameState.player))


def displayBattleGameState(battleGameState: BattleGameState):
    displayPlayers(battleGameState)
    print(f"Turn: {battleGameState.turn}\n")
    print(__shiftDisplayBox(str(battleGameState.getOpponentActivePkmn()), 20))
    print(str(battleGameState.getPlayerActivePkmn()))
    print(f"{__separation_line}")
    print(battleGameState.getPlayerActivePkmn().moveListAsStr())
    print(f"{__separation_line}")


def displayUsedMove(caster: PokemonModel, caster_move: PokemonMove, trgt: PokemonModel,
                    type_effectiveness: float, damage: int):
    print(f"{caster.name} uses {caster_move.name}")
    if type_effectiveness != 1:
        print("It's super effective!" if type_effectiveness > 1
              else f"It doesn't affect {trgt.name}" if type_effectiveness == 0
              else "It's not very effective...")
    if damage != 0:
        print(f"{trgt.name} loses {damage} HP")
    if trgt.isKO():
        print(f"{trgt.name} is K.O !")
    input()


def displaySwitch(player_name: str, out: PokemonModel, coming_in: PokemonModel):
    print(f"{out.name} goes back into its PokeBall.")
    print(f"{player_name} sends {coming_in.name} out !")
    input()


def displayEndOfBattle(win: bool, battleGameState: BattleGameState):
    print("# Finished #")
    displayPlayers(battleGameState)
    print(f"Winner: {battleGameState.player.name if win else battleGameState.opponent.name}")
    print(f"{'-'.join(__separation_line)}")
    input()
