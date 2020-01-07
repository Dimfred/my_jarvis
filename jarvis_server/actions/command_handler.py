import threading

from actions import actions
from utilities.func_wrapper import func_wrapper

class command_handler:

   __command_to_action = {
      "table on": func_wrapper( actions.table, "on" ),
      "table off": func_wrapper( actions.table, "off" ),
      "laptop on": func_wrapper( actions.laptop, "on" ),
      "laptop off": func_wrapper( actions.laptop, "off" ),
      }


   def __init__( self ):

      # notify for our task
      self.__notify = threading.Condition()

      # worker thread
      self.__thread = threading.Thread(
         name="command_handler", target=self.__command_task, args=(self.__notify,)
         )
      self.__thread.start()

      self.__queue_lock = threading.Lock()
      self.__queue = []


   def __command_task( self, cv ):

      while True:

         with cv:
            print( "Waiting for work" )
            cv.wait()

            command = ""
            with self.__queue_lock:
               command = self.__queue.pop(0)

            try:
               command_handler.__command_to_action[ command ].exe()
            except KeyError:
               pass


   def push_queue( self, command ):

      with self.__queue_lock:
         self.__queue.append( command )

      with self.__notify:
         self.__notify.notify()
