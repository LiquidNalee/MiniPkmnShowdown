from enum import Enum

from models.pkmn.types.PokemonType import PokemonType
from models.pkmn.stats.StatsDict import StatsDict


class MoveCategory(Enum):
    Physical = "[Ph]"
    Special = "[Sp]"
    Support = "[Su]"


class PokemonMove:

    def __init__(self, name: str, move_type: PokemonType, category: MoveCategory, pp: int,
                 power: int = 0, accuracy: int = 100, priority: int = 0, stat_mod_rate: int = 0,
                 self_stat_mod: StatsDict = None, trgt_stat_mod: StatsDict = None):
        self.name = name
        self.type = move_type
        self.category = category
        self.pp = pp
        self.max_pp = pp
        self.power = power
        self.accuracy = accuracy
        self.priority = priority
        self.stat_mod_rate = stat_mod_rate
        self.self_stat_mod = self_stat_mod if self_stat_mod is not None else StatsDict()
        self.trgt_stat_mod = trgt_stat_mod if trgt_stat_mod is not None else StatsDict()

    def __str__(self):
        prio_str = f"prio:{'+' if self.priority > 0 else ''}{self.priority}"
        return f"{str(self.type):^15}  {self.category.value}{self.pp:>9}/{self.max_pp:<3}\n" \
               f"{self.name:^34}\n" \
               f" {str(self.power):>3}BP -{str(self.accuracy) + '% acc.':^15}- {prio_str:>8} \n" \
               f"{'-':^34}" if self.stat_mod_rate == 0 else \
               f"{self.stat_mod_rate:<3}%: " if self.stat_mod_rate != 100 else "" \
               + f"{', '.join([key + ' x' + val for key, val in self.self_stat_mod if val != 0]):^20} [Self]" \
               if self.self_stat_mod != StatsDict() else \
               f"{', '.join([key + ' x' + val for key, val in self.trgt_stat_mod if val != 0]):^18} [Target]" \
               if self.trgt_stat_mod != StatsDict() else \
               ""

    def asJson(self):
        return {
            "name": self.name,
            "type": str(self.type),
            "category": self.category.value,
            "pp": self.pp,
            "max_pp": self.max_pp,
            "power": self.power,
            "accuracy": self.accuracy,
            "priority": f"{'+' if self.priority > 0 else ''}{self.priority}",
            "stat_mod": "" if self.stat_mod_rate == 0 else
                        f"{self.stat_mod_rate}%: " if self.stat_mod_rate != 100 else ""
                        + f"{', '.join([key + ' x' + val for key, val in self.self_stat_mod if val != 0])} [Self]"
                        if self.self_stat_mod != StatsDict() else
                        f"{', '.join([key + ' x' + val for key, val in self.trgt_stat_mod if val != 0])} [Target]"
                        if self.trgt_stat_mod != StatsDict() else
                        ""
        }
