from enum import IntEnum, StrEnum


class EngineTypes(StrEnum):
    DIESEL = "Diesel"
    ELECTRIC = "Electric"
    GASOLINE = "Gasoline"


class SeatsMetadata(IntEnum):
    MIN_COUNT = 2
    STANDARD_COUNT = 5
    MAX_COUNT = 8
