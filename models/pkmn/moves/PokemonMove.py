from enum import Enum

from models.pkmn.types.PokemonType import PokemonType
from models.pkmn.stats.StatsDict import StatsDict


class MoveCategory(Enum):
    Physical = 0
    Special = 1
    Support = 2


class PokemonMove:

    def __init__(self, name: str, move_type: PokemonType, category: MoveCategory, pp: int,
                 power: int = 0, accuracy: int = 100, priority: int = 0, stat_mod_rate: int = 0,
                 self_stat_mod: StatsDict = None, trgt_stat_mod: StatsDict = None):
        self.name = name
        self.type = move_type
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        self.priority = priority
        self.stat_mod_rate = stat_mod_rate
        self.self_stat_mod = self_stat_mod if self_stat_mod is not None else StatsDict()
        self.trgt_stat_mod = trgt_stat_mod if trgt_stat_mod is not None else StatsDict()
