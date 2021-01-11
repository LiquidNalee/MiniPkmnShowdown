from argparse import ArgumentParser
from json import load

from database.DatabaseConfig import updatePkmnDatabase, updateMoveDatabase

from engine.game.BattleEngine import BattleEngine
from engine.pkmn.types.ClassicTypesRuleSet import ClassicTypesRuleSet
from models.game.battle.BattleGameState import BattleGameState
from models.game.trainer.PokemonTrainer import PokemonTrainer
from models.game.trainer.utils.ArenaBadge import ArenaBadge
from models.pkmn.PokemonModel import PokemonModel
from models.pkmn.moves.PokemonMove import PokemonMove, MoveCategory
from models.pkmn.natures.PokemonNature import PokemonNature
from models.pkmn.stats.StatsDict import StatsDict
from models.pkmn.types.PokemonType import PokemonType

parser = ArgumentParser()
parser.add_argument("--update_db", "-u", help="Fill out Pkmn info as json in database folder for future use",
                    type=bool, required=False)
parser.add_argument("--player_trainer_json", "-p", help="Path to player's pokemon trainer json",
                    type=str, required=False)
parser.add_argument("--opponent_trainer_json", "-o", help="Path to opponent's pokemon trainer json",
                    type=str, required=False)
args = parser.parse_args()


def setUpDefaultTeams():
    pikachu = PokemonModel(
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
    charizard = PokemonModel(
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
    pidgeot = PokemonModel(
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
    blastoise = PokemonModel(
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
    red = PokemonTrainer(
        name="Red",
        team=[pikachu, charizard],
        badges=[ArenaBadge.Boulder, ArenaBadge.Cascade, ArenaBadge.Thunder, ArenaBadge.Rainbow,
                ArenaBadge.Soul, ArenaBadge.Marsh, ArenaBadge.Marsh, ArenaBadge.Earth]
    )
    blue = PokemonTrainer(
        name="Blue",
        team=[pidgeot, blastoise],
        badges=[ArenaBadge.Boulder, ArenaBadge.Cascade, ArenaBadge.Thunder, ArenaBadge.Rainbow,
                ArenaBadge.Soul, ArenaBadge.Marsh, ArenaBadge.Marsh, ArenaBadge.Earth]
    )
    return red, blue


def main():
    if args.update_db:
        updatePkmnDatabase([str(_) for _ in range(10)])
        updateMoveDatabase(["Swords Dance", "Meteor Mash", "Close Combat", "Mach Punch", "Aura Sphere", "Bug Bite",
                            "Hydro Pump", "Surf", "Waterfall", "Moonblast", "Play Rough", "Solar Beam", "Wood Hammer",
                            "Stone Edge", "Meteor Gem", "Sludge Bomb", "Poison Jab", "Draco Meteor", "Outrage",
                            "Dragon Dance", "Psychic", "Zen Headbutt", "Mystical Fire", "Fire Blast", "Flare Blitz",
                            "Hurricane", "Brave Bird", "Earthquake", "Earth Power"])

    player, opponent = setUpDefaultTeams()

    if args.player_trainer_json:
        with open(args.player_trainer_json) as player_trainer_json_file:
            player = PokemonTrainer.fromJson(load(player_trainer_json_file))
    if args.opponent_trainer_json:
        with open(args.opponent_trainer_json) as opponent_trainer_json_file:
            opponent = PokemonTrainer.fromJson(load(opponent_trainer_json_file))

    engine = BattleEngine(battleGameState=BattleGameState(player=player, opponent=opponent),
                          typesRuleSet=ClassicTypesRuleSet())
    engine.startGame()


if __name__ == "__main__":
    main()
