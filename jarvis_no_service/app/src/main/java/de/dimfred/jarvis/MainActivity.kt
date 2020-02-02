package de.dimfred.jarvis

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log

import de.dimfred.jarvis.core.AppMessageSender
import de.dimfred.jarvis.core.PiDiscoverer
import de.dimfred.jarvis.core.JarvisRecognizer

// implements the layout with ids
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    private lateinit var jarvisRecognizer: JarvisRecognizer

    private var piAddr: String? = null
    private var appPort = 1337

    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        jarvisRecognizer = JarvisRecognizer( this )
        jarvisRecognizer.registerResultCallback { result -> onSpeechResult( result) }

        voiceBtn.setOnClickListener{ jarvisRecognizer.listen() }

    }

    override fun onResume() {
        super.onResume()

        jarvisRecognizer.listen()
    }
    
    private fun onSpeechResult(speechResult: ArrayList<String>? )
    {
        if( speechResult == null )
            return

        var appMsg = buildAppMsg( speechResult )

        resultTv.text = appMsg

        piAddr = discoverPi()
        if( piAddr == null ) {
            var failedMsg= "PI could not be discovered."
            //resultTv.text += failedMsg
            Log.i( TAG, failedMsg )
            return
        }



        // var success = sendToPi( appMsg )
        sendToPi( appMsg )
    }

    private fun discoverPi(): String?
    {
        var discoverer = PiDiscoverer().also {
            it.execute("")
        }

        return discoverer.get()
    }

    private fun sendToPi(appMsg: String ): Boolean
    {
        var appMsgSender = AppMessageSender(
            piAddr!!,
            appPort
        ).also {
            it.execute( appMsg )
        }

        return appMsgSender.get()
    }

    private fun buildAppMsg( speechResult: ArrayList<String> ): String
    {
        var appMsg = ""
        for( part in speechResult ) {
            appMsg += part.toLowerCase() + "\n"
        }

        return appMsg
    }

    companion object
    {
        private var TAG = MainActivity::class.java.name
    }
}
