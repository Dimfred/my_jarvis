from . import action_executer
from . import app_msg_recv
from . import discovery

def start():
   discovery.start()
   action_executer.start()
   app_msg_recv.start( action_executer.push_queue )

