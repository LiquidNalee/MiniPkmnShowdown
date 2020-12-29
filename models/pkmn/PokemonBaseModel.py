from models.pkmn.stats.StatsDict import StatsDict
from models.pkmn.types.PokemonType import PokemonType, format_types_tuple, type_equals


class PokemonBaseModel:

    def __init__(self, name: str, types: (PokemonType, PokemonType), base_stats: StatsDict):
        self.name = name
        self.type = format_types_tuple(types)
        self.base_stats = base_stats

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplementedError
        return self.name == other.name and type_equals(self.type, other.type) \
            and self.base_stats == other.base_stats
