from adafruit_pca9685 import PCA9685
import config

class Pca9685:
  
  def __init__(self, i2c):
    self.pca9685 = PCA9685(i2c_bus=i2c, address=config.pins.I2C_ADDRESS_PCA9685)
    