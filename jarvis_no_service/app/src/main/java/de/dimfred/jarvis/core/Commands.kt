package de.dimfred.jarvis.core

import de.dimfred.jarvis.core.messages.CommandMessage

object Commands
{
    val TV_ON = CommandMessage("tv on")
    val TV_OFF = CommandMessage("tv off")

    val PC_ON = CommandMessage("pc on")
    val PC_OFF = CommandMessage("pc off")

    val LIGHT_ON = CommandMessage("light on")
    val LIGHT_OFF = CommandMessage("light off")

    val RELOAD_MAPPING = CommandMessage( "reload_mapping" )
}