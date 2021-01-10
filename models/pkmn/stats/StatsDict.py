

class StatsDict:

    def __init__(self, hp: int = 0, atk: int = 0, phys_def: int = 0, spe_atk: int = 0, spe_def: int = 0, spd: int = 0):
        self.hp = int(hp)
        self.atk = int(atk)
        self.phys_def = int(phys_def)
        self.spe_atk = int(spe_atk)
        self.spe_def = int(spe_def)
        self.spd = int(spd)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplementedError
        return self.__dict__ == other.__dict__

    def __getitem__(self, item: str):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = int(value)

    @classmethod
    def from_json(cls, json: {}):
        keys = cls.__dict__.keys()
        if all(keys) in json:
            return StatsDict(**{key: json[key] for key in keys})
