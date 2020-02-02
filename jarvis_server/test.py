



import socket


#####################
###  Samsung API  ###
#####################

import samsungctl

# 78:ab:bb:97:3c:1c

# maybe turn on over hdmi-cec

config = {
   "name": "pi",
   "description": "pi",
   "id": "dc:a6:32:44:37:49",
   "host": "169.254.19.205", # "192.168.0.217",
   "port": 55000,
   "method": "legacy",
   "timeout": 0
}

with samsungctl.Remote(config) as remote:
   while True:
      state = input("promt")
      if state == "on":
         remote.control("KEY_POWERON")
      elif state == "off":
         remote.control("KEY_POWEROFF")
      elif state == "menu":
         remote.control("KEY_MENU")
      else:
         remote.control(state)

######################
### Magic Home API ###
######################

# from devices.magichome import MagicHomeApi

#bulb = MagicHomeApi( "192.168.4.125", 0, False )

#bulb.turn_on()

# sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
# sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
# sock.setsockopt( socket.SOL_SOCKET, socket.SO_BROADCAST, 1 )
# #sock.connect(  )
# # returns host name
# print( "socket.getfqdn()\n", socket.getfqdn() )

# sock.bind( ("", 48899) )
# #sock.listen(1)



# print( "sending..." )
# sock.sendto( b"HF-A11ASSISTHREAD", ("192.168.0.255", 48899) )
# msg = sock.recv( 1024 )
# print( "msg\n", msg )
# msg = sock.recv( 1024 )
# print( "msg\n", msg )
# msg = sock.recv( 1024 )
# print( "msg\n", msg )

# sock.close()