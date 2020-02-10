from rpi_rf import RFDevice


_pin = 17

_codes = {
   # switch number, on, off (decimal number derived from tristate code)
   1: { "off": 1364, "on": 1361 },
   2: { "off": 4436, "on": 4433 },
   3: { "off": 5204, "on": 5201 }
}

def send( rfsocket_num, sig ):

   rfd = RFDevice( _pin )
   rfd.enable_tx()
   rfd.tx_repeat = 10

   if rfsocket_num in _codes:
      rfsocket_codes = _codes[ rfsocket_num ]
      if sig in rfsocket_codes:
         rfd.tx_code( rfsocket_codes[ sig ] )

   rfd.cleanup()