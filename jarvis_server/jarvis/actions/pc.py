from apis import rfsockets

import logging as log


def action( args ):
   SOCKET_NUM = 1
   new_state = args[0]
   rfsockets.send( socket_num, new_state )
   log.info( f"Socket PC set {new_state}." )

