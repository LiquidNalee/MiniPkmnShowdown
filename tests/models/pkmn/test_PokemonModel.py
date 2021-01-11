from unittest import TestCase
from models.pkmn.PokemonModel import PokemonModel
from models.pkmn.moves.PokemonMove import PokemonMove, MoveCategory
from models.pkmn.types.PokemonType import PokemonType, type_equals
from models.pkmn.natures.PokemonNature import PokemonNature
from models.pkmn.stats.StatsDict import StatsDict


class TestPokemonModel(TestCase):

    def test_pokemon_model(self):
        scizor = PokemonModel(
            name="Scizor",
            types=(PokemonType.Bug, PokemonType.Steel),
            level=100,
            nature=PokemonNature.Adamant,
            moves=[
                PokemonMove(
                    name="Bullet Punch",
                    move_type=PokemonType.Steel,
                    category=MoveCategory.Physical,
                    pp=48,
                    power=40,
                    priority=1
                ),
                PokemonMove(
                    name="U-Turn",
                    move_type=PokemonType.Bug,
                    category=MoveCategory.Physical,
                    pp=32,
                    power=70
                ),
                PokemonMove(
                    name="Steel Beam",
                    move_type=PokemonType.Steel,
                    category=MoveCategory.Special,
                    pp=8,
                    power=140,
                    accuracy=95
                ),
                PokemonMove(
                    name="Swords Dance",
                    move_type=PokemonType.Normal,
                    category=MoveCategory.Status,
                    pp=32,
                    effect_rate=100,
                    self_stat_mod=StatsDict(atk=2)
                )
            ],
            base_stats=StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=65),
            evs=StatsDict(hp=120, atk=252, phys_def=0, spe_atk=0, spe_def=0, spd=136),
            ivs=StatsDict(hp=31, atk=31, phys_def=31, spe_atk=31, spe_def=31, spd=31)
        )

        assert scizor.name == "Scizor"
        assert type_equals(scizor.type, (PokemonType.Steel, PokemonType.Bug))
        assert scizor.level == 100
        assert scizor._nature == PokemonNature.Adamant
        assert not scizor._nature == PokemonNature.Jolly
        assert scizor.base_stats == StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=65)
        assert scizor.base_stats.atk == 130
        assert scizor._evs == StatsDict(hp=120, atk=252, phys_def=0, spe_atk=0, spe_def=0, spd=136)
        assert scizor._ivs == StatsDict(hp=31, atk=31, phys_def=31, spe_atk=31, spe_def=31, spd=31)

        expected_stat_values = StatsDict(hp=311, atk=394, phys_def=236, spe_atk=131, spe_def=196, spd=200)
        assert scizor.stats == expected_stat_values
