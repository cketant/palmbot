from config.pins import I2C_ADDRESS_VL53L0X

from adafruit_vl53l0x import VL53L0X

class Vl53l0X():
  
  def __init__(self, i2c):
    self.vl53l0x = VL53L0X(i2c=i2c, address=I2C_ADDRESS_VL53L0X)
    
  @property
  def distance(self):
    return self.vl53l0x.distance