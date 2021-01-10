from unittest import TestCase

from models.game.trainer.PokemonTrainer import PokemonTrainer
from models.pkmn.PokemonModel import PokemonModel
from models.pkmn.moves.PokemonMove import PokemonMove, MoveCategory
from models.pkmn.stats.StatsDict import StatsDict
from models.pkmn.types.PokemonType import PokemonType
from models.pkmn.natures.PokemonNature import PokemonNature
from models.game.trainer.utils.ArenaBadge import ArenaBadge


class TestPokemonTrainer(TestCase):

    def setUp(self) -> None:
        self.Pikachu = PokemonModel(
            name="Pikachu",
            types=(PokemonType.Electric, None),
            level=100,
            nature=PokemonNature.Jolly,
            moves=[
                PokemonMove(
                    name="Volt Tackle",
                    move_type=PokemonType.Electric,
                    category=MoveCategory.Physical,
                    pp=24,
                    power=120
                ),
                PokemonMove(
                    name="Iron Tail",
                    move_type=PokemonType.Steel,
                    category=MoveCategory.Physical,
                    pp=24,
                    power=100,
                    accuracy=75
                ),
                PokemonMove(
                    name="Thunderbolt",
                    move_type=PokemonType.Electric,
                    category=MoveCategory.Special,
                    pp=24,
                    power=90
                )
            ],
            base_stats=StatsDict(hp=35, atk=55, phys_def=40, spe_atk=50, spe_def=50, spd=90),
            evs=StatsDict(hp=0, atk=252, phys_def=0, spe_atk=4, spe_def=0, spd=252),
            ivs=StatsDict(hp=31, atk=31, phys_def=31, spe_atk=31, spe_def=31, spd=31)
        )
        self.Charizard = PokemonModel(
            name="Charizard",
            types=(PokemonType.Fire, PokemonType.Flying),
            level=100,
            nature=PokemonNature.Jolly,
            moves=[
                PokemonMove(
                    name="Fire Blast",
                    move_type=PokemonType.Fire,
                    category=MoveCategory.Special,
                    pp=8,
                    power=110,
                    accuracy=85
                ),
                PokemonMove(
                    name="Hurricane",
                    move_type=PokemonType.Flying,
                    category=MoveCategory.Special,
                    pp=16,
                    power=110,
                    accuracy=70
                )
            ],
            base_stats=StatsDict(hp=78, atk=84, phys_def=78, spe_atk=109, spe_def=85, spd=100),
            evs=StatsDict(hp=0, atk=0, phys_def=0, spe_atk=252, spe_def=4, spd=252),
            ivs=StatsDict(hp=31, atk=31, phys_def=31, spe_atk=31, spe_def=31, spd=31)
        )
        self.Red = PokemonTrainer(
            name="Red",
            team=[self.Pikachu, self.Charizard],
            badges=[ArenaBadge.Boulder, ArenaBadge.Cascade, ArenaBadge.Thunder, ArenaBadge.Rainbow,
                    ArenaBadge.Soul, ArenaBadge.Marsh, ArenaBadge.Marsh, ArenaBadge.Earth]
        )

    def testPokemonTrainer(self):
        assert self.Red.team[0] == self.Pikachu
        assert self.Red.team[1] == self.Charizard
        assert self.Red.team[2] is None and self.Red.team[5] is None
        assert self.Red.badges == [ArenaBadge.Boulder, ArenaBadge.Cascade, ArenaBadge.Thunder, ArenaBadge.Rainbow,
                                   ArenaBadge.Soul, ArenaBadge.Marsh, ArenaBadge.Marsh, ArenaBadge.Earth]
