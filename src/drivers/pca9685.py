from adafruit_pca9685 import PCA9685
from adafruit_motor.servo import Servo
from config.pins import I2C_ADDRESS_PCA9685

# Arducam B0283 pan-tilt. Channels and limits from ArduCAM/PCA9685
# (example/rpi/PCA9685.h); its servos want a 500-2500us pulse, not the
# adafruit_motor default of 750-2250.
TILT_CHANNEL = 0
PAN_CHANNEL = 1
TILT_RANGE = (15, 145)
PAN_RANGE = (0, 180)
MIN_PULSE = 500
MAX_PULSE = 2500


class Pca9685():

  def __init__(self, i2c):
    self.pca9685 = PCA9685(i2c_bus=i2c, address=I2C_ADDRESS_PCA9685)
    # Must be set: the frequency setter is what turns on MODE1 auto-increment,
    # without which every channel write silently lands in the wrong register.
    self.pca9685.frequency = 50

  def _servo(self, channel):
    return Servo(self.pca9685.channels[channel],  # type: ignore[arg-type]
                 min_pulse=MIN_PULSE, max_pulse=MAX_PULSE)
    
  def pan(self, angle=0):
    """ PAN Range is [0, 180] """
    if angle < PAN_RANGE[0] or angle > PAN_RANGE[1]:
      return
    self._servo(PAN_CHANNEL).angle = angle
  
  def tilt(self, angle=15):
    """ TILT Range is [15, 145] """
    if angle < TILT_RANGE[0] or angle > TILT_RANGE[1]:
      return
    self._servo(TILT_CHANNEL).angle = angle

  def deinit(self):
    self.pca9685.deinit()
