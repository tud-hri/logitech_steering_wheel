import ctypes


class DIJOYSTATE2(ctypes.Structure):
    _fields_ = [
        ('lX', ctypes.c_int),
        ('lY', ctypes.c_int),
        ('lZ', ctypes.c_int),
        ('lRx', ctypes.c_int),
        ('lRy', ctypes.c_int),
        ('lRz', ctypes.c_int),
        ('rglSlider', ctypes.c_int * 2),
        ('rgdwPOV', ctypes.c_uint * 4),
        ('rgbButtons', ctypes.c_byte * 128),
        ('lVX', ctypes.c_int),
        ('lVY', ctypes.c_int),
        ('lVZ', ctypes.c_int),
        ('lVRx', ctypes.c_int),
        ('lVRy', ctypes.c_int),
        ('lVRz', ctypes.c_int),
        ('rglVSlider', ctypes.c_int * 2),
        ('lAX', ctypes.c_int),
        ('lAY', ctypes.c_int),
        ('lAZ', ctypes.c_int),
        ('lARx', ctypes.c_int),
        ('lARy', ctypes.c_int),
        ('lARz', ctypes.c_int),
        ('rglASlider', ctypes.c_int * 2),
        ('lFX', ctypes.c_int),
        ('lFY', ctypes.c_int),
        ('lFZ', ctypes.c_int),
        ('lFRx', ctypes.c_int),
        ('lFRy', ctypes.c_int),
        ('lFRz', ctypes.c_int),
        ('rglFSlider', ctypes.c_int * 2),
    ]


class State:
    def __init__(self, lX: int, lY: int, lZ: int, lRx: int, lRy: int, lRz: int, rglSlider: list, rgdwPOV: list,
                 rgbButtons: list, lVX: int, lVY: int, lVZ: int, lVRx: int, lVRy: int, lVRz: int, rglVSlider: list,
                 lAX: int, lAY: int, lAZ: int, lARx: int, lARy: int, lARz: int, rglASlider: list, lFX: int, lFY: int,
                 lFZ: int, lFRx: int, lFRy: int, lFRz: int, rglFSlider: list):

        self.lX = lX
        self.lY = lY
        self.lZ = lZ
        self.lRx = lRx
        self.lRy = lRy
        self.lRz = lRz
        self.rglSlider = rglSlider
        self.rgdwPOV = rgdwPOV
        self.rgbButtons = rgbButtons
        self.lVX = lVX
        self.lVY = lVY
        self.lVZ = lVZ
        self.lVRx = lVRx
        self.lVRy = lVRy
        self.lVRz = lVRz
        self.rglVSlider = rglVSlider
        self.lAX = lAX
        self.lAY = lAY
        self.lAZ = lAZ
        self.lARx = lARx
        self.lARy = lARy
        self.lARz = lARz
        self.rglASlider = rglASlider
        self.lFX = lFX
        self.lFY = lFY
        self.lFZ = lFZ
        self.lFRx = lFRx
        self.lFRy = lFRy
        self.lFRz = lFRz
        self.rglFSlider = rglFSlider

    def as_c_struct(self):
        c_struct = DIJOYSTATE2()

        c_struct.lX = self.lX
        c_struct.lY = self.lY
        c_struct.lZ = self.lZ
        c_struct.lRx = self.lRx
        c_struct.lRy = self.lRy
        c_struct.lRz = self.lRz

        for index, item in enumerate(self.rglSlider):
            c_struct.rglSlider[index] = ctypes.c_long(item)

        for index, item in enumerate(self.rgdwPOV):
            c_struct.rgdwPOV[index] = item

        for index, item in enumerate(self.rgbButtons):
            c_struct.rgbButtons[index] = item

        c_struct.lVX = self.lVX
        c_struct.lVY = self.lVY
        c_struct.lVZ = self.lVZ
        c_struct.lVRx = self.lVRx
        c_struct.lVRy = self.lVRy
        c_struct.lVRz = self.lVRz

        for index, item in enumerate(self.rglVSlider):
            c_struct.rglVSlider[index] = item

        c_struct.lAX = self.lAX
        c_struct.lAY = self.lAY
        c_struct.lAZ = self.lAZ
        c_struct.lARx = self.lARx
        c_struct.lARy = self.lARy
        c_struct.lARz = self.lARz

        for index, item in enumerate(self.rglASlider):
            c_struct.rglASlider[index] = item

        c_struct.lFX = self.lFX
        c_struct.lFY = self.lFY
        c_struct.lFZ = self.lFZ
        c_struct.lFRx = self.lFRx
        c_struct.lFRy = self.lFRy
        c_struct.lFRz = self.lFRz

        for index, item in enumerate(self.rglFSlider):
            c_struct.rglFSlider[index] = item

        return c_struct

    @staticmethod
    def from_c_struct(c_struct: DIJOYSTATE2):
        rglSlider = list(c_struct.rglSlider)
        rgdwPOV = list(c_struct.rgdwPOV)
        rgbButtons = list(c_struct.rgbButtons)
        rglVSlider = list(c_struct.rglVSlider)
        rglASlider = list(c_struct.rglASlider)
        rglFSlider = list(c_struct.rglFSlider)

        new_state = State(lX=c_struct.lX,
                          lY=c_struct.lY,
                          lZ=c_struct.lZ,
                          lRx=c_struct.lRx,
                          lRy=c_struct.lRy,
                          lRz=c_struct.lRz,
                          rglSlider=rglSlider,
                          rgdwPOV=rgdwPOV,
                          rgbButtons=rgbButtons,
                          lVX=c_struct.lVX,
                          lVY=c_struct.lVY,
                          lVZ=c_struct.lVZ,
                          lVRx=c_struct.lVRx,
                          lVRy=c_struct.lVRy,
                          lVRz=c_struct.lVRz,
                          rglVSlider=rglVSlider,
                          lAX=c_struct.lAX,
                          lAY=c_struct.lAY,
                          lAZ=c_struct.lAZ,
                          lARx=c_struct.lARx,
                          lARy=c_struct.lARy,
                          lARz=c_struct.lARz,
                          rglASlider=rglASlider,
                          lFX=c_struct.lFX,
                          lFY=c_struct.lFY,
                          lFZ=c_struct.lFZ,
                          lFRx=c_struct.lFRx,
                          lFRy=c_struct.lFRy,
                          lFRz=c_struct.lFRz,
                          rglFSlider=rglFSlider)

        return new_state
