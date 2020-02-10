package de.dimfred.jarvis

import android.graphics.drawable.Drawable
import android.util.Log
import androidx.core.content.ContextCompat
import de.dimfred.jarvis.core.Commands
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.activity_main.view.*

class MVController
{
    private var view: MainActivity

    constructor( view: MainActivity )
    {
        this.view = view
    }

    fun initOnClickListeners()
    {
        view.voiceBtn.setOnClickListener {
            if( view.discoverPi() )
                view.jarvisRecognizer.listen()
        }

        view.discoveryBtn.setOnClickListener {
            if( view.discoverPi() )
                view.discoverPi()
        }

        view.tvOnBtn.setOnClickListener {
            if( view.discoverPi() )
                view.sendToPi( Commands.TV_ON.serialize() )
        }

        view.tvOffBtn.setOnClickListener {
            if( view.discoverPi() )
                view.sendToPi( Commands.TV_OFF.serialize() )
        }

        view.lightOnBtn.setOnClickListener {
            if( view.discoverPi() )
                view.sendToPi( Commands.LIGHT_ON.serialize() )
        }

        view.lightOffBtn.setOnClickListener {
            if( view.discoverPi() )
                view.sendToPi( Commands.LIGHT_OFF.serialize() )
        }

        view.pcOnBtn.setOnClickListener {
            if( view.discoverPi() )
                view.sendToPi( Commands.PC_ON.serialize() )
        }

        view.pcOffBtn.setOnClickListener {
            if( view.discoverPi() )
                view.sendToPi( Commands.PC_OFF.serialize() )
        }

        view.trainingSw.setOnCheckedChangeListener { ctx,
            isChecked ->
                if( isChecked )
                    view.setSpeechResultCallbackTraining()
                else
                    view.setSpeechResultCallbackCommand()
        }

        view.reloadMappingBtn.setOnClickListener {
            if( view.discoverPi() )
                view.sendToPi( Commands.RELOAD_MAPPING.serialize() )
        }
    }

    fun onAppMsgBuild( appMsg: String )
    {

    }

    fun onPiDiscoveryFinish()
    {
        var ressourceId = if( view.piAddr != null )
            R.drawable.ic_sync_green
        else
            R.drawable.ic_sync_red

        view.discoveryBtn.background = ContextCompat.getDrawable( view, ressourceId )
    }

    companion object
    {
        val TAG = MVController::class.java.name
    }
}