package de.dimfred.jarvis_no_service.speech_recognition


import android.Manifest
import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.speech.SpeechRecognizer
import android.speech.RecognizerIntent
import androidx.core.app.ActivityCompat



class JarvisRecognizer
{
    private var speechRecognizer: SpeechRecognizer
    private var recognizerIntent: Intent
    private var jarvisListener: JarvisListener

    constructor( ctx: AppCompatActivity )
    {
        jarvisListener = JarvisListener()

        speechRecognizer = initRecognizer( ctx, jarvisListener )
        recognizerIntent = initIntent()

        requestPermissions( ctx )
    }

    fun listen()
    {
        speechRecognizer.startListening( recognizerIntent )
    }

    fun registerResultCallback( cb: (result: ArrayList<String>?) -> Unit )
    {
        jarvisListener.registerResultCallback( cb )
    }

    private fun initRecognizer( ctx: Activity, listener: JarvisListener ): SpeechRecognizer
    {
        var recog = SpeechRecognizer.createSpeechRecognizer( ctx )
        recog.setRecognitionListener( listener )
        return recog
    }

    private fun initIntent(): Intent
    {
        var intent = Intent( RecognizerIntent.ACTION_RECOGNIZE_SPEECH )

        intent.putExtra( RecognizerIntent.EXTRA_LANGUAGE_PREFERENCE, "en" )
        intent.putExtra( RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM )
        intent .putExtra( RecognizerIntent.EXTRA_MAX_RESULTS, 3 )

        return intent
    }

    private fun requestPermissions( ctx: Activity )
    {
        ActivityCompat.requestPermissions( ctx, arrayOf( Manifest.permission.RECORD_AUDIO ), REQUEST_RECORD_PERMISSION )
    }

    companion object
    {
        const val REQUEST_RECORD_PERMISSION: Int = 100
    }
}