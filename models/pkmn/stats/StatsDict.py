

class StatsDict:

    def __init__(self, hp: int, atk: int, phys_def: int, spe_atk: int, spe_def: int, spd: int):
        self.hp = hp
        self.atk = atk
        self.phys_def = phys_def
        self.spe_atk = spe_atk
        self.spe_def = spe_def
        self.spd = spd

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @classmethod
    def from_json(cls, json: {}):
        keys = cls.__dict__.keys()
        if all(keys) in json:
            return StatsDict(**{key: json[key] for key in keys})
