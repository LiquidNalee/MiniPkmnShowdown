from unittest import TestCase
from models.pkmn.PokemonBaseModel import PokemonBaseModel
from models.pkmn.utils.PokemonType import PokemonType
from models.pkmn.utils.StatsDict import StatsDict


class TestPokemonBaseModel(TestCase):

    def test_double_type_pokemon(self):
        scizor = PokemonBaseModel(
            name="Scizor",
            types=(PokemonType.Bug, PokemonType.Steel),
            base_stats_dict=StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=60)
        )

        assert scizor.name == "Scizor"
        assert scizor.type_equals((PokemonType.Bug, PokemonType.Steel))
        assert scizor.base_stats_dict == StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=60)
        assert scizor.base_stats_dict.atk == 130

    def test_double_type_pokemon_valid_comparison(self):
        scizor = PokemonBaseModel(
            name="Scizor",
            types=(PokemonType.Bug, PokemonType.Steel),
            base_stats_dict=StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=60)
        )

        definitely_not_scizor = PokemonBaseModel(
            name="Scizor",
            types=(PokemonType.Steel, PokemonType.Bug),
            base_stats_dict=StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=60)
        )

        assert scizor.name == definitely_not_scizor.name
        assert scizor.type_equals(definitely_not_scizor.type)
        assert scizor.type_equals(scizor.type)
        assert scizor.base_stats_dict == definitely_not_scizor.base_stats_dict
        assert scizor.base_stats_dict.atk == definitely_not_scizor.base_stats_dict.atk
        assert scizor == definitely_not_scizor

    def test_double_type_pokemon_invalid_comparison(self):
        scizor = PokemonBaseModel(
            name="Scizor",
            types=(PokemonType.Bug, PokemonType.Steel),
            base_stats_dict=StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=60)
        )

        crawdaunt = PokemonBaseModel(
            name="Crawdaunt",
            types=(PokemonType.Water, PokemonType.Dark),
            base_stats_dict=StatsDict(hp=63, atk=130, phys_def=85, spe_atk=90, spe_def=55, spd=55)
        )

        assert scizor.name != crawdaunt.name
        assert not scizor.type_equals(crawdaunt.type)
        assert scizor.base_stats_dict != crawdaunt.base_stats_dict
        assert scizor.base_stats_dict.atk == crawdaunt.base_stats_dict.atk
        assert scizor != crawdaunt

    def test_simple_type_pokemon(self):
        blissey = PokemonBaseModel(
            name="Blissey",
            types=(PokemonType.Normal, None),
            base_stats_dict=StatsDict(hp=255, atk=10, phys_def=10, spe_atk=75, spe_def=135, spd=55)
        )

        assert blissey.name == "Blissey"
        assert blissey.type_equals((PokemonType.Normal, None))
        assert blissey.base_stats_dict == StatsDict(hp=255, atk=10, phys_def=10, spe_atk=75, spe_def=135, spd=55)
        assert blissey.base_stats_dict.hp == 255

    def test_simple_type_pokemon_valid_comparison(self):
        blissey = PokemonBaseModel(
            name="Blissey",
            types=(PokemonType.Normal, None),
            base_stats_dict=StatsDict(hp=255, atk=10, phys_def=10, spe_atk=75, spe_def=135, spd=55)
        )

        definitely_not_blissey = PokemonBaseModel(
            name="Blissey",
            types=(None, PokemonType.Normal),
            base_stats_dict=StatsDict(hp=255, atk=10, phys_def=10, spe_atk=75, spe_def=135, spd=55)
        )

        assert blissey.name == definitely_not_blissey.name
        assert blissey.type_equals(definitely_not_blissey.type)
        assert blissey.base_stats_dict == definitely_not_blissey.base_stats_dict
        assert blissey.base_stats_dict.atk == definitely_not_blissey.base_stats_dict.atk
        assert blissey == definitely_not_blissey

    def test_simple_type_pokemon_invalid_comparison(self):
        blissey = PokemonBaseModel(
            name="Blissey",
            types=(PokemonType.Normal, None),
            base_stats_dict=StatsDict(hp=255, atk=10, phys_def=10, spe_atk=75, spe_def=135, spd=55)
        )

        barraskewda = PokemonBaseModel(
            name="Barraskewda",
            types=(PokemonType.Water, None),
            base_stats_dict=StatsDict(hp=61, atk=123, phys_def=60, spe_atk=60, spe_def=50, spd=136)
        )

        assert blissey.name != barraskewda.name
        assert not blissey.type_equals(barraskewda.type)
        assert blissey.base_stats_dict != barraskewda.base_stats_dict
        assert blissey.base_stats_dict.atk != barraskewda.base_stats_dict.atk
        assert blissey != barraskewda
