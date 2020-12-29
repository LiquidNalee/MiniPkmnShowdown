from typing import Callable

from models.pkmn.types.PokemonType import PokemonType


class PokemonBaseMove:

    def __init__(self, name: str, move_type: PokemonType, pp: int,
                 priority: int, effect: Callable):
        self.name = name
        self.type = move_type
        self.pp = pp
        self.priority = priority
        self.effect = effect
