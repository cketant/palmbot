'''
Single source of truth for the Palmbot wiring map.

Pure data, no hardware imports -- this module is importable on any machine,
so fakes and tests can reason about the wiring without a Pi attached.
All numbers are BCM GPIO, matching gpiozero's default numbering.

########################################################

  # Pi 5 #        # JPT #        # DRV8833 #        # MAX98357A/I2S #      # LED RING #      # I2C #

# --------------------------------------------------------------------------------------------------------------------------------

######## WHEEL 1, MOTOR B

# ENCODERS
  # GPIO 17        yellow
  # GPIO 27        white
  # GPIO 5                           BIN1
  # GPIO 6                           BIN2


######## WHEEL 2, MOTOR A

# ENCODERS
  # GPIO 25        white
  # GPIO 24        yellow
  # GPIO 16                          AIN1
  # GPIO 12                          AIN2

######## GENERAL

  # GPIO 23                          STBY

# --------------------------------------------------------------------------------------------------------------------------------

  # GPIO 18                                               BCLK
  # GPIO 19                                               LRCLK
  # GPIO 20                                               DIN

# --------------------------------------------------------------------------------------------------------------------------------

  # GPIO 10                                                                SPI MOSI

# --------------------------------------------------------------------------------------------------------------------------------

  # GPIO 2                                                                                    SDA
  # GPIO 3                                                                                    SCL

# --------------------------------------------------------------------------------------------------------------------------------

########################################################
'''

from typing import NamedTuple


class MotorPins(NamedTuple):
  '''One DRV8833 channel: two direction/PWM inputs.'''
  in1: int
  in2: int


class EncoderPins(NamedTuple):
  '''Quadrature encoder channel pair, named by JPT wire colour.'''
  a: int  # yellow
  b: int  # white


# ---------------------------------------------------------------- drivetrain

# DRV8833 channel B -> wheel 1 (left)
MOTOR_LEFT = MotorPins(in1=5, in2=6)
ENCODER_LEFT = EncoderPins(a=17, b=27)

# DRV8833 channel A -> wheel 2 (right)
MOTOR_RIGHT = MotorPins(in1=16, in2=12)
ENCODER_RIGHT = EncoderPins(a=24, b=25)

# Held high to enable both DRV8833 channels; low coasts the H-bridges.
MOTOR_STANDBY = 23

# ------------------------------------------------------------------ i2s audio

# MAX98357A. Driven by the kernel I2S peripheral via device tree overlay,
# not by userspace -- listed so the map stays complete and so nothing else
# claims these lines.
I2S_BCLK = 18
I2S_LRCLK = 19
I2S_DIN = 20

# ----------------------------------------------------------------- led ring

# On a Pi 5 NeoPixels are clocked out over SPI MOSI, so the ring data line
# must be GPIO 10. See hal/buses.py.
LED_RING_DATA = 10
NUM_PIXELS = 12 # number of pixels on the LED Ring
RED    = 0xFF0000
YELLOW = 0xFFFF00
GREEN  = 0x00FF00
BLUE = 0x0000FF



# ----------------------------------------------------------------- i2c bus

# Shared by VL53L0X, MPU6050 and PCA9685. board.I2C() picks these up itself;
# recorded here so the map is complete.
I2C_SDA = 2
I2C_SCL = 3

# Default 7-bit addresses of the devices on that bus. Compare against
# Buses.scan_i2c() to diagnose a missing peripheral.
I2C_ADDRESS_VL53L0X = 0x29
I2C_ADDRESS_MPU6050 = 0x68
I2C_ADDRESS_PCA9685 = 0x40


# Every GPIO this project drives, grouped by owner. Used by the collision
# check below and useful for diagnostics.
CLAIMED = {
  'motor_left': list(MOTOR_LEFT),
  'motor_right': list(MOTOR_RIGHT),
  'encoder_left': list(ENCODER_LEFT),
  'encoder_right': list(ENCODER_RIGHT),
  'motor_standby': [MOTOR_STANDBY],
  'i2s': [I2S_BCLK, I2S_LRCLK, I2S_DIN],
  'led_ring': [LED_RING_DATA],
  'i2c': [I2C_SDA, I2C_SCL],
}


def find_conflicts() -> dict[int, list[str]]:
  '''Return any GPIO claimed by more than one subsystem, pin -> owners.'''
  owners: dict[int, list[str]] = {}
  for name, pins in CLAIMED.items():
    for pin in pins:
      owners.setdefault(pin, []).append(name)
  return {pin: names for pin, names in owners.items() if len(names) > 1}


def assert_no_conflicts() -> None:
  '''Raise if two subsystems claim the same GPIO.

  Cheap to call at startup: a double-claimed pin shows up here as an
  exception instead of as a peripheral that mysteriously does not respond.
  '''
  conflicts = find_conflicts()
  if conflicts:
    detail = '; '.join(
      f'GPIO {pin}: {", ".join(names)}' for pin, names in sorted(conflicts.items())
    )
    raise ValueError(f'pin map conflict -- {detail}')
