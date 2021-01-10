from enum import Enum


class ArenaBadge(Enum):
    Boulder = 1
    Cascade = 2
    Thunder = 3
    Rainbow = 4
    Soul = 5
    Marsh = 6
    Volcano = 7
    Earth = 8

    def __lt__(self, other):
        if self.__class__ != other.__class__:
            return NotImplementedError
        return self.value < other.value

