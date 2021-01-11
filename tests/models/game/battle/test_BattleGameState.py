from unittest import TestCase

from models.game.battle.BattleGameState import BattleGameState
from models.game.trainer.PokemonTrainer import PokemonTrainer
from models.game.trainer.utils.ArenaBadge import ArenaBadge
from models.pkmn.PokemonModel import PokemonModel
from models.pkmn.moves.PokemonMove import MoveCategory, PokemonMove
from models.pkmn.natures.PokemonNature import PokemonNature
from models.pkmn.stats.StatsDict import StatsDict
from models.pkmn.types.PokemonType import PokemonType


class TestBattleGameState(TestCase):

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
        self.Pidgeot = PokemonModel(
            name="Pidgeot",
            types=(PokemonType.Flying, PokemonType.Normal),
            level=100,
            nature=PokemonNature.Jolly,
            moves=[
                PokemonMove(
                    name="Double Edge",
                    move_type=PokemonType.Normal,
                    category=MoveCategory.Physical,
                    pp=24,
                    power=120
                ),
                PokemonMove(
                    name="Brave Bird",
                    move_type=PokemonType.Flying,
                    category=MoveCategory.Physical,
                    pp=24,
                    power=120
                )
            ],
            base_stats=StatsDict(hp=83, atk=80, phys_def=75, spe_atk=70, spe_def=70, spd=101),
            evs=StatsDict(hp=0, atk=252, phys_def=0, spe_atk=0, spe_def=4, spd=252),
            ivs=StatsDict(hp=31, atk=31, phys_def=31, spe_atk=31, spe_def=31, spd=31)
        )
        self.Blastoise = PokemonModel(
            name="Blastoise",
            types=(PokemonType.Water, None),
            level=100,
            nature=PokemonNature.Modest,
            moves=[
                PokemonMove(
                    name="Hydro Pump",
                    move_type=PokemonType.Water,
                    category=MoveCategory.Special,
                    pp=8,
                    power=110,
                    accuracy=80
                ),
                PokemonMove(
                    name="Ice Beam",
                    move_type=PokemonType.Ice,
                    category=MoveCategory.Special,
                    pp=16,
                    power=90
                )
            ],
            base_stats=StatsDict(hp=79, atk=83, phys_def=100, spe_atk=85, spe_def=105, spd=78),
            evs=StatsDict(hp=252, atk=0, phys_def=0, spe_atk=252, spe_def=4, spd=0),
            ivs=StatsDict(hp=31, atk=31, phys_def=31, spe_atk=31, spe_def=31, spd=31)
        )
        self.Red = PokemonTrainer(
            name="Red",
            team=[self.Pikachu, self.Charizard],
            badges=[ArenaBadge.Boulder, ArenaBadge.Cascade, ArenaBadge.Thunder, ArenaBadge.Rainbow,
                    ArenaBadge.Soul, ArenaBadge.Marsh, ArenaBadge.Marsh, ArenaBadge.Earth]
        )
        self.Blue = PokemonTrainer(
            name="Blue",
            team=[self.Pidgeot, self.Blastoise],
            badges=[ArenaBadge.Boulder, ArenaBadge.Cascade, ArenaBadge.Thunder, ArenaBadge.Rainbow,
                    ArenaBadge.Soul, ArenaBadge.Marsh, ArenaBadge.Marsh, ArenaBadge.Earth]
        )
        self.BattleGameState = BattleGameState(player=self.Red, opponent=self.Blue)

    def test_battle_game_state(self):

        assert self.BattleGameState.player.name == "Red" and self.BattleGameState.opponent.name == "Blue"
        assert self.BattleGameState.turn == 1
        assert self.BattleGameState.getPlayerActivePkmn() == self.Pikachu
        assert self.BattleGameState.getOpponentActivePkmn() == self.Pidgeot
        self.BattleGameState.setPlayerActivePkmn(1)
        assert self.BattleGameState.getPlayerActivePkmn() == self.Charizard
        assert self.BattleGameState.getOpponentActivePkmn() == self.Pidgeot
        self.BattleGameState.setOpponentActivePkmn(1)
        assert self.BattleGameState.getPlayerActivePkmn() == self.Charizard
        assert self.BattleGameState.getOpponentActivePkmn() == self.Blastoise

