from enum import Enum

from models.pkmn.stats.StatsDict import StatsDict


# Bonus/Malus percentage from natures
nature_base_modifier = 100
nature_bonus = 10
nature_bonus_modifier = nature_base_modifier + nature_bonus
nature_malus = 10
nature_malus_modifier = nature_base_modifier - nature_malus


class _PokemonNatureImplm:

    def __init__(self, hp: int = nature_base_modifier,
                 atk: int = nature_base_modifier, phys_def: int = nature_base_modifier,
                 spe_atk: int = nature_base_modifier, spe_def: int = nature_base_modifier,
                 spd: int = nature_base_modifier):
        super().__init__()
        self.__stats_table = StatsDict(hp=hp, atk=atk, phys_def=phys_def, spe_atk=spe_atk, spe_def=spe_def, spd=spd)

    def apply_modifier(self, stats: StatsDict):
        for stat_key in self.__stats_table.__dict__.keys():
            stats[stat_key] *= self.__stats_table[stat_key] / 100


class PokemonNature(Enum):
    Lonely = _PokemonNatureImplm(atk=nature_bonus_modifier, phys_def=nature_malus_modifier)
    Adamant = _PokemonNatureImplm(atk=nature_bonus_modifier, spe_atk=nature_malus_modifier)
    Naughty = _PokemonNatureImplm(atk=nature_bonus_modifier, spe_def=nature_malus_modifier)
    Brave = _PokemonNatureImplm(atk=nature_bonus_modifier, spd=nature_malus_modifier)

    Bold = _PokemonNatureImplm(phys_def=nature_bonus_modifier, atk=nature_malus_modifier)
    Impish = _PokemonNatureImplm(phys_def=nature_bonus_modifier, spe_atk=nature_malus_modifier)
    Lax = _PokemonNatureImplm(phys_def=nature_bonus_modifier, spe_def=nature_malus_modifier)
    Relaxed = _PokemonNatureImplm(phys_def=nature_bonus_modifier, spd=nature_malus_modifier)

    Modest = _PokemonNatureImplm(spe_atk=nature_bonus_modifier, atk=nature_malus_modifier)
    Mild = _PokemonNatureImplm(spe_atk=nature_bonus_modifier, phys_def=nature_malus_modifier)
    Rash = _PokemonNatureImplm(spe_atk=nature_bonus_modifier, spe_def=nature_malus_modifier)
    Quiet = _PokemonNatureImplm(spe_atk=nature_bonus_modifier, spd=nature_malus_modifier)

    Calm = _PokemonNatureImplm(spe_def=nature_bonus_modifier, atk=nature_malus_modifier)
    Gentle = _PokemonNatureImplm(spe_def=nature_bonus_modifier, phys_def=nature_malus_modifier)
    Careful = _PokemonNatureImplm(spe_def=nature_bonus_modifier, spe_atk=nature_malus_modifier)
    Sassy = _PokemonNatureImplm(spe_def=nature_bonus_modifier, spd=nature_malus_modifier)

    Timid = _PokemonNatureImplm(spd=nature_bonus_modifier, atk=nature_malus_modifier)
    Hasty = _PokemonNatureImplm(spd=nature_bonus_modifier, phys_def=nature_malus_modifier)
    Jolly = _PokemonNatureImplm(spd=nature_bonus_modifier, spe_atk=nature_malus_modifier)
    Naive = _PokemonNatureImplm(spd=nature_bonus_modifier, spe_def=nature_malus_modifier)

    Quirky = _PokemonNatureImplm()
    Docile = _PokemonNatureImplm()
    Hardy = _PokemonNatureImplm()
    Bashful = _PokemonNatureImplm()
    Serious = _PokemonNatureImplm()

    def apply_modifier(self, stats: StatsDict):
        self.value.apply_modifier(stats)
