# Logitech Steering Wheel Module

This module allows access from Python to the steering wheel SDK provided by Logitech for their gaming steering wheels. The API of this module is the same as the "Logitech Gaming Steering Wheel SDK" version 8.75.30. This SDK and it's documentation can be downloaded from the [Logitech G website](https://www.logitechg.com/en-us/innovation/developer-lab.html). The module has been tested on Python 3.8 and only works on Windows.  

This module includes part of the before mentioned steering wheel SDK (the `LogitechSteeringwheel.dll` and `LogitechSteeringWheelEnginesWrapper.dll` files). These files do not fall under the open source license with the rest of the module. They are re-distributed with permission from Logitech (also see the README file in the SDK). Therefore, there is no need to obtain the SDK. The only dependency of this module is the Logitech Gaming Software.

## Installation instructions

The `logitech-steering-wheel` module is available from PyPi and can be installed using pip (`pip install logitech-steering-wheel`). The only dependency is the Logitech Gaming Software that can be downloaded for [Logitech's website](https://support.logi.com/hc/en-gb/articles/360025298053-Logitech-Gaming-Software). The module has been tested with version 5.10. This version works with older steering wheels. According to Logitech, the SDK is also compatible with newer versions of the gaming software.

In some cases, Windows has been known to install other drivers when a steering wheel is plugged in. These default drivers installed by Windows do not work with the SDK. The solution to is problem is to:
1) plug in the steering wheel,
2) uninstall the driver Windows automatically installed, and leave steering wheel plugged-in and turned on, and
3) Install the Logitech Gaming Software (this should automatically install the correct drivers)

## Test/Example

The script below can be used to test the connection with a steering wheel and serves as an example of how to connect, get the current state, and play force feedback effects. This example and a GUI based example can be found on the GitHub repo of this module.

```
import time

import logitech_steering_wheel as lsw
import pygetwindow as gw


if __name__ == '__main__':
    # The steering wheel should be connected to s specific window, the first step is to get the window handle and initialize the SDK
    
    window_handle = gw.getActiveWindow()._hWnd
    initialized = lsw.initialize_with_window(ignore_x_input_controllers=True, hwnd=window_handle)

    print("SDK version is: " + str(lsw.get_sdk_version()))

    connected = lsw.is_connected(0)

    lsw.update()

    # Check if setting and Getting of the operating range works 
    operated = lsw.set_operating_range(0, 100)
    print(lsw.get_operating_range(0))

    if connected and generated:
        print('Steering wheel online')
    else:
        print('Connection failed')
        exit()

    # The update function is called to update the current state, the get state function returns a state object representing the current state of the 
    # steering wheel
    lsw.update()
    s = lsw.get_state(0)
    print(s)

    # Test the force feedback by playing the bumpy road effect on 20 percent of its maximal magnitude 
    lsw.play_bumpy_road_effect(0, 20)

    time.sleep(2.)

    lsw.stop_bumpy_road_effect(0)

    # close the connection
    lsw.shutdown()
```
