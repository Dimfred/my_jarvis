from jarvis.messages import *
from jarvis import config

import logging as log
import json
from collections import Counter
import operator


_mapping = {}

def load_command_action_mapping( *args ):
   global _mapping
   _mapping = {}

   cleanup = _parse_mapping_file()

   if cleanup:
      _remove_multiple_commands()


def get_action_and_args( app_msg ):

   json_msg = json.loads( app_msg )

   log.info( f"Received:\n{json.dumps(json_msg,indent=2)}" )

   if _is_train_message( json_msg ):

      train_msg = TrainActionMessage( json_msg )
      return ( json_msg["method"], train_msg )

   elif _is_command_message( json_msg ):

      command_msg = CommandMessage( json_msg )

      #action = _perform_action_decision( command_msg )
      action = _get_valid_action( command_msg )

      name, args = _split_in_name_and_args( action )
      return name, args

   raise ValueError( "Unknown message method name." )


def _parse_mapping_file():
   cleanup = False

   with open( config.COMMAND_ACTION_MAPPING_FILE, "r" ) as file:
         lines = list(file)

         cleanup = False
         for line in lines:
            line = _remove_cr( line )

            command, action = line.split("#")
            if command not in _mapping:
               _mapping[command] = action
            else:
               cleanup = True

   return cleanup


def _is_train_message( json_msg ):
   return json_msg["method"] == "train_action"


def _is_command_message( json_msg ):
   return json_msg["method"] == "command"


def _get_valid_action( command_msg ):
   for command in command_msg.commands:
      if command in _mapping:
         return _mapping[command]

   raise ValueError( "No valid action found." )


def _perform_action_decision( command_msg ):
   possible_actions = []
   for command in command_msg.commands:
      possible_actions.append( _get_action_from_mapping(command) )

   return _get_most_frequent_action( possible_actions )


def _get_action_from_mapping( command ):
   if command in _mapping:
      return _mapping[command]
   return None


def _get_most_frequent_action( possible_actions ):
   count = Counter( possible_actions )
   return max( count.items(), key=operator.itemgetter(1) )[0]


def _split_in_name_and_args( action ):
   split = action.split(" ")
   return split.pop(0), split


def _remove_multiple_commands():
   with open( config.COMMAND_ACTION_MAPPING_FILE, "w" ) as file:
         for command, action in _mapping.items():
            file.write( f"{command}#{action}\n" )


def _remove_cr( line ):
   return line[:-1]