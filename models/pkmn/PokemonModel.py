from typing import List

from models.pkmn.PokemonBaseModel import PokemonBaseModel
from models.pkmn.stats.StatsDict import StatsDict
from models.pkmn.types.PokemonType import PokemonType
from models.pkmn.natures.PokemonNature import PokemonNature
from models.pkmn.moves.PokemonBaseMove import PokemonBaseMove


class PokemonModel(PokemonBaseModel):

    def __init__(self, name: str, types: (PokemonType, PokemonType), level: int, nature: PokemonNature,
                 moves: List[PokemonBaseMove], base_stats: StatsDict, evs: StatsDict, ivs: StatsDict):
        super().__init__(name=name, types=types, base_stats=base_stats)
        self.level = level
        self._nature = nature
        self.moves = moves
        self._evs = evs
        self._ivs = ivs
        self.stats = self.stats_compute()

    @staticmethod
    def __compute_stat_baseline(level: int, base_stat: int, iv: int, ev: int) -> int:
        return int((2 * base_stat + iv + ev / 4) * level / 100)

    def stats_compute(self) -> StatsDict:
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
