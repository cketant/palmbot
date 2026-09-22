from gpiozero import Motor, Robot, DigitalOutputDevice
from config.pins import MOTOR_LEFT, MOTOR_RIGHT, ENCODER_LEFT, ENCODER_RIGHT, MOTOR_STANDBY

class Drv8833():
  """ H-Bridge representing the wheels and encoders """
  
  def __init__(self):
    self.standby = DigitalOutputDevice(MOTOR_STANDBY, active_high=True)
    self.robot = Robot(left=Motor(*MOTOR_LEFT), right=Motor(*MOTOR_RIGHT))
    
  def is_on(self, is_on):
    """ Turn the H-Bridge on/off """
    if is_on:
      self.standby.on()
    else:
      self.standby.off()
      
  def forward(self, speed):
    self.robot.forward(speed)
    
  def reverse(self):
    self.robot.reverse()
    
  def stop(self):
    self.robot.stop()
    
  def left(self, speed):
    self.robot.left(speed)
    
  def right(self, speed):
    self.robot.right(speed)