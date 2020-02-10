package de.dimfred.jarvis.core.messages

import com.google.gson.Gson
import com.google.gson.annotations.SerializedName

class CommandMessage: AppMessage
{
    @SerializedName( value = "method" )
    override val method = "command"

    @SerializedName( value = "commands" )
    val commands: ArrayList<String>

    constructor( commands: ArrayList<String> )
    {
        this.commands = commands
    }

    constructor( command: String )
    {
        this.commands = arrayListOf( command )
    }

    override fun serialize(): String
    {
        return Gson().toJson(this, CommandMessage::class.java )
    }
}