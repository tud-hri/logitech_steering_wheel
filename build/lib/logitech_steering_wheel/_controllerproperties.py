import ctypes


class LogiControllerPropertiesData(ctypes.Structure):
    _fields_ = [
        ('forceEnable', ctypes.c_bool),
        ('overallGain', ctypes.c_int),
        ('springGain', ctypes.c_int),
        ('damperGain', ctypes.c_int),
        ('defaultSpringEnabled', ctypes.c_bool),
        ('defaultSpringGain', ctypes.c_int),
        ('combinePedals', ctypes.c_bool),
        ('wheelRange', ctypes.c_int),
        ('gameSettingsEnabled', ctypes.c_bool),
        ('allowGameSettings', ctypes.c_bool),
    ]


class ControllerPropertiesData:
    def __init__(self, force_enable: bool, overall_gain: int, spring_gain: int, damper_gain: int,
                 default_spring_enabled: bool, default_spring_gain: int, combine_pedals: bool, wheel_range: int,
                 game_settings_enabled: bool, allow_game_settings: bool):
        self.force_enable = force_enable
        self.overall_gain = overall_gain
        self.spring_gain = spring_gain
        self.damper_gain = damper_gain
        self.default_spring_enabled = default_spring_enabled
        self.default_spring_gain = default_spring_gain
        self.combine_pedals = combine_pedals
        self.wheel_range = wheel_range
        self.game_settings_enabled = game_settings_enabled
        self.allow_game_settings = allow_game_settings

    def as_c_struct(self):
        c_struct = LogiControllerPropertiesData()

        c_struct.forceEnable = ctypes.c_bool(self.force_enable)
        c_struct.overallGain = ctypes.c_int(self.overall_gain)
        c_struct.springGain = ctypes.c_int(self.spring_gain)
        c_struct.damperGain = ctypes.c_int(self.damper_gain)
        c_struct.defaultSpringEnabled = ctypes.c_bool(self.default_spring_enabled)
        c_struct.defaultSpringGain = ctypes.c_int(self.default_spring_gain)
        c_struct.combinePedals = ctypes.c_bool(self.combine_pedals)
        c_struct.wheelRange = ctypes.c_int(self.wheel_range)
        c_struct.gameSettingsEnabled = ctypes.c_bool(self.game_settings_enabled)
        c_struct.allowGameSettings = ctypes.c_bool(self.allow_game_settings)

        return c_struct

    @staticmethod
    def from_c_struct(c_struct: LogiControllerPropertiesData):
        new_properties = ControllerPropertiesData(force_enable=c_struct.forceEnable.value,
                                                  overall_gain=c_struct.overallGain.value,
                                                  spring_gain=c_struct.springGain.value,
                                                  damper_gain=c_struct.damperGain.value,
                                                  default_spring_enabled=c_struct.defaultSpringEnabled.value,
                                                  default_spring_gain=c_struct.defaultSpringGain.value,
                                                  combine_pedals=c_struct.combinePedals.value,
                                                  wheel_range=c_struct.wheelRange.value,
                                                  game_settings_enabled=c_struct.gameSettingsEnabled.value,
                                                  allow_game_settings=c_struct.allowGameSettings.value)
        return new_properties
