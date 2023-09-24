import sys
sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from enum import Enum
class PluginType(Enum):
    VACCINES = 1
    BLOOD = 2