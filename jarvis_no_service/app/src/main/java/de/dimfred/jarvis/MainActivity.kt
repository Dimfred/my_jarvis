package de.dimfred.jarvis

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log

import de.dimfred.jarvis.core.AppMessageSender
import de.dimfred.jarvis.core.Config
import de.dimfred.jarvis.core.JarvisRecognizer
import de.dimfred.jarvis.core.messages.CommandMessage
import de.dimfred.jarvis.core.PiDiscoverer
import de.dimfred.jarvis.core.messages.TrainActionMessage
import kotlinx.android.synthetic.main.activity_main.*

// implements the layout with ids

class MainActivity : AppCompatActivity() {

    var prevMsgDelivered = false

    var piAddr: String? = null

    lateinit var jarvisRecognizer: JarvisRecognizer
    private lateinit var mvController: MVController


    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        jarvisRecognizer = JarvisRecognizer( this )
        jarvisRecognizer.setOnSpeechResultCallback { result -> onSpeechResultCommand( result) }

        mvController = MVController( this )
        mvController.initOnClickListeners()
    }

    override fun onResume()
    {
        super.onResume()

        discoverPi()

        jarvisRecognizer.listen()
    }
    
    private fun onSpeechResultCommand(speechResult: ArrayList<String>? )
    {
        if( speechResult.isNullOrEmpty() )
            return

        if( !prevMsgDelivered && !discoverPi() )
            return

        var processed = preProcessSpeechResults( speechResult!! )

        var msg = CommandMessage( processed )
        prevMsgDelivered = sendToPi( msg.serialize() )
        if( !prevMsgDelivered )
            piAddr = null
    }


    private fun onSpeechResultTraining( speechResult: ArrayList<String>? )
    {
        if( speechResult.isNullOrEmpty() )
            return

        var actionToTrain = trainingEb.text.toString()
        if( trainingEb.text.isNullOrEmpty() )
            return

        if( !prevMsgDelivered && !discoverPi() )
            return

        var processed = preProcessSpeechResults( speechResult!! )

        var msg = TrainActionMessage( actionToTrain, processed )

        Log.i(TAG, msg.serialize())

        prevMsgDelivered = sendToPi( msg.serialize() )
        if( !prevMsgDelivered )
            piAddr = null
    }

    private fun preProcessSpeechResults(speechResult: ArrayList<String> ): ArrayList<String>
    {
        var processed = ArrayList<String>()

        for( result in speechResult )
        {
            var res = result.replace(",", "" )
            res = res.replace(".", "" )
            res = res.replace("!", "" )
            res = res.replace("?", "" )
            res = res.toLowerCase()
            processed.add( res )
        }

        return processed
    }

    fun discoverPi(): Boolean
    {
        var piDiscoverer = PiDiscoverer(Config.DISCOVERY_ADDR, Config.DISCOVERY_PORT).also {
            it.execute()
        }

        piAddr = piDiscoverer.get().toString()
        Log.i( TAG, piAddr )

        mvController.onPiDiscoveryFinish()

        return piAddr != null
    }

    fun sendToPi( appMsg: String ): Boolean
    {
        var appMsgSender = AppMessageSender(
            piAddr!!,
            Config.APP_PORT
        ).also {
            it.execute( appMsg )
        }

        return appMsgSender.get().toString().toBoolean()
    }

    fun setSpeechResultCallbackCommand()
    {
        jarvisRecognizer.setOnSpeechResultCallback { result -> onSpeechResultCommand( result) }
    }

    fun setSpeechResultCallbackTraining()
    {
        jarvisRecognizer.setOnSpeechResultCallback { result -> onSpeechResultTraining( result) }
    }

    companion object
    {
        private var TAG = MainActivity::class.java.name
    }
}
