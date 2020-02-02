from tasks.actions import actions

import threading
import logging as log


__queue_has_elem_condition = threading.Condition()
__queue_lock = threading.Lock()
__queue = []

def start():

   threading.Thread(
      name="action_performer_task",
      target=__task,
      args=(__queue_has_elem_condition,)
      ).start()


def push_queue( app_msg ):

   with __queue_lock:
      __queue.append( app_msg )

   with __queue_has_elem_condition:
      __queue_has_elem_condition.notify()


def __task( cv ):

   while True:

      with cv:
         cv.wait()

         with __queue_lock:
            app_msg = __queue.pop(0)
            __perform_action( app_msg )


def __perform_action( app_msg ):

   actions_and_args = __get_all_actions_and_args( app_msg )
   for name, args in actions_and_args:
      if name in actions and args:
         actions[ name ]( args )
         log.info( "Performed: {} with {}".format( name, args ) )

   log.info( "No suitable action could be found." )


def __get_all_actions_and_args( app_msg ):
   raw_actions = __split_into_raw_actions( app_msg )

   actions_and_args = []
   for raw_action in raw_actions:

      # TODO
      if "and" in raw_action and "spotify" not in raw_action:

         multi_raw_actions = raw_action.split( "and" )

         for multi_raw_action in multi_raw_actions:
            multi_raw_action = __remove_space_from_begin( multi_raw_action )
            name, args = __get_action_and_args( multi_raw_action )
            actions_and_args.append( (name, args) )

      else:
         name, args = __get_action_and_args( raw_action )
         actions_and_args.append( (name, args) )

   return actions_and_args



def __remove_space_from_begin( string ):
   if len(string) != 0:
      if string[0] == " ":
         return string[1:]

   return string

def __split_into_raw_actions( app_msg ):
   return app_msg.split("\n")


def __get_action_and_args( command ):
   args = command.split(" ")
   command_name = args.pop(0)
   return command_name, args






