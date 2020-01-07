#!/usr/bin/python3

import socket
from actions import actions
from actions.command_handler import command_handler


def init_socket():

   addr = ( "0.0.0.0", 1337 )
   sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
   sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
   try:
      sock.bind( addr )
   except Exception as e:
      print( e )

   sock.listen(1)
   return sock




if __name__ == "__main__":

   actions.PINS.INIT()

   sock = init_socket()

   command_handler = command_handler()

   while True:

      client, client_addr = sock.accept()

      # allow only local connections
      if not client_addr[0].startswith( "192.168." ):
         client.close()
         continue

      command = client.recv( 32 ).decode()
      client.close()

      command_handler.push_queue( command )


