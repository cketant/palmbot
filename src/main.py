from neopixel import NeoPixel # LED ring
from gpiozero import Robot, Motor, Pin # DRV8833
from picamera2 import Picamera2 # Camera

from time import sleep

from hal.buses import Buses
from drivers.pca9685 import Pca9685
from drivers.vl53l0x import Vl53l0X


'''
Adafruit CircuitPython libraries (Read the Docs):

adafruit_pca9685 — https://docs.circuitpython.org/projects/pca9685/en/latest/api.html
adafruit_vl53l0x — https://docs.circuitpython.org/projects/vl53l0x/en/latest/api.html
adafruit_mpu6050 — https://docs.circuitpython.org/projects/mpu6050/en/latest/api.html
neopixel — https://docs.circuitpython.org/projects/neopixel/en/latest/api.html

Blinka / CircuitPython core modules (board and busio come from Blinka on a Pi):

board — https://docs.circuitpython.org/en/latest/shared-bindings/board/index.html
busio — https://docs.circuitpython.org/en/latest/shared-bindings/busio/index.html
Blinka (platform notes for both) — https://docs.circuitpython.org/projects/blinka/en/latest/

Raspberry Pi libraries:

gpiozero — https://gpiozero.readthedocs.io/en/stable/api_output.html (full index: https://gpiozero.readthedocs.io/en/stable/)
picamera2 — https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf (source/examples: https://github.com/raspberrypi/picamera2)
'''

def main():
  print("Starting...")
  buses = Buses().start()
  
  # instantiate drivers
  # vl53l0x = Vl53l0X(buses.i2c)
  pca9685 = Pca9685(buses.i2c)
  pca9685.tilt()
  sleep(2)
  pca9685.pan()
  
  # tear down #
  pca9685.deinit()
  
  print("Stopping...")
  buses.stop()
  
main()
