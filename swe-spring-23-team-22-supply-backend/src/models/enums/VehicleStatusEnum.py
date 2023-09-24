import sys
sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from enum import Enum
class VehicleEmergencyStatus(Enum):
    AVAILABLE = 1
    IN_PROGRESS = 2
    EMERGENCY = 3
    UNREGISTERED = 4