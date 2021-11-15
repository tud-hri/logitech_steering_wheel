import os

import ctypes
import sys

from logitech_steering_wheel._enums import *
from logitech_steering_wheel._controllerproperties import ControllerPropertiesData, LogiControllerPropertiesData
from logitech_steering_wheel._state import State, DIJOYSTATE2

# import dll and define return types for all functions
_sys_arch = 'x64' if sys.maxsize > 2 ** 32 else 'x86'
_dll_handle = ctypes.windll.LoadLibrary(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib', _sys_arch, 'LogitechSteeringWheelEnginesWrapper.dll'))

_dll_handle.LogiSteeringInitialize.restype = ctypes.c_bool
_dll_handle.LogiSteeringInitializeWithWindow.restype = ctypes.c_bool
_dll_handle.LogiSteeringInitialize.restype = ctypes.c_bool
_dll_handle.LogiSteeringGetSdkVersion.restype = ctypes.c_bool
_dll_handle.LogiUpdate.restype = ctypes.c_bool
_dll_handle.LogiGetState.restype = ctypes.POINTER(DIJOYSTATE2)
_dll_handle.LogiGetDevicePath.restype = ctypes.c_bool
_dll_handle.LogiGetFriendlyProductName.restype = ctypes.c_bool
_dll_handle.LogiIsConnected.restype = ctypes.c_bool
_dll_handle.LogiIsDeviceConnected.restype = ctypes.c_bool
_dll_handle.LogiIsManufacturerConnected.restype = ctypes.c_bool
_dll_handle.LogiIsModelConnected.restype = ctypes.c_bool
_dll_handle.LogiButtonTriggered.restype = ctypes.c_bool
_dll_handle.LogiButtonReleased.restype = ctypes.c_bool
_dll_handle.LogiButtonIsPressed.restype = ctypes.c_bool
_dll_handle.LogiGenerateNonLinearValues.restype = ctypes.c_bool
_dll_handle.LogiGetNonLinearValue.restype = ctypes.c_int
_dll_handle.LogiHasForceFeedback.restype = ctypes.c_bool
_dll_handle.LogiIsPlaying.restype = ctypes.c_bool
_dll_handle.LogiPlaySpringForce.restype = ctypes.c_bool
_dll_handle.LogiStopSpringForce.restype = ctypes.c_bool
_dll_handle.LogiPlayConstantForce.restype = ctypes.c_bool
_dll_handle.LogiStopConstantForce.restype = ctypes.c_bool
_dll_handle.LogiPlayDamperForce.restype = ctypes.c_bool
_dll_handle.LogiStopDamperForce.restype = ctypes.c_bool
_dll_handle.LogiPlaySideCollisionForce.restype = ctypes.c_bool
_dll_handle.LogiPlayFrontalCollisionForce.restype = ctypes.c_bool
_dll_handle.LogiPlayDirtRoadEffect.restype = ctypes.c_bool
_dll_handle.LogiStopDirtRoadEffect.restype = ctypes.c_bool
_dll_handle.LogiPlayBumpyRoadEffect.restype = ctypes.c_bool
_dll_handle.LogiStopBumpyRoadEffect.restype = ctypes.c_bool
_dll_handle.LogiPlaySlipperyRoadEffect.restype = ctypes.c_bool
_dll_handle.LogiStopSlipperyRoadEffect.restype = ctypes.c_bool
_dll_handle.LogiPlaySurfaceEffect.restype = ctypes.c_bool
_dll_handle.LogiStopSurfaceEffect.restype = ctypes.c_bool
_dll_handle.LogiPlayCarAirborne.restype = ctypes.c_bool
_dll_handle.LogiStopCarAirborne.restype = ctypes.c_bool
_dll_handle.LogiPlaySoftstopForce.restype = ctypes.c_bool
_dll_handle.LogiStopSoftstopForce.restype = ctypes.c_bool
_dll_handle.LogiSetPreferredControllerProperties.restype = ctypes.c_bool
_dll_handle.LogiGetCurrentControllerProperties.restype = ctypes.c_bool
_dll_handle.LogiGetShifterMode.restype = ctypes.c_int
_dll_handle.LogiSetOperatingRange.restype = ctypes.c_bool
_dll_handle.LogiGetOperatingRange.restype = ctypes.c_bool
_dll_handle.LogiPlayLeds.restype = ctypes.c_bool
_dll_handle.LogiSteeringShutdown.restype = ctypes.c_void_p


def initialize_with_window(ignore_x_input_controllers: bool, hwnd: int):
    """
    Call this function to initialize if you have already the window handle
    """

    return _dll_handle.LogiSteeringInitializeWithWindow(ctypes.c_bool(ignore_x_input_controllers), ctypes.c_long(hwnd))


def initialize(ignore_x_input_controllers: bool):
    """
    Call this function before any other of the following
    """

    return _dll_handle.LogiSteeringInitialize(ctypes.c_bool(ignore_x_input_controllers))


def get_sdk_version():
    """
    Get the current SDK Version number
    """
    major_version = ctypes.c_int64()
    minor_version = ctypes.c_int64()
    build_version = ctypes.c_int64()

    result = _dll_handle.LogiSteeringGetSdkVersion(ctypes.byref(major_version),
                                                   ctypes.byref(minor_version),
                                                   ctypes.byref(build_version))

    return major_version.value, minor_version.value, build_version.value, result


def update():
    """
    Update the status of the controller
    """

    return _dll_handle.LogiUpdate()


def get_state(index: int) -> State:
    """
    Get the state of the controller in the standard way.

    :returns DIJOYSTATE2*
    """
    c_struct_state_pointer = _dll_handle.LogiGetState(ctypes.c_int(index))
    return State.from_c_struct(c_struct_state_pointer.contents)


def get_device_path(index: int, buffer_size: int):
    """
    Get the computer specific operating system assigned controller GUID at a given index
    """

    buffer = ctypes.create_unicode_buffer(buffer_size)
    result = _dll_handle.LogiGetDevicePath(ctypes.c_int(index), ctypes.byref(buffer), ctypes.c_int(buffer_size))

    return buffer.value, result


def get_friendly_product_name(index: int, buffer_size: int):
    """
    Get the friendly name of the product at index
    """

    buffer = ctypes.create_unicode_buffer(buffer_size)
    result = _dll_handle.LogiGetFriendlyProductName(ctypes.c_int(index), ctypes.byref(buffer),
                                                    ctypes.c_int(buffer_size))

    return buffer.value, result


def is_connected(index: int):
    """
    Check if a generic device at index is connected
    """

    return _dll_handle.LogiIsConnected(ctypes.c_int(index))


def is_device_connected(index: int, device_type: DeviceType):
    """
    Check if the device connected at index is of the same type specified by deviceType
    """

    return _dll_handle.LogiIsDeviceConnected(ctypes.c_int(index), ctypes.c_int(device_type.value))


def is_manufacturer_connected(index: int, manufacturer: Manufacurer):
    """
    Check if the device connected at index is made from the manufacturer specified by manufacturerName
    """

    return _dll_handle.LogiIsManufacturerConnected(ctypes.c_int(index), ctypes.c_int(manufacturer.value))


def is_model_connected(index: int, model: Model):
    """
    Check if the device connected at index is the model specified by modelName
    """

    return _dll_handle.LogiIsModelConnected(ctypes.c_int(index), ctypes.c_int(model.value))


def button_triggered(index: int, button_number: int):
    """
    Check if the device connected at index is currently triggering the button specified by button_number
    """

    return _dll_handle.LogiButtonTriggered(ctypes.c_int(index), ctypes.c_int(button_number))


def button_released(index: int, button_number: int):
    """
    Check if on the device connected at index has been released the button specified by button_number
    """

    return _dll_handle.LogiButtonReleased(ctypes.c_int(index), ctypes.c_int(button_number))


def button_is_pressed(index: int, button_number: int):
    """
    Check if on the device connected at index is currently being pressed the button specified by button_number
    """

    return _dll_handle.LogiButtonIsPressed(ctypes.c_int(index), ctypes.c_int(button_number))


def generate_non_linear_values(index: int, non_linear_coefficient: int):
    """
    Generate non-linear values for the axis of the controller at index
    """

    return _dll_handle.LogiGenerateNonLinearValues(ctypes.c_int(index), ctypes.c_int(non_linear_coefficient))


def get_non_linear_value(index: int, input_value: int):
    """
    Get a non-linear value from a table previously generated
    """

    return _dll_handle.LogiGetNonLinearValue(ctypes.c_int(index), ctypes.c_int(input_value))


def has_force_feedback(index: int):
    """
     Check if the controller at index has force feedback
     """

    return _dll_handle.LogiHasForceFeedback(ctypes.c_int(index))


def is_playing(index: int, force_type: ForceType):
    """
    Check if the controller at index is playing the force specified by forceType
    """

    return _dll_handle.LogiIsPlaying(ctypes.c_int(index), ctypes.c_int(force_type.value))


def play_spring_force(index: int, offset_percentage: int, saturation_percentage: int, coefficient_percentage: int):
    """
    Play the spring force on the controller at index with the specified parameters
    """

    return _dll_handle.LogiPlaySpringForce(ctypes.c_int(index), ctypes.c_int(offset_percentage),
                                           ctypes.c_int(saturation_percentage), ctypes.c_int(coefficient_percentage))


def stop_spring_force(index: int):
    """
    Stop the spring force on the controller at index
    """

    return _dll_handle.LogiStopSpringForce(ctypes.c_int(index))


def play_constant_force(index: int, magnitude_percentage: int):
    """
    Play the constant force on the controller at index with the specified parameter
    """

    return _dll_handle.LogiPlayConstantForce(ctypes.c_int(index), ctypes.c_int(magnitude_percentage))


def stop_constant_force(index: int):
    """
    Stop the constant force on the controller at index
    """

    return _dll_handle.LogiStopConstantForce(ctypes.c_int(index))


def play_damper_force(index: int, coefficient_percentage: int):
    """
    Play the damper force on the controller at index with the specified parameter
    """

    return _dll_handle.LogiPlayDamperForce(ctypes.c_int(index), ctypes.c_int(coefficient_percentage))


def stop_damper_force(index: int):
    """
    Stop the damper force on the controller at index
    """

    return _dll_handle.LogiStopDamperForce(ctypes.c_int(index))


def play_side_collision_force(index: int, magnitude_percentage: int):
    """
    Play the side collision force on the controller at index with the specified parameter
    """

    return _dll_handle.LogiPlaySideCollisionForce(ctypes.c_int(index), ctypes.c_int(magnitude_percentage))


def play_frontal_collision_force(index: int, magnitude_percentage: int):
    """
    Play the frontal collision force on the controller at index with the specified parameter
    """

    return _dll_handle.LogiPlayFrontalCollisionForce(ctypes.c_int(index), ctypes.c_int(magnitude_percentage))


def play_dirt_road_effect(index: int, magnitude_percentage: int):
    """
    Play the dirt road effect on the controller at index with the specified parameter
    """

    return _dll_handle.LogiPlayDirtRoadEffect(ctypes.c_int(index), ctypes.c_int(magnitude_percentage))


def stop_dirt_road_effect(index: int):
    """
    Stop the dirt road effect on the controller at index
    """

    return _dll_handle.LogiStopDirtRoadEffect(ctypes.c_int(index))


def play_bumpy_road_effect(index: int, magnitude_percentage: int):
    """
    Play the bumpy road effect on the controller at index with the specified parameter
    """

    return _dll_handle.LogiPlayBumpyRoadEffect(ctypes.c_int(index), ctypes.c_int(magnitude_percentage))


def stop_bumpy_road_effect(index: int):
    """
    Stop the bumpy road effect on the controller at index
    """

    return _dll_handle.LogiStopBumpyRoadEffect(ctypes.c_int(index))


def play_slippery_road_effect(index: int, magnitude_percentage: int):
    """
    Play the slippery road effect on the controller at index with the specified parameter
    """

    return _dll_handle.LogiPlaySlipperyRoadEffect(ctypes.c_int(index), ctypes.c_int(magnitude_percentage))


def stop_slippery_road_effect(index: int):
    """
    Stop the slippery road effect on the controller at index
    """

    return _dll_handle.LogiStopSlipperyRoadEffect(ctypes.c_int(index))


def play_surface_effect(index: int, effect_type: int, magnitude_percentage: int,
                        periodic_effect: PeriodicSurfaceEffect):
    """
    Play the surface effect on the controller at index with the specified parameter
    """

    return _dll_handle.LogiPlaySurfaceEffect(ctypes.c_int(index), ctypes.c_int(effect_type),
                                             ctypes.c_int(magnitude_percentage), ctypes.c_int(periodic_effect.value))


def stop_surface_effect(index: int):
    """
    Stop the surface effect on the controller at index
    """

    return _dll_handle.LogiStopSurfaceEffect(ctypes.c_int(index))


def play_car_airborne(index: int):
    """
    Play the car airborne effect on the controller at index
    """

    return _dll_handle.LogiPlayCarAirborne(ctypes.c_int(index))


def stop_car_airborne(index: int):
    """
    Stop the car airborne effect on the controller at index
    """

    return _dll_handle.LogiStopCarAirborne(ctypes.c_int(index))


def play_soft_stop_force(index: int, usable_range_percentage: int):
    """
     Play the soft stop force on the controller at index with the specified parameter
     """

    return _dll_handle.LogiPlaySoftstopForce(ctypes.c_int(index), ctypes.c_int(usable_range_percentage))


def stop_soft_stop_force(index: int):
    """
    Stop the soft stop force on the controller at index
    """

    return _dll_handle.LogiStopSoftstopForce(ctypes.c_int(index))


def set_preferred_controller_properties(properties: ControllerPropertiesData):
    """
    Set preferred wheel properties specified by the struct properties
    """

    return _dll_handle.LogiSetPreferredControllerProperties(properties.as_c_struct())


def get_current_controller_properties(index: int):
    """
    Fills the properties parameter with the current controller properties
    """

    c_type_properties = LogiControllerPropertiesData()
    data = ctypes.create_unicode_buffer(36)

    result = _dll_handle.LogiGetCurrentControllerProperties(ctypes.c_int(index), ctypes.pointer(c_type_properties))

    if result:
        python_properties = ControllerPropertiesData.from_c_struct(c_type_properties)
        return python_properties, result
    else:
        return None, result


def get_shifter_mode(index: int):
    """
    get current shifter mode (gated or sequential)
    """

    return _dll_handle.LogiGetShifterMode(ctypes.c_int(index))


def set_operating_range(index: int, motion_range: int):
    """
    Sets the operating range in degrees on the controller at the index.
    """

    return _dll_handle.LogiSetOperatingRange(ctypes.c_int(index), ctypes.c_int(motion_range))


def get_operating_range(index: int):
    """
    Gets the current operating range in degrees on the controller at the index.
    """

    motion_range = ctypes.c_int()
    result = _dll_handle.LogiGetOperatingRange(ctypes.c_int(index), ctypes.byref(motion_range))

    return motion_range.value, result


def play_leds(index: int, current_rpm: float, rpm_first_led_turns_on: float, rpm_red_line: float):
    """
    Play the LEDs on the controller at index applying the specified parameters.
    """

    return _dll_handle.LogiPlayLeds(ctypes.c_int(index), ctypes.c_float(current_rpm),
                                    ctypes.c_float(rpm_first_led_turns_on),
                                    ctypes.c_float(rpm_red_line))


def shutdown():
    """
    Call this function to shutdown the SDK and destroy the controller and wheel objects
    """

    return _dll_handle.LogiSteeringShutdown()
