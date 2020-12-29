from enum import Enum


class PokemonType(Enum):
    Normal = 1
    Fighting = 2
    Flying = 3
    Poison = 4
    Ground = 5
    Rock = 6
    Bug = 7
    Ghost = 8
    Psychic = 9
    Grass = 10
    Fire = 11
    Water = 12
    Electric = 13
    Ice = 14
    Dragon = 15
    Steel = 16
    Dark = 17
    Fairy = 18

    def __lt__(self, other):
        if self.__class__ != other.__class__:
            return NotImplementedError
        return self.value < other.value


def format_types_tuple(types: (PokemonType, PokemonType)):
    if types[0] is None:
        if types[1] is None:
            raise Exception("PokemonBaseModel - init: Unhandled type (None; None)")
        else:
            return types[1], None
    else:
        if types[0] == types[1]:
            raise Exception(f"PokemonBaseModel - init: Unhandled type ({str(types[0])}; {str(types[1])})")
        return types if types[1] is None or types[0] < types[1] else (types[1], types[0])


def type_equals(self, other: (PokemonType, PokemonType)):
    return format_types_tuple(self) == format_types_tuple(other)
