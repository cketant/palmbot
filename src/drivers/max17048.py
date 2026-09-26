from adafruit_max1704x import MAX17048
from config.pins import I2C_ADDRESS_MAX17048

class Max17048():
  
  def __init__(self, i2c):
    self.max17048 = MAX17048(i2c, address=I2C_ADDRESS_MAX17048)
    
  @property
  def curr_charge_percentage(self) -> float:
    return self.max17048.cell_percent
  
  @property
  def charge_rate(self) -> float:
    return self.max17048.charge_rate
    
  