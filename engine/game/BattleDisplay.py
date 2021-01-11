from re import sub, M
from models.game.battle.BattleGameState import BattleGameState
from models.pkmn.PokemonModel import PokemonModel
from models.pkmn.moves.PokemonMove import PokemonMove

__separation_line = '-'.join('' for _ in range(150))


def __shiftDisplayBox(box: str, shift: int):
    return sub("^", "\t".join("" for _ in range(shift)), box, flags=M)


def __displaySideBySide(box_1: str, box_2: str):
    split_lines = (box_1.splitlines(), box_2.splitlines())
    print("\n".join([f"{split_lines[0][_]:<50}{split_lines[1][_]:>50}" for _ in range(len(split_lines[0]))]))


def displayPlayers(battleGameState: BattleGameState):
    __displaySideBySide(str(battleGameState.player), str(battleGameState.opponent))


def displayBattleGameState(battleGameState: BattleGameState):
    displayPlayers(battleGameState)
    print(f"Turn: {battleGameState.turn}\n")
    __displaySideBySide(str(battleGameState.getPlayerActivePkmn()), str(battleGameState.getOpponentActivePkmn()))
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
