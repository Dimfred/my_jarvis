package de.dimfred.jarvis.core.messages

import com.google.gson.Gson
import com.google.gson.annotations.SerializedName

class TrainActionMessage: AppMessage
{
    override val method = "train_action"

    @SerializedName( value = "action_to_train")
    val actionToTrain: String

    @SerializedName( value = "speech_results" )
    val speechResults: ArrayList<String>

    constructor( actionToTrain: String, speechResults: ArrayList<String> )
    {
        this.actionToTrain = actionToTrain
        this.speechResults = speechResults
    }

    override fun serialize(): String
    {
        return Gson().toJson(this, TrainActionMessage::class.java )
    }
}