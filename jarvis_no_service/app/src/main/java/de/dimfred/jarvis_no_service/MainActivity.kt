package de.dimfred.jarvis_no_service

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import de.dimfred.jarvis_no_service.command.DoAsync

import de.dimfred.jarvis_no_service.command.Sender
import de.dimfred.jarvis_no_service.command.Decoder
import de.dimfred.jarvis_no_service.speech_recognition.JarvisRecognizer

// implements the layout with ids
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    private lateinit var jarvisRecognizer: JarvisRecognizer
    private val decoder = Decoder()


    private var ip = "192.168.0.104"// "192.168.0.34"
    private var port = 1337

    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        jarvisRecognizer = JarvisRecognizer( this )
        jarvisRecognizer.registerResultCallback { result -> onSpeechResult( result) }

        voiceBtn.setOnClickListener{ jarvisRecognizer.listen() }
    }
    
    private fun onSpeechResult( result: ArrayList<String>? )
    {
        if( result == null )
            return

        var text: String = ""
        for( part in result )
            text += part + "\n"

        resultTv.text = text

        var command: String? = decoder.decode( result ) ?: return

        var sender = Sender(ip, port).also {
            it.execute( command )
        }
    }
}
