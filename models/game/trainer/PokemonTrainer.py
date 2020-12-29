from typing import List
from models.game.trainer.utils.ArenaBadge import ArenaBadge

from models.pkmn.PokemonModel import PokemonModel


class PokemonTrainer:

    def __init__(self, name: str, team: List[PokemonModel], badges: List[ArenaBadge]):
        self.name = name
        self.team = team
        self.badges = badges
