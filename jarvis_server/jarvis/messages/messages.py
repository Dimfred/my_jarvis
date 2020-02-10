

class CommandMessage:
   def __init__(self, json):
      self.commands = json["commands"]


class TrainActionMessage:
   def __init__(self, json):
      self.action_to_train = json["action_to_train"]
      self.speech_results = json["speech_results"]
