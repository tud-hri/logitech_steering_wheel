import ctypes
import time

import logitech_steering_wheel as lsw
import pygetwindow as gw


if __name__ == '__main__':
    w = gw.getActiveWindow()._hWnd
    initialized = lsw.initialize_with_window(True, w)
    # initialized = lsw.initialize(True)

    print("SDK version is: " + str(lsw.get_sdk_version()))

    connected = lsw.is_connected(0)

    lsw.update()

    generated = lsw.generate_non_linear_values(0, -40)
    operated = lsw.set_operating_range(0, 100)
    print(lsw.get_operating_range(0))

    if connected and generated:
        print('Steering wheel online')
    else:
        print('Connection failed')
        exit()

    lsw.update()
    s = lsw.get_state(0)

    lsw.play_bumpy_road_effect(0, 20)

    time.sleep(2.)

    lsw.stop_bumpy_road_effect(0)

    # p, r = lsw.get_current_controller_properties(0)

    # print(p, r)

    # print(lsw.get_friendly_product_name(0, 100))

    # print(ctypes.sizeof(s))
    # print(s.lX)
    # print([a for a in s.rgbButtons])
    #
    # for r in range(10):
    #     # print(w == gw.getActiveWindow()._hWnd)
    #     lsw.update()
    #     s = lsw.get_state(0)
    #     print(s.lX)

    lsw.shutdown()
