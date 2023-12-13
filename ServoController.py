import digitalio
import time
import board
# led = digitalio.DigitalInOut(board.LED)
# led.direction = digitalio.Direction.OUTPUT
# print("pre LEDing")
# x = 0
# while x<2:
#     led.value = True
#     time.sleep(0.5)
#     led.value = False
#     time.sleep(0.5)
#     print("LEDing")
#     x += 1
#     print ("x = ",x)
# print("done LEDing")
# SPDX-FileCopyrightText: 2020 Dan Halbert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
# pylint: disable=unused-import
import board
import busio
import pwmio
from digitalio import DigitalInOut
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_airlift.esp32 import ESP32
from adafruit_motor import servo
# If you are using a Metro M4 Airlift Lite, PyPortal,
# or MatrixPortal, you can use the default pin settings.
# Leave this DEFAULT line uncommented.
# If you are using a board with pre-defined ESP32 Pins:
esp32 = ESP32()
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
pwm1 = pwmio.PWMOut(board.A5, duty_cycle=2 ** 15, frequency=50)
my_servo1 = servo.Servo(pwm1, min_pulse = 500)
#A1 = digitalio.DigitalInOut(board.A1)
#pwm.value = False
# If you are using a Metro M7 **OR**
# if you are using CircuitPython 6.0.0 or earlier,
# on PyPortal and PyPortal Titano only, use the pin settings
# below. Comment out the DEFAULT line above and uncomment
# the line below. For CircuitPython 6.1.0, the pin names
# have changed for these boards, and the DEFAULT line
# above is correct.
# esp32 = ESP32(tx=board.TX, rx=board.RX)
# If you are using an AirLift FeatherWing or AirLift Bitsy Add-On,
# use the pin settings below. Comment out the DEFAULT line above
# and uncomment the lines below.
# If you are using an AirLift Breakout, check that these
# choices match the wiring to your microcontroller board,
# or change them as appropriate.
# esp32 = ESP32(
#     reset=board.D12,
#     gpio0=board.D10,
#     busy=board.D11,
#     chip_select=board.D13,
#     tx=board.TX,
#     rx=board.RX,
# )
# If you are using an AirLift Shield,
# use the pin settings below. Comment out the DEFAULT line above
# and uncomment the lines below.
# esp32 = ESP32(
#     reset=board.D5,
#     gpio0=board.D6,
#     busy=board.D7,
#     chip_select=board.D10,
#     tx=board.TX,
#     rx=board.RX,
# )
adapter = esp32.start_bluetooth()
ble = BLERadio(adapter)
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)
while True:
    ble.start_advertising(advertisement)
    print("waiting to connect")
    while not ble.connected:
        pass
    print("connected: trying to read input")
    while ble.connected:
        # Returns b'' if nothing was read.
        one_byte = uart.read(10)
        if one_byte:
            print(one_byte)
            print("space")
            rounds = 0
            if one_byte == b'!B219!B20:':#2
                for angle in range(90, 180, 5):  # 0 - 20 degrees, 5 degrees at a time.
                    my_servo.angle = angle
                    time.sleep(0.05)
                    rounds +=1
            if one_byte == b'!B318!B309': #3
                for angle in range(0,50, 5):
                    my_servo1.angle = angle
                    time.sleep(0.05)
            if one_byte == b'!B417!B408': #4
                for angle in range(180, 90, -5):  # 0 - 180 degrees, 5 degrees at a time.
                    my_servo.angle = angle
                    time.sleep(0.05)
            if one_byte == b'!B11:!B10;': #1
                for angle in range(50, 0, -5):  # 0 - 180 degrees, 5 degrees at a time.
                    my_servo1.angle = angle
                    time.sleep(0.05)
            uart.write(one_byte)