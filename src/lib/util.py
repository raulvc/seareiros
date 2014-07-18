'''
    Some general useful stuff I couldn't really categorize
'''
from src.lib.constants import access_table

def bin(s):
    """ returns a binary number (str format) based on an integer (not really needed on python3) """
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

def check_access(access_level, target):
    try:
        bit_representation = bin(access_level)
        bit_target = access_table.index(target) + 1
        return bool(int(bit_representation[-bit_target]))
    except IndexError:
        # undefined permission'
        return False
    except ValueError:
        # target not in permission table (will happen to some stuff I don't want to control)
        return True
