package de.dimfred.jarvis_no_service.command

class Decoder
{
    fun decode( commands: ArrayList<String> ): String?
    {
        for( validCommand in validCommands )
        {
            for( command in commands )
            {
                val lowerCommand = command.toLowerCase()
                if( lowerCommand == validCommand )
                    return lowerCommand
            }
        }

        return null
    }
  
    companion object
    {
        private val validCommands: ArrayList<String> = arrayListOf(
            "table on",
            "table off",
            "laptop on",
            "laptop off"
            )
    }
}