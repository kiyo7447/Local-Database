from objectbox.model import *

@Entity(id=1, uid=1)
class Person:
    id = Id(id=1, uid=1001)
    name = Property(str, id=2, uid=1002)
    is_enabled = Property(bool, id=3, uid=1003)
    # int can be stored with 64 (default), 32, 16 or 8 bit precision.
    int64 = Property(int, id=4, uid=1004)
    int32 = Property(int, type=PropertyType.int, id=5, uid=1005)
    int16 = Property(int, type=PropertyType.short, id=6, uid=1006)
    int8 = Property(int, type=PropertyType.byte, id=7, uid=1007)
    # float can be stored with 64 or 32 (default) bit precision.
    float64 = Property(float, id=8, uid=1008)
    float32 = Property(float, type=PropertyType.float, id=9, uid=1009)
    byte_array = Property(bytes, id=10, uid=1010)
    # Regular properties are not stored.
    transient = ""
