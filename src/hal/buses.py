import board
import busio


class Buses:
  '''Owns the shared I2C bus so drivers never create their own.

  SPI is deliberately absent: on a Pi 5 the LED ring driver opens GPIO 10
  (MOSI) itself, so nothing else may hold that bus.
  '''

  def __init__(self):
    self.i2c = None

  def start(self):
    self.i2c = busio.I2C(board.SCL, board.SDA)
    return self

  def scan(self):
    while not self.i2c.try_lock():
      pass
    try:
      return self.i2c.scan()
    finally:
      self.i2c.unlock()

  def stop(self):
    if self.i2c:
      self.i2c.deinit()
      self.i2c = None
