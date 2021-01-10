from typing import List

from models.pkmn.PokemonBaseModel import PokemonBaseModel
from models.pkmn.stats.StatsDict import StatsDict
from models.pkmn.types.PokemonType import PokemonType
from models.pkmn.natures.PokemonNature import PokemonNature
from models.pkmn.moves.PokemonMove import PokemonMove


class PokemonModel(PokemonBaseModel):

    __bar_len = 25

    def __init__(self, name: str, types: (PokemonType, PokemonType), level: int, nature: PokemonNature,
                 moves: List[PokemonMove], base_stats: StatsDict, evs: StatsDict, ivs: StatsDict):
        super().__init__(name=name, types=types, base_stats=base_stats)
        self.level = level
        self._nature = nature
        self.moves = moves
        self._evs = evs
        self._ivs = ivs
        self.stats = self.__stats_compute()
        self.max_hp = self.stats.hp

    def __str__(self):
        hp_percentage = self.stats.hp / self.max_hp
        ticks = int(hp_percentage * self.__bar_len + .5)
        return f"{self.name} (lvl.{self.level}):" \
               f"{'█'.join('' for _ in range(ticks))}{'▁'.join('' for _ in range(self.__bar_len - ticks))}" \
               f" {self.stats.hp}/{self.max_hp} ({int(hp_percentage * 100)}%)"

    def moveListAsStr(self) -> str:
        split_lines = [str(move).splitlines() for move in self.moves]
        return "\n".join(["| |".join([split_lines[x][y] for x in range(len(split_lines))])
                         for y in range(len(split_lines[0]))])

    def takeDamage(self, damage: int):
        self.stats.hp -= min(damage, self.stats.hp)

    def isKO(self):
        return self.stats.hp == 0

    @staticmethod
    def __compute_stat_baseline(level: int, base_stat: int, iv: int, ev: int) -> int:
        return int((2 * base_stat + iv + ev / 4) * level / 100)

    def __stats_compute(self) -> StatsDict:
        stat_values = StatsDict(**{
            stat_key:
                self.__compute_stat_baseline(level=self.level, base_stat=self.base_stats.hp,
                                             iv=self._ivs.hp, ev=self._evs.hp) + self.level + 10
                if stat_key == "hp" else
                self.__compute_stat_baseline(level=self.level, base_stat=self.base_stats[stat_key],
                                             iv=self._ivs[stat_key], ev=self._evs[stat_key]) + 5
            for stat_key in self.base_stats.__dict__.keys()
        })
        self._nature.apply_modifier(stat_values)
        return stat_values
