from models.game.trainer.PokemonTrainer import PokemonTrainer
from models.pkmn.PokemonModel import PokemonModel


class BattleGameState:

    def __init__(self, player: PokemonTrainer, opponent: PokemonTrainer):
        self.turn = 1
        self.player = player
        self.__player_active_pkmn_slot = 0
        self.opponent = opponent
        self.__opponent_active_pkmn_slot = 0

    def getPlayerActivePkmn(self) -> PokemonModel:
        return self.player.team[self.__player_active_pkmn_slot]

    def getOpponentActivePkmn(self) -> PokemonModel:
        return self.opponent.team[self.__opponent_active_pkmn_slot]

    def setPlayerActivePkmn(self, index: int):
        self.__player_active_pkmn_slot = index

    def setOpponentActivePkmn(self, index: int):
        self.__opponent_active_pkmn_slot = index
