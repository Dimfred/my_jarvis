from apis import rfsockets

import functools

######################
### socket actions ###
######################

def __rfsocket_action( socket_num, args ):
   # just ignore all other args if present
   new_state = args[0]
   rfsockets.send( socket_num, new_state )


def __pc_action( args ):
   SOCKET_NUM = 1
   __rfsocket_action( SOCKET_NUM, args )


def __tv_action( args ):
   SOCKET_NUM = 2
   __rfsocket_action( SOCKET_NUM, args )


def __light_action( args ):
   SOCKET_NUM = 3
   __rfsocket_action( SOCKET_NUM, args )


def __all_action( args ):
   __pc_action( args )
   __tv_action( args )
   __light_action( args )


######################
###    spotify     ###
######################

# __spotify_actions = {
#    "play": __spotify_play,
#    "next": __spotify_next,
#    "again": __spotify_again,
# }

# def __spotify_action( args ):
#    pass


######################
### other actions  ###
######################


######################
###  all actions   ###
######################

actions =  {
   "pc": __pc_action,
   "tv": __tv_action,
   "light": __light_action,
   "all": __all_action,
   # "spotify": __spotify_action,
}