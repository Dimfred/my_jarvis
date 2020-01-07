package de.dimfred.jarvis_no_service.speech_recognition

import android.os.Bundle
import android.speech.RecognitionListener
import android.speech.SpeechRecognizer
import android.util.Log

class JarvisListener : RecognitionListener
{
    private var resultCb: ((res: ArrayList<String>?) -> Unit)? = null

    fun registerResultCallback( cb: (result: ArrayList<String>?) -> Unit )
    {
        resultCb = cb
    }

    override fun onResults(results: Bundle)
    {
        Log.i(TAG, "onResults")
        var matches = results.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION)

        //var text = ""
        //for (result in matches!!)
        //    text += result + "\n"

        if( resultCb != null )
            resultCb!!( matches )
    }

    override fun onError(error: Int)
    {
        Log.e( TAG, "Error: $error" )
    }

    override fun onEndOfSpeech()
    {

    }

    override fun onBeginningOfSpeech()
    {

    }

    override fun onEvent(eventType: Int, params: Bundle?)
    {

    }

    override fun onPartialResults(partialResults: Bundle?)
    {

    }

    override fun onBufferReceived(buffer: ByteArray?)
    {

    }

    override fun onRmsChanged(rmsdB: Float)
    {

    }

    override fun onReadyForSpeech(params: Bundle?)
    {

    }

    companion object
    {
        val TAG = RecognitionListener::class.java.name
    }
}