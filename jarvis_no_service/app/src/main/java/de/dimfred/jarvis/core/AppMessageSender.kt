package de.dimfred.jarvis.core


import android.os.AsyncTask
import android.util.Log
import java.lang.Exception

import java.net.Socket

class AppMessageSender: AsyncTask<String, Void, Boolean>
{
    private lateinit var socket: Socket
    private val piAddr: String
    private val piPort: Int

    constructor( ip: String, port: Int )
    {
        piAddr = ip
        piPort = port
    }

    override fun doInBackground(vararg params: String?): Boolean
    {
        socket = Socket( piAddr, piPort )
        // in ms
        socket.soTimeout = 500


        var appMsg = params[0]!!

        val success = sendAppMsg( appMsg )

        socket.close()

        return success
    }

    override fun onPostExecute(result: Boolean) {
        super.onPostExecute(result)
        return
    }

    private fun sendAppMsg( appMsg: String ): Boolean
    {
        try {
            socket.outputStream.write( appMsg.toByteArray() )
        }
        catch( e: Exception ) {
            Log.e(TAG, e.toString() )
            return false
        }

        return true
    }

    companion object
    {
        val TAG = AppMessageSender::class.java.name
    }
}