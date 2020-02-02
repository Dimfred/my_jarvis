import socket
import logging as log
import threading


__APP_ADDR = ( "0.0.0.0", 1337 )

# msg_cb = callback function what should happen with the message
def start( msg_cb ):

   threading.Thread(
      name="app_msg_recv_task",
      target=__task,
      args=( msg_cb, )
      ).start()


def __task( msg_cb ):

   sock = __init_socket()

   while True:
      client, client_addr = sock.accept()
      msg = client.recv( 256 ).decode()
      # TODO maybe response?
      client.close()

      msg_cb( msg )


def __init_socket():

   sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
   sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
   sock.bind( __APP_ADDR )
   sock.listen(1)
   return sock