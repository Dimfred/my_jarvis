from jarvis import config
from apis import rfsockets

import cec
import samsungctl

import logging as log
import time
import threading


def action( args ):
   if args and args[0] in _tv_actions:
      action = args[0]

      _tv_actions[ action ]( args )


def _tv_on( args ):
   _tv_socket_on()
   _tv_cec_on()
   log.info( "TV turned on." )


def _tv_off( args ):
   try:
      _tv_remote_action( "off" )
      _tv_socket_off()
      log.info( "TV turned off." )
   except Exception as e:
      log.error( f"TV off: {e}" )


_tv_actions = {
   "on": _tv_on,
   "off": _tv_off
}

_remote_key_codes = {
   "off": "KEY_POWEROFF",
}

def _tv_remote_action( arg ):
   if arg in _remote_key_codes:
      key_code = _remote_key_codes[arg]

      with samsungctl.Remote( config.SAMSUNG ) as remote:
         remote.control( key_code )
   else:
      log.e( f"TV: parameter does not exist: {arg}" )


def _tv_socket_on():
   def __turn_on():
      rfsockets.send( config.TV_SOCKET, "on" )
      time.sleep(3)

   threading.Thread(
      name="tv_on_task",
      target=__turn_on
      ).start()


def _tv_socket_off():
   def __turn_off():
      time.sleep(15)
      rfsockets.send( config.TV_SOCKET, "off" )

   threading.Thread(
      name="tv_off_task",
      target=__turn_off
      ).start()


def _tv_cec_on():
   tv = _init_cec()
   tv.power_on()


def _init_cec():
   cec.init( config.CEC_DEVICE_NAME )
   return cec.Device( cec.CECDEVICE_TV )

