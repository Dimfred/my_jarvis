from rpi_rf import RFDevice

class remote_sockets:

   __pin = 17

   __remote_codes = {
      # switch number, on, off (decimal number derived from tristate code)
      1: { "off": 1364, "on": 1361 },
      2: { "off": 4436, "on": 4433 },
      3: { "off": 5204, "on": 5201 }
   }

   @staticmethod
   def send( num, sig ):

      rfd = RFDevice( remote_sockets.__pin )
      rfd.enable_tx()
      rfd.tx_repeat = 10
      rfd.tx_code( remote_sockets.__remote_codes[num][sig] )
      rfd.cleanup()


