import socket
import logging as log
import threading


_APP_ADDR = ( "0.0.0.0", 1337 )

# msg_cb = callback function what should happen with the message
def start( msg_cb ):

   threading.Thread(
      name="app_msg_recv_task",
      target=_task,
      args=( msg_cb, )
      ).start()


def _task( msg_cb ):

   sock = _init_socket()

   while True:
      client, client_addr = sock.accept()
      msg = client.recv( 256 ).decode()
      # TODO maybe response?
      client.close()

      msg_cb( msg )


def _init_socket():

   sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
   sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
   sock.bind( _APP_ADDR )
   sock.listen(1)
   return sock