from jarvis.actions import actions
from jarvis.actions import command_interpreter

import threading
import logging as log


_queue_has_elem_cv = threading.Condition()
_queue_lock = threading.Lock()
_queue = []

command_interpreter.load_command_action_mapping()

def start():

   threading.Thread(
      name="action_performer_task",
      target=_task,
      args=(_queue_has_elem_cv,)
      ).start()


def push_queue( app_msg ):

   with _queue_lock:
      _queue.append( app_msg )

   with _queue_has_elem_cv:
      _queue_has_elem_cv.notify()


def _task( cv ):
   # TEST
   while True:

      if not _queue:
         with cv:
            cv.wait()

      app_msg = ""
      with _queue_lock:
         app_msg = _queue.pop(0)

      try:

         action, args = command_interpreter.get_action_and_args( app_msg )
         if action in actions.actions:
            _execute_action( action, args )

      except ValueError as e:
         log.error( f"ActionExecuter: {e}" )


def _execute_action( action, args ):
      actions.actions[ action ]( args )




