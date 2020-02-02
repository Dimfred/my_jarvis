import threading
import socket
import logging as log



__DISCOVER_ADDR = ( "0.0.0.0", 55555 )
__DISCOVERY_MSG = "WHO DIS"
__DISCOVERY_RESPONSE = "IT'S PI"


def start():

   threading.Thread(
      name="dicovery_task",
      target=__task
      ).start()


def __task():

   sock = __init_socket()

   while True:

      msg, addr = sock.recvfrom( 256 )
      msg = msg.decode()

      if __is_dicovery( msg ):
         log.info( "Successfully discovered {}".format( addr ) )
         sock.sendto( bytes(__DISCOVERY_RESPONSE, "utf-8"), addr )


def __init_socket():

   sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
   sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
   sock.bind( __DISCOVER_ADDR )
   return sock


def __is_dicovery( msg ):
   return __DISCOVERY_MSG == msg.replace( "\n", "" )
