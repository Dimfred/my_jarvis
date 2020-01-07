import RPi.GPIO as GPIO
import time

class PINS:

   class TABLE:
      OFF = 26
      ON  = 26

   class LAPTOP:
      OFF = 0
      ON  = 0

   @staticmethod
   def INIT():

      # refers by GPIO* not 1-N
      GPIO.setmode( GPIO.BCM )
      GPIO.setup( PINS.TABLE.ON, GPIO.OUT )
      GPIO.setup( PINS.TABLE.OFF, GPIO.OUT )



def table( param ):
   # TODO move to config
   sleep_time = 0.3

   if param == "on":

      for i in range(4):

         GPIO.output( PINS.TABLE.ON, 1 )
         time.sleep( sleep_time )
         GPIO.output( PINS.TABLE.ON, 0 )
         time.sleep( sleep_time )


   elif param == "off":

      print( "table off" )

      for i in range(4):

         GPIO.output( PINS.TABLE.OFF, 1 )
         time.sleep( sleep_time )
         GPIO.output( PINS.TABLE.OFF, 0 )
         time.sleep( sleep_time )


def laptop( param ):
   pass

