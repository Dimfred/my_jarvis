package de.dimfred.jarvis_no_service.command


import android.os.AsyncTask
import android.util.Log
import java.net.ConnectException

import java.net.Socket

class Sender: AsyncTask<String, Void, String>
{
    private var _ip: String
    private var _port: Int

    constructor( ip: String, port: Int )
    {
        _ip = ip
        _port = port
    }

    override fun doInBackground(vararg params: String?): String
    {
        try {
            var socket = Socket( _ip, _port )
            socket.outputStream.write( params[0]!!.toByteArray() )
            socket.close()
        } catch( e: ConnectException ) {
            Log.i( "Sender", "Could not establish connection." )
        }

        return ""
    }
}