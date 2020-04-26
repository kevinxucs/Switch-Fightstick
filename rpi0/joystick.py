import collections
import struct
import time


JoystickReportInput = collections.namedtuple('JoystickReportInput',
                                             ['button', 'hat', 'lx', 'ly',
                                              'rx', 'ry', 'vendor_spec'])


class Joystick(object):

    SWITCH_Y = 0x01
    SWITCH_B = 0x02
    SWITCH_A = 0x04
    SWITCH_X = 0x08
    SWITCH_L = 0x10
    SWITCH_R = 0x20
    SWITCH_ZL = 0x40
    SWITCH_ZR = 0x80
    SWITCH_MINUS = 0x100
    SWITCH_PLUS = 0x200
    SWITCH_LCLICK = 0x400
    SWITCH_RCLICK = 0x800
    SWITCH_HOME = 0x1000
    SWITCH_CAPTURE = 0x2000

    HAT_TOP = 0x00
    HAT_TOP_RIGHT = 0x01
    HAT_RIGHT = 0x02
    HAT_BOTTOM_RIGHT = 0x03
    HAT_BOTTOM = 0x04
    HAT_BOTTOM_LEFT = 0x05
    HAT_LEFT = 0x06
    HAT_TOP_LEFT = 0x07
    HAT_CENTER = 0x08

    STICK_MIN = 0
    STICK_CENTER = 128
    STICK_MAX = 255

    BUTTON_TIME = 0.05

    def __init__(self):
        self.input_struct = struct.Struct('HBBBBBB')

    def _write_report(self, report_input):
        report = self.input_struct.pack(*report_input)
        with open('/dev/hidg0', 'rb+') as f:
            f.write(report)

    def _new_input(self,
                   button=0x0,
                   hat=HAT_CENTER,
                   lx=STICK_CENTER,
                   ly=STICK_CENTER,
                   rx=STICK_CENTER,
                   ry=STICK_CENTER,
                   vendor_spec=0x0):
        ri = JoystickReportInput(button=button,
                                 hat=hat,
                                 lx=lx,
                                 ly=ly,
                                 rx=rx,
                                 ry=ry,
                                 vendor_spec=vendor_spec)
        return ri

    def _press_button(self, button):
        self._write_report(self._new_input(button=button))
        time.sleep(self.BUTTON_TIME)
        self._write_report(self._new_input())

    def press_a(self):
        return self._press_button(self.SWITCH_A)

    def press_b(self):
        return self._press_button(self.SWITCH_B)

    def press_x(self):
        return self._press_button(self.SWITCH_X)

    def press_y(self):
        return self._press_button(self.SWITCH_Y)

    def press_l(self):
        return self._press_button(self.SWITCH_L)

    def press_r(self):
        return self._press_button(self.SWITCH_R)

    def press_zl(self):
        return self._press_button(self.SWITCH_ZL)

    def press_zr(self):
        return self._press_button(self.SWITCH_ZR)

    def press_minus(self):
        return self._press_button(self.SWITCH_MINUS)

    def press_plus(self):
        return self._press_button(self.SWITCH_PLUS)

    def press_lstick(self):
        return self._press_button(self.SWITCH_LSTICK)

    def press_rstick(self):
        return self._press_button(self.SWITCH_RSTICK)

    def press_home(self):
        return self._press_button(self.SWITCH_HOME)

    def press_capture(self):
        return self._press_button(self.SWITCH_CAPTURE)
