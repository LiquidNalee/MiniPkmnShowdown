from unittest import TestCase

from database.DatabaseConfig import getPkmnDatabase

from models.game.trainer.PokemonTrainer import PokemonTrainer
from models.pkmn.natures.PokemonNature import PokemonNature
from models.pkmn.stats.StatsDict import StatsDict
from models.pkmn.types.PokemonType import PokemonType


class TestDatabaseInit(TestCase):

    def test_database_init(self):
        trainer_json = {
            "name": "Red",
            "team": {
                "0": {
                    "name": "Scizor",
                    "level": 100,
                    "nature": "Adamant",
                    "moves": ["Bullet Punch"],
                    "evs": {"hp": 120, "atk": 252, "phys_def": 0, "spe_atk": 0, "spe_def": 0, "spd": 136},
                    "ivs": {"hp": 31, "atk": 31, "phys_def": 31, "spe_atk": 31, "spe_def": 31, "spd": 31}
                }
            }
        }
        trainer = PokemonTrainer.fromJson(trainer_json)

        assert trainer.name == "Red"
        assert trainer.team[1] is None
        assert trainer.team[0].name == "Scizor"
        assert trainer.team[0].level == 100
        assert trainer.team[0]._nature == PokemonNature.Adamant
        assert trainer.team[0].moves[0].type == PokemonType.Steel
        assert trainer.team[0].moves[0].power == 40
        assert trainer.team[0].moves[0].accuracy == 100
        assert trainer.team[0].base_stats == StatsDict(hp=70, atk=130, phys_def=100, spe_atk=55, spe_def=80, spd=65)
        assert trainer.team[0].stats == StatsDict(hp=311, atk=394, phys_def=236, spe_atk=131, spe_def=196, spd=200)

    def test_database_update(self):
        db = getPkmnDatabase(["tyranitar"])

        assert "tyranitar" in db
        expected_json = {
            "type": {"0": "rock", "1": "dark"},
            "base_stats": {
                "hp": 100,
                "atk": 134,
                "phys_def": 110,
                "spe_atk": 95,
                "spe_def": 100,
                "spd": 61
            }
        }
        assert db["tyranitar"] == expected_json
