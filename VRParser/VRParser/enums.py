from enum import Enum;
class InvestmentStyle(Enum):
    Growth = 0;
    Blend = 1;
    Value = 2;
    none = 3;
class Capitalisation(Enum):
    Large = 0;
    Mid = 1;
    Small = 2;
    none = 3;