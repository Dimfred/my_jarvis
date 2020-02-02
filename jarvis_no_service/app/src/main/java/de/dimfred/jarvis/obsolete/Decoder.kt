package de.dimfred.jarvis.obsolete

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
        // TODO make hashset or move entirely into pi
        private val validCommands: ArrayList<String> = arrayListOf(
            "table on",
            "table off",
            "make it romantic",
            "laptop on",
            "laptop off",
            "light on",
            "light off"
            )
    }
}