from pandas import DataFrame
from engine.pkmn.types.TypesBaseRuleSet import TypesBaseRuleSet
from models.pkmn.types.PokemonType import PokemonType


class TypesClassicRuleSet(TypesBaseRuleSet):

    def __init__(self):
        # Init all at 1
        type_effectiveness_chart = DataFrame({ref_pkmn_type: {pkmn_type: 1 for pkmn_type in PokemonType}
                                              for ref_pkmn_type in PokemonType})

        # Normal is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Normal, PokemonType.Ghost] = 0
        #   not very effective against
        type_effectiveness_chart[PokemonType.Normal, PokemonType.Steel] = .5
        type_effectiveness_chart[PokemonType.Normal, PokemonType.Rock] = .5

        # Fire is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Fire, PokemonType.Steel] = 2
        type_effectiveness_chart[PokemonType.Fire, PokemonType.Grass] = 2
        type_effectiveness_chart[PokemonType.Fire, PokemonType.Ice] = 2
        type_effectiveness_chart[PokemonType.Fire, PokemonType.Bug] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Fire, PokemonType.Fire] = .5
        type_effectiveness_chart[PokemonType.Fire, PokemonType.Water] = .5
        type_effectiveness_chart[PokemonType.Fire, PokemonType.Rock] = .5
        type_effectiveness_chart[PokemonType.Fire, PokemonType.Dragon] = .5

        # Water is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Water, PokemonType.Fire] = 2
        type_effectiveness_chart[PokemonType.Water, PokemonType.Ground] = 2
        type_effectiveness_chart[PokemonType.Water, PokemonType.Rock] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Water, PokemonType.Water] = .5
        type_effectiveness_chart[PokemonType.Water, PokemonType.Grass] = .5
        type_effectiveness_chart[PokemonType.Water, PokemonType.Dragon] = .5

        # Electric is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Electric, PokemonType.Ground] = 0
        #   very effective against
        type_effectiveness_chart[PokemonType.Electric, PokemonType.Water] = 2
        type_effectiveness_chart[PokemonType.Electric, PokemonType.Flying] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Electric, PokemonType.Electric] = .5
        type_effectiveness_chart[PokemonType.Electric, PokemonType.Grass] = .5
        type_effectiveness_chart[PokemonType.Electric, PokemonType.Dragon] = .5

        # Grass is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Grass, PokemonType.Water] = 2
        type_effectiveness_chart[PokemonType.Grass, PokemonType.Ground] = 2
        type_effectiveness_chart[PokemonType.Grass, PokemonType.Rock] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Grass, PokemonType.Fire] = .5
        type_effectiveness_chart[PokemonType.Grass, PokemonType.Grass] = .5
        type_effectiveness_chart[PokemonType.Grass, PokemonType.Poison] = .5
        type_effectiveness_chart[PokemonType.Grass, PokemonType.Flying] = .5
        type_effectiveness_chart[PokemonType.Grass, PokemonType.Bug] = .5
        type_effectiveness_chart[PokemonType.Grass, PokemonType.Dragon] = .5
        type_effectiveness_chart[PokemonType.Grass, PokemonType.Steel] = .5

        # Ice is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Ice, PokemonType.Grass] = 2
        type_effectiveness_chart[PokemonType.Ice, PokemonType.Ground] = 2
        type_effectiveness_chart[PokemonType.Ice, PokemonType.Flying] = 2
        type_effectiveness_chart[PokemonType.Ice, PokemonType.Dragon] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Ice, PokemonType.Fire] = .5
        type_effectiveness_chart[PokemonType.Ice, PokemonType.Water] = .5
        type_effectiveness_chart[PokemonType.Ice, PokemonType.Ice] = .5
        type_effectiveness_chart[PokemonType.Ice, PokemonType.Steel] = .5

        # Fighting is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Fighting, PokemonType.Ghost] = 0
        #   very effective against
        type_effectiveness_chart[PokemonType.Fighting, PokemonType.Normal] = 2
        type_effectiveness_chart[PokemonType.Fighting, PokemonType.Ice] = 2
        type_effectiveness_chart[PokemonType.Fighting, PokemonType.Rock] = 2
        type_effectiveness_chart[PokemonType.Fighting, PokemonType.Dark] = 2
        type_effectiveness_chart[PokemonType.Fighting, PokemonType.Steel] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Fighting, PokemonType.Poison] = .5
        type_effectiveness_chart[PokemonType.Fighting, PokemonType.Flying] = .5
        type_effectiveness_chart[PokemonType.Fighting, PokemonType.Psychic] = .5
        type_effectiveness_chart[PokemonType.Fighting, PokemonType.Bug] = .5
        type_effectiveness_chart[PokemonType.Fighting, PokemonType.Fairy] = .5

        # Poison is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Poison, PokemonType.Steel] = 0
        #   very effective against
        type_effectiveness_chart[PokemonType.Poison, PokemonType.Grass] = 2
        type_effectiveness_chart[PokemonType.Poison, PokemonType.Fairy] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Poison, PokemonType.Poison] = .5
        type_effectiveness_chart[PokemonType.Poison, PokemonType.Ground] = .5
        type_effectiveness_chart[PokemonType.Poison, PokemonType.Rock] = .5
        type_effectiveness_chart[PokemonType.Poison, PokemonType.Ghost] = .5

        # Ground is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Ground, PokemonType.Flying] = 0
        #   very effective against
        type_effectiveness_chart[PokemonType.Ground, PokemonType.Fire] = 2
        type_effectiveness_chart[PokemonType.Ground, PokemonType.Electric] = 2
        type_effectiveness_chart[PokemonType.Ground, PokemonType.Poison] = 2
        type_effectiveness_chart[PokemonType.Ground, PokemonType.Rock] = 2
        type_effectiveness_chart[PokemonType.Ground, PokemonType.Steel] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Ground, PokemonType.Grass] = .5
        type_effectiveness_chart[PokemonType.Ground, PokemonType.Bug] = .5

        # Flying is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Flying, PokemonType.Grass] = 2
        type_effectiveness_chart[PokemonType.Flying, PokemonType.Fighting] = 2
        type_effectiveness_chart[PokemonType.Flying, PokemonType.Bug] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Flying, PokemonType.Electric] = .5
        type_effectiveness_chart[PokemonType.Flying, PokemonType.Rock] = .5
        type_effectiveness_chart[PokemonType.Flying, PokemonType.Steel] = .5

        # Psychic is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Psychic, PokemonType.Dark] = 0
        #   very effective against
        type_effectiveness_chart[PokemonType.Psychic, PokemonType.Poison] = 2
        type_effectiveness_chart[PokemonType.Psychic, PokemonType.Fighting] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Psychic, PokemonType.Psychic] = .5
        type_effectiveness_chart[PokemonType.Psychic, PokemonType.Steel] = .5

        # Bug is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Bug, PokemonType.Grass] = 2
        type_effectiveness_chart[PokemonType.Bug, PokemonType.Psychic] = 2
        type_effectiveness_chart[PokemonType.Bug, PokemonType.Dark] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Bug, PokemonType.Fire] = .5
        type_effectiveness_chart[PokemonType.Bug, PokemonType.Fighting] = .5
        type_effectiveness_chart[PokemonType.Bug, PokemonType.Poison] = .5
        type_effectiveness_chart[PokemonType.Bug, PokemonType.Flying] = .5
        type_effectiveness_chart[PokemonType.Bug, PokemonType.Rock] = .5
        type_effectiveness_chart[PokemonType.Bug, PokemonType.Ghost] = .5
        type_effectiveness_chart[PokemonType.Bug, PokemonType.Steel] = .5
        type_effectiveness_chart[PokemonType.Bug, PokemonType.Fairy] = .5

        # Rock is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Rock, PokemonType.Fire] = 2
        type_effectiveness_chart[PokemonType.Rock, PokemonType.Ice] = 2
        type_effectiveness_chart[PokemonType.Rock, PokemonType.Flying] = 2
        type_effectiveness_chart[PokemonType.Rock, PokemonType.Bug] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Rock, PokemonType.Fighting] = .5
        type_effectiveness_chart[PokemonType.Rock, PokemonType.Ground] = .5
        type_effectiveness_chart[PokemonType.Rock, PokemonType.Steel] = .5

        # Ghost is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Ghost, PokemonType.Normal] = 0
        #   very effective against
        type_effectiveness_chart[PokemonType.Ghost, PokemonType.Psychic] = 2
        type_effectiveness_chart[PokemonType.Ghost, PokemonType.Ghost] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Ghost, PokemonType.Dark] = .5

        # Dragon is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Dragon, PokemonType.Fairy] = 0
        #   very effective against
        type_effectiveness_chart[PokemonType.Dragon, PokemonType.Dragon] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Dragon, PokemonType.Steel] = .5

        # Dark is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Dark, PokemonType.Psychic] = 2
        type_effectiveness_chart[PokemonType.Dark, PokemonType.Ghost] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Dark, PokemonType.Fighting] = .5
        type_effectiveness_chart[PokemonType.Dark, PokemonType.Dark] = .5
        type_effectiveness_chart[PokemonType.Dark, PokemonType.Fairy] = .5

        # Steel is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Steel, PokemonType.Ice] = 2
        type_effectiveness_chart[PokemonType.Steel, PokemonType.Rock] = 2
        type_effectiveness_chart[PokemonType.Steel, PokemonType.Fairy] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Steel, PokemonType.Fire] = .5
        type_effectiveness_chart[PokemonType.Steel, PokemonType.Water] = .5
        type_effectiveness_chart[PokemonType.Steel, PokemonType.Electric] = .5
        type_effectiveness_chart[PokemonType.Steel, PokemonType.Steel] = .5

        # Fairy is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Fairy, PokemonType.Fighting] = 2
        type_effectiveness_chart[PokemonType.Fairy, PokemonType.Dark] = 2
        type_effectiveness_chart[PokemonType.Fairy, PokemonType.Dragon] = 2
        #   not very effective against
        type_effectiveness_chart[PokemonType.Fairy, PokemonType.Fire] = .5
        type_effectiveness_chart[PokemonType.Fairy, PokemonType.Poison] = .5
        type_effectiveness_chart[PokemonType.Fairy, PokemonType.Steel] = .5

        super().__init__(type_effectiveness_chart=type_effectiveness_chart)
