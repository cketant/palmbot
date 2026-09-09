import board
import adafruit_vl53l0x
import adafruit-circuitpython-pca9685
import adafruit-circuitpython-servokit


########################################################

  # Pi 5 #        # JPT #        # DRVV8833 #        # MAX98357A #      # LED RING #
  
# ----------------------------------------------------------------------------------------  

######## WHEEL 1, MOTOR B

# ENCODERS
  # GPIO 17        yellow                 
  # GPIO 27        white
  # GPIO 5                           BIN1
  # GPIO 6                           BIN2                                                      


######## WHEEL 2, MOTOR A

# ENCODERS
  # GPIO 25        white
  # GPIO 24       yellow
  # GPIO 16                          AIN1
  # GPIO 12                          AIN2

######## GENERAL

  # GPIO 23                          STBY
  
# ----------------------------------------------------------------------------------------

  # GPIO 13                                               BCLK
  # GPIO 19                                               LRCLK
  # GPIO 26                                               DIN
  
  
# ----------------------------------------------------------------------------------------  

  # SPIMOSI                                                                     *
  
########################################################