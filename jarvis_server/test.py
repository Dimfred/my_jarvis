import socket


#####################
###  Samsung API  ###
#####################

import samsungctl

# # 78:ab:bb:97:3c:1c

config = {
   "name": "pi",
   "description": "pi",
   "id": "dc:a6:32:44:37:49",
   "host": "192.168.0.217",
   "port": 55000,
   "method": "legacy",
   "timeout": 0
}

# with samsungctl.Remote(config) as remote:
#    while True:
#       state = input("promt")
#       if state == "on":
#          remote.control("KEY_POWERON")
#       elif state == "off":
#          remote.control("KEY_POWEROFF")
#       elif state == "menu":
#          remote.control("KEY_MENU")
#       else:
#          remote.control(state)

####################
###   HDMI-CEC   ###
####################


import cec

# adapters = cec.list_adapters()
# print( adapters )

cec.init( "RPI" )
print( "inited")
tv = cec.Device( cec.CECDEVICE_TV)
print( "device added" )

while True:
   if input("promt: ") == "on":
      tv.power_on()
   else:
      with samsungctl.Remote(config) as remote:
         remote.control("KEY_POWEROFF")
