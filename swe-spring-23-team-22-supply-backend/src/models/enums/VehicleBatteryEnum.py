import sys
sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from enum import Enum
class VehicleBatteryStatus(Enum):
    # PowerStatus for vehicle battery
    Dead = 0
    CriticallyLowPower = 1
    LowPower = 2
    FairPower = 3
    FullPower = 4