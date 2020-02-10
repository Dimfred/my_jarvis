from magichue import *

import socket

class Status(magichue.Status):
   pass


class Light(magichue.Light):

   def _connect(self):
      self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self._sock.settimeout(1)
      self._sock.connect((self.addr, self.port))


class Discovery(object):

   DISCOVERY_PORT = 48899
   DISCOVERY_MSG = b"HF-A11ASSISTHREAD"


   def __init__(self, broadcast_addr="255.255.255.255", timeout=1):
      self._broadcast_addr = (broadcast_addr, Discovery.DISCOVERY_PORT)
      self._timeout = timeout
      self._socket = self._make_socket()


   def discover(self):

      self._send_discovery_msg()

      discovered_addrs = self._recv_all_discovered_addrs()


      self._socket.close()

      return discovered_addrs


   def _make_socket(self):
      sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
      sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
      sock.setsockopt( socket.SOL_SOCKET, socket.SO_BROADCAST, 1 )
      sock.settimeout( self._timeout )
      sock.bind( ("0.0.0.0", Discovery.DISCOVERY_PORT) )
      return sock


   def _send_discovery_msg(self):
      self._socket.sendto(Discovery.DISCOVERY_MSG, self._broadcast_addr)


   def _recv_all_discovered_addrs(self):

      discovered_addrs = []

      try:
         # while True:
         for i in range(2):
            response, addr = self._socket.recvfrom(64)
            if response != Discovery.DISCOVERY_MSG:
               addr = response.decode().split(",")[0]
               discovered_addrs.append(addr)
      except socket.timeout:
         pass

      return discovered_addrs
