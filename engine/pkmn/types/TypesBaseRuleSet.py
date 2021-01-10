from pandas import DataFrame
from models.pkmn.types.PokemonType import PokemonType


class TypesBaseRuleSet:

    # .loc on DataFrame: effectiveness of attack on defense
    # .iloc on DataFrame: effectiveness of defense on attack

    def __init__(self, type_effectiveness_chart: DataFrame):
        self.type_effectiveness_chart = type_effectiveness_chart

    def __getitem__(self, item: PokemonType) -> (DataFrame, DataFrame):
        return self.type_effectiveness_chart.loc(item), self.type_effectiveness_chart.iloc(item)

    def getEffectiveness(self, attack_type: PokemonType, defender_type: (PokemonType, PokemonType)) -> float:
        return self.type_effectiveness_chart[attack_type][defender_type[0]] \
                * self.type_effectiveness_chart[attack_type][defender_type[1]] if defender_type[1] is not None else 1
