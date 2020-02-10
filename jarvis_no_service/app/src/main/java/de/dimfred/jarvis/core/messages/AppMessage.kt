package de.dimfred.jarvis.core.messages


abstract class AppMessage
{
    abstract val method: String
    abstract fun serialize(): String
}