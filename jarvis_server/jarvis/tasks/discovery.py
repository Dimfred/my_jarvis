import threading
import socket
import logging as log



_DISCOVERY_ADDR = ( "0.0.0.0", 55555 )
_DISCOVERY_MSG = "WHO DIS"
_DISCOVERY_RESPONSE = "IT'S PI"


def start():
   threading.Thread(
      name="dicovery_task",
      target=_task
      ).start()


def _task():
   sock = _init_socket()
   while True:
      msg, addr = sock.recvfrom( 256 )
      msg = msg.decode()

      if _is_dicovery( msg ):
         log.info( f"Pi successfully discovered by: {addr}" )
         sock.sendto( bytes(_DISCOVERY_RESPONSE, "utf-8"), addr )


def _init_socket():
   sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
   sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
   sock.bind( _DISCOVERY_ADDR )
   return sock


def _is_dicovery( msg ):
   return _DISCOVERY_MSG == msg.replace( "\n", "" )
