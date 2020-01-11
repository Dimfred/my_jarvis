#!/usr/bin/python3

import socket

from actions.command_handler import command_handler


def init_socket():

   try:

      addr = ( "0.0.0.0", 1337 )
      sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
      sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
      sock.bind( addr )
      sock.listen(1)
      return sock

   except Exception as e:
      print( e )




if __name__ == "__main__":

   sock = init_socket()

   command_handler = command_handler()

   while True:

      client, client_addr = sock.accept()

      # allow only local connections
      if not client_addr[0].startswith( "192.168." ):
         client.close()
         continue

      msg = client.recv( 128 ).decode()
      client.close()

      # TODO maybe split msg here
      command_handler.push_queue( msg )


