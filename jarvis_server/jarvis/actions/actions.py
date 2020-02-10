from . import light
from . import tv
from . import pc
from . import action_trainer
from . import command_interpreter

actions = {
   "pc": pc.action,
   "tv": tv.action,
   "light": light.action,
   "train_action": action_trainer.add_action,
   "reload_mapping": command_interpreter.load_command_action_mapping
}


