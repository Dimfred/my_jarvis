from apis import magichome
from jarvis import helper

import functools
import logging as log



bulb = None
bulb_addr = None
def action( args ):
   global bulb

   if bulb == None:
      bulb = _discover()

   try:
      if args[0] in _light_actions:
         key = args[0]
         _light_actions[key]( args )
         log.info( f"Magichome light with: {key} {args}." )
   except Exception as e:
      log.info( f"Magichome actions exception: {e}" )
      bulb = None


#######################
###   light state   ###
#######################

_light_states = {
   "on": True,
   "off": False,
   "default": True,
}

def _light_set_state( args ):

   new_state = _light_states[ "default" ]
   if args[0] in _light_states:
      new_state = _light_states[ args[0] ]

   #bulb.on = new_state
   magichome.Light(bulb_addr).on = new_state


#########################
###   light colours   ###
#########################

_light_colours = {
   "red": (230, 1, 1),
   "green": (1, 230, 1),
   "blue": (1, 1, 230),
   "warm": (254, 197, 41),
   "default": (254, 197, 41),
}

def _light_set_colour( args ):
   args.pop(0)
   log.info( f"Args: {args}")

   colour = _light_colours[ "default" ]
   if args and args[0] in _light_colours:
      colour = _light_colours[ args[0] ]

   bulb.rgb = colour
   log.info( f"Bulb set colour: {colour} = {_light_colours[colour]}" )


############################
###   light brightness   ###
############################

_brightness_bindings = {
   1: 30,
   100: 30,
   2: 55,
   3: 80,
   4: 105,
   5: 130,
   6: 155,
   7: 180,
   8: 205,
   9: 230,
   10: 255
}

def _light_set_brightness( args ):
   args.pop(0)
   bulb.brightness = _get_brightness_lvl( args )


def _get_brightness_lvl( args ):
   # default
   lvl = 10

   if args:
      if helper.is_int( args[0] ) and int( args[0] ) in _brightness_bindings:
         lvl = int( args[0] )
      else:
         conv = helper.word_to_num( args[0] )
         if conv is not None and conv in _brightness_bindings:
            lvl = conv

   return _brightness_bindings[ lvl ]


#######################
###   light modes   ###
#######################

_mode_bindings = {
   "red": magichome.RED_GRADUALLY,
   "normal": magichome.NORMAL,
   "crossfade": magichome.RAINBOW_CROSSFADE,
   "default": magichome.NORMAL,
}


def _light_set_mode( args ):
   args.pop(0)

   mode = "default"
   if args[0] in _mode_bindings:
      mode = args[0]

   bulb.mode = _mode_bindings[ mode ]


#############################
###   all light actions   ###
#############################

_light_actions = {
   "on": _light_set_state,
   "off": _light_set_state,
   "colour": _light_set_colour,
   "brightness": _light_set_brightness,
   "mode": _light_set_mode,
}


###################
###   helpers   ###
###################

def _discover():
   global bulb_addr
   addrs = magichome.Discovery("192.168.4.255").discover()
   if addrs:
      log.info( f"Bulb discovered {addrs[0]}." )
      bulb_addr = addrs[0]
      return magichome.Light( addrs[0] )
   else:
      log.info( "Bulb could not be discovered." )
      return None


