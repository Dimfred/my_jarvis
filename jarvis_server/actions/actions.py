import functools
import time



class __actions:

   @staticmethod
   def table( param ):
      # TODO move to config
      sleep_time = 0.3

      if param == "on":

         for i in range(4):

            GPIO.output( PINS.TABLE.ON, 1 )
            #time.sleep( sleep_time )
            #GPIO.output( PINS.TABLE.ON, 0 )
            #time.sleep( sleep_time )


      elif param == "off":

         print( "table off" )

         for i in range(4):

            #GPIO.output( PINS.TABLE.OFF, 1 )
            #time.sleep( sleep_time )
            GPIO.output( PINS.TABLE.OFF, 0 )
            #time.sleep( sleep_time )


   @staticmethod
   def laptop( param ):
      pass


command_to_action = {
   "table on": functools.partial( __actions.table, "on" ),
   "table off": functools.partial( __actions.table, "off" ),
   "laptop on": functools.partial( __actions.laptop, "on" ),
   "laptop off": functools.partial( __actions.laptop, "off" ),
   }


