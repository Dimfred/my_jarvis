package de.dimfred.jarvis.core


import android.os.AsyncTask
import android.util.Log
import java.lang.Exception
import java.net.*

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

    override fun doInBackground( vararg params: String? ): Boolean
    {
        var success = true

        try
        {
            socket = makeTcpSocket()
            socket.connect( InetSocketAddress(piAddr, piPort), 200 )

            var appMsg = params[0]!!
            socket!!.outputStream.write( appMsg.toByteArray() )

            socket!!.close()
        }
        catch( e: Exception )
        {
            Log.i( TAG, e.toString() )
            success = false
        }

        return success
    }

    private fun makeTcpSocket(): Socket
    {
        var sock = Socket()
        sock.soTimeout = 300 // ms
        return sock
    }

    override fun onPostExecute(result: Boolean)
    {
        super.onPostExecute(result)
        return
    }

    companion object
    {
        val TAG = AppMessageSender::class.java.name
    }
}