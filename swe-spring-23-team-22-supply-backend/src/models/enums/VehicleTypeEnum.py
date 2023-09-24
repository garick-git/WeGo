import sys
sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from enum import Enum
class VehicleType(Enum):
    SEDAN = 1
    SUV = 2
    VAN = 3