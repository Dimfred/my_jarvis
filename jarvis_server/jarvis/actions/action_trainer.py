from jarvis import config


def add_action( train_action_msg ):
   with open( config.COMMAND_ACTION_MAPPING_FILE, "a" ) as mapping:
      for speech_result in train_action_msg.speech_results:
         mapping.write( f"{speech_result}#{train_action_msg.action_to_train}\n" )

      mapping.close()