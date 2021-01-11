from typing import List

from models.pkmn.PokemonModel import PokemonModel
from models.pkmn.moves.PokemonMove import PokemonMove


def repeatOnError(*exceptions):
    def checking(function):
        def checked(*args, **kwargs):
            while True:
                try:
                    result = function(*args, **kwargs)
                except exceptions as ex:
                    print("Invalid Input!")
                else:
                    return result

        return checked

    return checking


@repeatOnError(NotImplementedError)
def getDecisionType():
    i = input("Enter 'm' to use a move or 's' to switch out: ")
    if i != "m" and i != "s":
        raise NotImplementedError()
    return i


@repeatOnError(ValueError)
def getNumberInput(max_range: int):
    i = input(f'Enter your selection (0 - {max_range - 1}): ')
    val = int(i)
    if val < 0 or val >= max_range:
        raise ValueError
    return val


@repeatOnError(ValueError)
def getCancelableNumberInput(max_range: int):
    i = input(f'Enter your selection (0 - {max_range - 1}) or Cancel (C): ')
    if i == "C":
        return -1
    val = int(i)
    if val < 0 or val >= max_range:
        raise ValueError
    return val


def pkmnSelection(team: List[PokemonModel]) -> int:
    print("\nChoose a Pkmn.")
    while True:
        i = getNumberInput(len([_ for _ in team if _ is not None]))
        if team[i].isKO():
            print(f"{team[i].name} is K.O ! It cannot fight anymore...")
        else:
            break
    return i


def turnDecision(active_pkmn: PokemonModel, team: List[PokemonModel]) -> (PokemonMove, int):
    while True:
        t = getDecisionType()
        max_range = len([_ for _ in active_pkmn.moves if _ is not None]) if t == "m" \
            else len([_ for _ in team if _ is not None])
        i = getCancelableNumberInput(max_range=max_range)
        if i != -1:
            break
    return (active_pkmn.moves[i], None) if t == "m" else (None, i)
