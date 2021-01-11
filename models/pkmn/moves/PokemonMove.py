from enum import Enum
from os.path import join
from json import load

from models.pkmn.types.PokemonType import PokemonType
from models.pkmn.stats.StatsDict import StatsDict

from database.DatabaseConfig import database_dir


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

    @staticmethod
    def fromDb(name: str):
        with open(join(str(database_dir), "moves", f"{name}.json")) as move_data_file:
            move_data = load(move_data_file)
            return PokemonMove(
                name=name,
                move_type=PokemonType[move_data["type"]],
                category=MoveCategory[move_data["category"]],
                pp=int(move_data["pp"]),
                power=int(move_data["power"]) if "power" in move_data else 0,
                accuracy=int(move_data["accuracy"]) if "accuracy" in move_data else 100,
                priority=int(move_data["priority"]) if "priority" in move_data else 0,
                stat_mod_rate=int(move_data["stat_mod_rate"]) if "stat_mod_rate" in move_data else 0,
                self_stat_mod=StatsDict(move_data["self_stat_mod"]) if "self_stat_mod" in move_data else StatsDict(),
                trgt_stat_mod=StatsDict(move_data["trgt_stat_mod"]) if "trgt_stat_mod" in move_data else StatsDict()
            )
