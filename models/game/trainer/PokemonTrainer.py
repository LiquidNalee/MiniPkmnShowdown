from typing import List
from models.game.trainer.utils.ArenaBadge import ArenaBadge

from models.pkmn.PokemonModel import PokemonModel


class PokemonTrainer:

    def __init__(self, name: str, team: List[PokemonModel], badges: List[ArenaBadge]):
        self.name = name
        self.team = [team[i] if i < len(team) else None for i in range(6)]
        self.badges = list(badges)
        self.badges.sort()

    def __str__(self):
        team_str_list = [f"{x}. {self.team[x].name} ({self.team[x].stats.hp}/{self.team[x].max_hp})"
                         for x in range(len(self.team)) if self.team[x] is not None]
        return f"Trainer: {self.name}\n" \
               f"{'  -  '.join(team_str_list)}"

    def hasLost(self):
        return all(pkmn.isKO() if pkmn is not None else True for pkmn in self.team)

    def makeCopy(self):
        return PokemonTrainer(name=self.name, team=list(self.team), badges=list(self.badges))

    @staticmethod
    def fromJson(json: {}):
        if "name" in json and "team" in json:
            return PokemonTrainer(
                name=json["name"],
                team=[PokemonModel.fromJson(json["team"][_]) for _ in json["team"]],
                badges=[]
            )
        raise AttributeError("PokemonTrainer - fromJson: Invalid JSON Input")
