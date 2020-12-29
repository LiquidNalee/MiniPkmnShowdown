from models.game.trainer.PokemonTrainer import PokemonTrainer


class BattleGameState:

    def __init__(self, player: PokemonTrainer, opponent: PokemonTrainer):
        self.turn = 1
        self.player_team = player
        self.opponent_team = opponent
