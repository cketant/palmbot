# Gyro + Accel

from config.pins import I2C_ADDRESS_MPU6050

from adafruit_mpu6050 import MPU6050

class Mpu6050():
  """ Gyro, Acceleration, and Temperature"""
  
  def __init__(self, i2c):
    self.mpu6050 = MPU6050(i2c, address=I2C_ADDRESS_MPU6050)
    
  @property
  def x_accel(self) -> float:
    """ Acceleration in m/S^2"""
    return self.mpu6050.acceleration[0]
  
  @property
  def y_accel(self) -> float:
    """ Acceleration in  m/S^2"""
    return self.mpu6050.acceleration[1]
  
  @property
  def z_accel(self) -> float:
    """ Acceleration in m/S^2"""
    return self.mpu6050.acceleration[2]
  
  @property
  def temp(self) -> float:
    """ Return temperature in F """
    celsius = self.mpu6050.temperature
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit
  
  @property
  def x_gyro(self) -> float:
    """ Gyro in rad/s (degrees per sec)"""
    return self.mpu6050.gyro[0]
  
  @property
  def y_gyro(self) -> float:
    """ Gyro in rad/s (degrees per sec) """
    return self.mpu6050.gyro[1]
  
  @property
  def z_gyro(self) -> float:
    """ Gyro in rad/s (degrees per sec) """
    return self.mpu6050.gyro[2]
  
  def sleep(self, isSleep):
    self.mpu6050.sleep = isSleep
    
    