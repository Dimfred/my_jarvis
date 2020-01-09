import RPi.GPIO as GPIO

class PINS:

   class TABLE:
      OFF = 26
      ON  = 26

   class LAPTOP:
      OFF = 0
      ON  = 0

   @staticmethod
   def init():

      # refers by GPIO* not 1-N
      GPIO.setmode( GPIO.BCM )
      GPIO.setup( PINS.TABLE.ON, GPIO.OUT )
      GPIO.setup( PINS.TABLE.OFF, GPIO.OUT )