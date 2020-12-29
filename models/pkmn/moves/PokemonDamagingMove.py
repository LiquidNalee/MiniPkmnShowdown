from models.pkmn.utils.PokemonType import PokemonType
from models.combat import CombatGameState


class PokemonDamagingMove:

    def __init__(self, name: str, move_type: PokemonType, pp: int, priority: int,
                 effect: lambda state: CombatGameState, power: int, accuracy: int):
        super().__init__(name=name, move_type=move_type, pp=pp, priority=priority, effect=effect)
        self.power = power
        self.accuracy = accuracy
