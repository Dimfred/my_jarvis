from setup import pins
from utilities.utilities import print_func_deco
from hardware.hardware import remote_sockets

import functools
import time


command_to_action = {
   "table on": functools.partial( remote_sockets.send, 1, "on" ),
   "table off": functools.partial( remote_sockets.send, 1, "off" ),
   "laptop on": functools.partial( remote_sockets.send, 2, "on" ),
   "laptop off": functools.partial( remote_sockets.send, 2, "off" ),
   "light on": functools.partial( remote_sockets.send, 3, "on" ),
   "light off": functools.partial( remote_sockets.send, 3, "off" ),
   }
