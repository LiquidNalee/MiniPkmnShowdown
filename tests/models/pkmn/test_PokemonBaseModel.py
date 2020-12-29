from unittest import TestCase
from models.pkmn.PokemonBaseModel import PokemonBaseModel
from models.pkmn.types.PokemonType import PokemonType, type_equals
from models.pkmn.stats.StatsDict import StatsDict


class TestPokemonBaseModel(TestCase):

    def test_double_type_pokemon(self):
        scizor = PokemonBaseModel(
            name="Scizor",
            types=(PokemonType.Bug, PokemonType.Steel),
            base_stats=StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=65)
        )

        assert scizor.name == "Scizor"
        assert type_equals(scizor.type, (PokemonType.Bug, PokemonType.Steel))
        assert scizor.base_stats == StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=65)
        assert scizor.base_stats.atk == 130

    def test_double_type_pokemon_valid_comparison(self):
        scizor = PokemonBaseModel(
            name="Scizor",
            types=(PokemonType.Bug, PokemonType.Steel),
            base_stats=StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=65)
        )

        definitely_not_scizor = PokemonBaseModel(
            name="Scizor",
            types=(PokemonType.Steel, PokemonType.Bug),
            base_stats=StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=65)
        )

        assert scizor.name == definitely_not_scizor.name
        assert type_equals(scizor.type, definitely_not_scizor.type)
        assert scizor.base_stats == definitely_not_scizor.base_stats
        assert scizor.base_stats.atk == definitely_not_scizor.base_stats.atk
        assert scizor == definitely_not_scizor

    def test_double_type_pokemon_invalid_comparison(self):
        scizor = PokemonBaseModel(
            name="Scizor",
            types=(PokemonType.Bug, PokemonType.Steel),
            base_stats=StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=65)
        )

        crawdaunt = PokemonBaseModel(
            name="Crawdaunt",
            types=(PokemonType.Water, PokemonType.Dark),
            base_stats=StatsDict(hp=63, atk=130, phys_def=85, spe_atk=90, spe_def=55, spd=55)
        )

        assert scizor.name != crawdaunt.name
        assert not type_equals(scizor.type, crawdaunt.type)
        assert scizor.base_stats != crawdaunt.base_stats
        assert scizor.base_stats.atk == crawdaunt.base_stats.atk
        assert scizor != crawdaunt

    def test_simple_type_pokemon(self):
        blissey = PokemonBaseModel(
            name="Blissey",
            types=(PokemonType.Normal, None),
            base_stats=StatsDict(hp=255, atk=10, phys_def=10, spe_atk=75, spe_def=135, spd=55)
        )

        assert blissey.name == "Blissey"
        assert type_equals(blissey.type, (PokemonType.Normal, None))
        assert blissey.base_stats == StatsDict(hp=255, atk=10, phys_def=10, spe_atk=75, spe_def=135, spd=55)
        assert blissey.base_stats.hp == 255

    def test_simple_type_pokemon_valid_comparison(self):
        blissey = PokemonBaseModel(
            name="Blissey",
            types=(PokemonType.Normal, None),
            base_stats=StatsDict(hp=255, atk=10, phys_def=10, spe_atk=75, spe_def=135, spd=55)
        )

        definitely_not_blissey = PokemonBaseModel(
            name="Blissey",
            types=(None, PokemonType.Normal),
            base_stats=StatsDict(hp=255, atk=10, phys_def=10, spe_atk=75, spe_def=135, spd=55)
        )

        assert blissey.name == definitely_not_blissey.name
        assert type_equals(blissey.type, definitely_not_blissey.type)
        assert blissey.base_stats == definitely_not_blissey.base_stats
        assert blissey.base_stats.atk == definitely_not_blissey.base_stats.atk
        assert blissey == definitely_not_blissey

    def test_simple_type_pokemon_invalid_comparison(self):
        blissey = PokemonBaseModel(
            name="Blissey",
            types=(PokemonType.Normal, None),
            base_stats=StatsDict(hp=255, atk=10, phys_def=10, spe_atk=75, spe_def=135, spd=55)
        )

        barraskewda = PokemonBaseModel(
            name="Barraskewda",
            types=(PokemonType.Water, None),
            base_stats=StatsDict(hp=61, atk=123, phys_def=60, spe_atk=60, spe_def=50, spd=136)
        )

        assert blissey.name != barraskewda.name
        assert not type_equals(blissey.type, barraskewda.type)
        assert blissey.base_stats != barraskewda.base_stats
        assert blissey.base_stats.atk != barraskewda.base_stats.atk
        assert blissey != barraskewda
