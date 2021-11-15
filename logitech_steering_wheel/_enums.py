import enum


class ForceType(enum.Enum):
    NONE = -1
    SPRING = 0
    CONSTANT = 1
    DAMPER = 2
    SIDE_COLLISION = 3
    FRONTAL_COLLISION = 4
    DIRT_ROAD = 5
    BUMPY_ROAD = 6
    SLIPPERY_ROAD = 7
    SURFACE_EFFECT = 8
    SOFTSTOP = 10
    CAR_AIRBORNE = 11


class PeriodicSurfaceEffect(enum.Enum):
    NONE = -1
    SINE = 0
    SQUARE = 1
    TRIANGLE = 2


class DeviceType(enum.Enum):
    NONE = -1
    WHEEL = 0
    JOYSTICK = 1
    GAMEPAD = 2
    OTHER = 3


class Manufacurer(enum.Enum):
    NONE = -1
    LOGITECH = 0
    MICROSOFT = 1
    OTHER = 2


class Model(enum.Enum):
    G27 = 0
    DRIVING_FORCE_GT = 1
    G25 = 2
    MOMO_RACING = 3
    MOMO_FORCE = 4
    DRIVING_FORCE_PRO = 5
    DRIVING_FORCE = 6
    NASCAR_RACING_WHEEL = 7
    FORMULA_FORCE = 8
    FORMULA_FORCE_GP = 9
    FORCE_3D_PRO = 10
    EXTREME_3D_PRO = 11
    FREEDOM_24 = 12
    ATTACK_3 = 13
    FORCE_3D = 14
    STRIKE_FORCE_3D = 15
    G940_JOYSTICK = 16
    G940_THROTTLE = 17
    G940_PEDALS = 18
    RUMBLEPAD = 19
    RUMBLEPAD_2 = 20
    CORDLESS_RUMBLEPAD_2 = 21
    CORDLESS_GAMEPAD = 22
    DUAL_ACTION_GAMEPAD = 23
    PRECISION_GAMEPAD_2 = 24
    CHILLSTREAM = 25
    G29 = 26
    G920 = 27
