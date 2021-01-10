from pandas import DataFrame
from engine.pkmn.types.TypesBaseRuleSet import TypesBaseRuleSet
from models.pkmn.types.PokemonType import PokemonType


class ClassicTypesRuleSet(TypesBaseRuleSet):

    def __init__(self):
        # Init all at 1
        type_effectiveness_chart = DataFrame({ref_pkmn_type: {pkmn_type: float(1) for pkmn_type in PokemonType}
                                              for ref_pkmn_type in PokemonType})

        # Normal is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Normal][PokemonType.Ghost] = float(0)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Normal][PokemonType.Steel] = float(.5)
        type_effectiveness_chart[PokemonType.Normal][PokemonType.Rock] = float(.5)

        # Fire is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Fire][PokemonType.Steel] = float(2)
        type_effectiveness_chart[PokemonType.Fire][PokemonType.Grass] = float(2)
        type_effectiveness_chart[PokemonType.Fire][PokemonType.Ice] = float(2)
        type_effectiveness_chart[PokemonType.Fire][PokemonType.Bug] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Fire][PokemonType.Fire] = float(.5)
        type_effectiveness_chart[PokemonType.Fire][PokemonType.Water] = float(.5)
        type_effectiveness_chart[PokemonType.Fire][PokemonType.Rock] = float(.5)
        type_effectiveness_chart[PokemonType.Fire][PokemonType.Dragon] = float(.5)

        # Water is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Water][PokemonType.Fire] = float(2)
        type_effectiveness_chart[PokemonType.Water][PokemonType.Ground] = float(2)
        type_effectiveness_chart[PokemonType.Water][PokemonType.Rock] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Water][PokemonType.Water] = float(.5)
        type_effectiveness_chart[PokemonType.Water][PokemonType.Grass] = float(.5)
        type_effectiveness_chart[PokemonType.Water][PokemonType.Dragon] = float(.5)

        # Electric is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Electric][PokemonType.Ground] = float(0)
        #   very effective against
        type_effectiveness_chart[PokemonType.Electric][PokemonType.Water] = float(2)
        type_effectiveness_chart[PokemonType.Electric][PokemonType.Flying] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Electric][PokemonType.Electric] = float(.5)
        type_effectiveness_chart[PokemonType.Electric][PokemonType.Grass] = float(.5)
        type_effectiveness_chart[PokemonType.Electric][PokemonType.Dragon] = float(.5)

        # Grass is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Grass][PokemonType.Water] = float(2)
        type_effectiveness_chart[PokemonType.Grass][PokemonType.Ground] = float(2)
        type_effectiveness_chart[PokemonType.Grass][PokemonType.Rock] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Grass][PokemonType.Fire] = float(.5)
        type_effectiveness_chart[PokemonType.Grass][PokemonType.Grass] = float(.5)
        type_effectiveness_chart[PokemonType.Grass][PokemonType.Poison] = float(.5)
        type_effectiveness_chart[PokemonType.Grass][PokemonType.Flying] = float(.5)
        type_effectiveness_chart[PokemonType.Grass][PokemonType.Bug] = float(.5)
        type_effectiveness_chart[PokemonType.Grass][PokemonType.Dragon] = float(.5)
        type_effectiveness_chart[PokemonType.Grass][PokemonType.Steel] = float(.5)

        # Ice is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Ice][PokemonType.Grass] = float(2)
        type_effectiveness_chart[PokemonType.Ice][PokemonType.Ground] = float(2)
        type_effectiveness_chart[PokemonType.Ice][PokemonType.Flying] = float(2)
        type_effectiveness_chart[PokemonType.Ice][PokemonType.Dragon] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Ice][PokemonType.Fire] = float(.5)
        type_effectiveness_chart[PokemonType.Ice][PokemonType.Water] = float(.5)
        type_effectiveness_chart[PokemonType.Ice][PokemonType.Ice] = float(.5)
        type_effectiveness_chart[PokemonType.Ice][PokemonType.Steel] = float(.5)

        # Fighting is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Fighting][PokemonType.Ghost] = float(0)
        #   very effective against
        type_effectiveness_chart[PokemonType.Fighting][PokemonType.Normal] = float(2)
        type_effectiveness_chart[PokemonType.Fighting][PokemonType.Ice] = float(2)
        type_effectiveness_chart[PokemonType.Fighting][PokemonType.Rock] = float(2)
        type_effectiveness_chart[PokemonType.Fighting][PokemonType.Dark] = float(2)
        type_effectiveness_chart[PokemonType.Fighting][PokemonType.Steel] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Fighting][PokemonType.Poison] = float(.5)
        type_effectiveness_chart[PokemonType.Fighting][PokemonType.Flying] = float(.5)
        type_effectiveness_chart[PokemonType.Fighting][PokemonType.Psychic] = float(.5)
        type_effectiveness_chart[PokemonType.Fighting][PokemonType.Bug] = float(.5)
        type_effectiveness_chart[PokemonType.Fighting][PokemonType.Fairy] = float(.5)

        # Poison is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Poison][PokemonType.Steel] = float(0)
        #   very effective against
        type_effectiveness_chart[PokemonType.Poison][PokemonType.Grass] = float(2)
        type_effectiveness_chart[PokemonType.Poison][PokemonType.Fairy] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Poison][PokemonType.Poison] = float(.5)
        type_effectiveness_chart[PokemonType.Poison][PokemonType.Ground] = float(.5)
        type_effectiveness_chart[PokemonType.Poison][PokemonType.Rock] = float(.5)
        type_effectiveness_chart[PokemonType.Poison][PokemonType.Ghost] = float(.5)

        # Ground is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Ground][PokemonType.Flying] = float(0)
        #   very effective against
        type_effectiveness_chart[PokemonType.Ground][PokemonType.Fire] = float(2)
        type_effectiveness_chart[PokemonType.Ground][PokemonType.Electric] = float(2)
        type_effectiveness_chart[PokemonType.Ground][PokemonType.Poison] = float(2)
        type_effectiveness_chart[PokemonType.Ground][PokemonType.Rock] = float(2)
        type_effectiveness_chart[PokemonType.Ground][PokemonType.Steel] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Ground][PokemonType.Grass] = float(.5)
        type_effectiveness_chart[PokemonType.Ground][PokemonType.Bug] = float(.5)

        # Flying is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Flying][PokemonType.Grass] = float(2)
        type_effectiveness_chart[PokemonType.Flying][PokemonType.Fighting] = float(2)
        type_effectiveness_chart[PokemonType.Flying][PokemonType.Bug] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Flying][PokemonType.Electric] = float(.5)
        type_effectiveness_chart[PokemonType.Flying][PokemonType.Rock] = float(.5)
        type_effectiveness_chart[PokemonType.Flying][PokemonType.Steel] = float(.5)

        # Psychic is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Psychic][PokemonType.Dark] = float(0)
        #   very effective against
        type_effectiveness_chart[PokemonType.Psychic][PokemonType.Poison] = float(2)
        type_effectiveness_chart[PokemonType.Psychic][PokemonType.Fighting] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Psychic][PokemonType.Psychic] = float(.5)
        type_effectiveness_chart[PokemonType.Psychic][PokemonType.Steel] = float(.5)

        # Bug is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Bug][PokemonType.Grass] = float(2)
        type_effectiveness_chart[PokemonType.Bug][PokemonType.Psychic] = float(2)
        type_effectiveness_chart[PokemonType.Bug][PokemonType.Dark] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Bug][PokemonType.Fire] = float(.5)
        type_effectiveness_chart[PokemonType.Bug][PokemonType.Fighting] = float(.5)
        type_effectiveness_chart[PokemonType.Bug][PokemonType.Poison] = float(.5)
        type_effectiveness_chart[PokemonType.Bug][PokemonType.Flying] = float(.5)
        type_effectiveness_chart[PokemonType.Bug][PokemonType.Rock] = float(.5)
        type_effectiveness_chart[PokemonType.Bug][PokemonType.Ghost] = float(.5)
        type_effectiveness_chart[PokemonType.Bug][PokemonType.Steel] = float(.5)
        type_effectiveness_chart[PokemonType.Bug][PokemonType.Fairy] = float(.5)

        # Rock is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Rock][PokemonType.Fire] = float(2)
        type_effectiveness_chart[PokemonType.Rock][PokemonType.Ice] = float(2)
        type_effectiveness_chart[PokemonType.Rock][PokemonType.Flying] = float(2)
        type_effectiveness_chart[PokemonType.Rock][PokemonType.Bug] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Rock][PokemonType.Fighting] = float(.5)
        type_effectiveness_chart[PokemonType.Rock][PokemonType.Ground] = float(.5)
        type_effectiveness_chart[PokemonType.Rock][PokemonType.Steel] = float(.5)

        # Ghost is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Ghost][PokemonType.Normal] = float(0)
        #   very effective against
        type_effectiveness_chart[PokemonType.Ghost][PokemonType.Psychic] = float(2)
        type_effectiveness_chart[PokemonType.Ghost][PokemonType.Ghost] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Ghost][PokemonType.Dark] = float(.5)

        # Dragon is:
        #   ineffective against
        type_effectiveness_chart[PokemonType.Dragon][PokemonType.Fairy] = float(0)
        #   very effective against
        type_effectiveness_chart[PokemonType.Dragon][PokemonType.Dragon] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Dragon][PokemonType.Steel] = float(.5)

        # Dark is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Dark][PokemonType.Psychic] = float(2)
        type_effectiveness_chart[PokemonType.Dark][PokemonType.Ghost] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Dark][PokemonType.Fighting] = float(.5)
        type_effectiveness_chart[PokemonType.Dark][PokemonType.Dark] = float(.5)
        type_effectiveness_chart[PokemonType.Dark][PokemonType.Fairy] = float(.5)

        # Steel is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Steel][PokemonType.Ice] = float(2)
        type_effectiveness_chart[PokemonType.Steel][PokemonType.Rock] = float(2)
        type_effectiveness_chart[PokemonType.Steel][PokemonType.Fairy] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Steel][PokemonType.Fire] = float(.5)
        type_effectiveness_chart[PokemonType.Steel][PokemonType.Water] = float(.5)
        type_effectiveness_chart[PokemonType.Steel][PokemonType.Electric] = float(.5)
        type_effectiveness_chart[PokemonType.Steel][PokemonType.Steel] = float(.5)

        # Fairy is:
        #   very effective against
        type_effectiveness_chart[PokemonType.Fairy][PokemonType.Fighting] = float(2)
        type_effectiveness_chart[PokemonType.Fairy][PokemonType.Dark] = float(2)
        type_effectiveness_chart[PokemonType.Fairy][PokemonType.Dragon] = float(2)
        #   not very effective against
        type_effectiveness_chart[PokemonType.Fairy][PokemonType.Fire] = float(.5)
        type_effectiveness_chart[PokemonType.Fairy][PokemonType.Poison] = float(.5)
        type_effectiveness_chart[PokemonType.Fairy][PokemonType.Steel] = float(.5)

        super().__init__(type_effectiveness_chart=type_effectiveness_chart)
