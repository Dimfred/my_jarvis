import threading

class command_handler:

   def __init__( self, command_to_action ):

      # passing the actions to perform on received keywords
      self.__command_to_action = command_to_action

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
               self.__command_to_action[ command ].exe()
            except KeyError:
               pass


   def push_queue( self, command ):

      with self.__queue_lock:
         self.__queue.append( command )

      with self.__notify:
         self.__notify.notify()
