package de.dimfred.jarvis.core


import android.os.AsyncTask
import android.util.Log
import java.lang.Exception
import java.net.*
import java.nio.charset.Charset
import java.net.DatagramSocket

class PiDiscoverer: AsyncTask<Void, Void, String?>
{
    private val addr: InetAddress
    private val port: Int

    private var socket: DatagramSocket

    constructor( addr: String, port: Int )
    {
        this.addr = Inet4Address.getByName(addr )
        this.port = port
        socket = makeDatagramSocket()
    }

    override fun doInBackground(vararg params: Void?): String?
    {
        var packet = makeDiscoveryPacket()

        try
        {
            // perform discovery
            socket.send(packet)
            socket.receive(packet) // from myself
            socket.receive(packet) // hopefully from PI
            socket.close()

            if( !isPacketFromPi(packet) )
                return null
        }
        catch( e: Exception )
        {
            Log.i( TAG, e.toString() )
            return null
        }

        return extractIpAddr( packet )
    }

    override fun onPostExecute(result: String?) {
        super.onPostExecute(result)
        return
    }

    private fun makeDatagramSocket(): DatagramSocket
    {
        var sock = DatagramSocket(null)
        sock.reuseAddress = true
        sock.soTimeout = 500
        sock.bind( InetSocketAddress(port) )
        return sock
    }

    private fun makeDiscoveryPacket(): DatagramPacket
    {
        return DatagramPacket( discoverySend.clone(), discoverySend.size, addr, port )
    }

    private fun isPacketFromPi( packet: DatagramPacket ): Boolean
    {
        var response = packet.data.toString( Charset.defaultCharset() )

        if( response != discoveryRecv )
            return false

        return true
    }

    private fun extractIpAddr( packet: DatagramPacket ): String
    {
        var addr = packet.address
            .toString()
            .removePrefix("/")

        Log.i(TAG, "Extracted Address: $addr" )
        return addr
    }

    companion object
    {
        private val TAG = PiDiscoverer::class.java.name
        private val discoverySend = "WHO DIS".toByteArray()
        private const val discoveryRecv = "IT'S PI"
    }
}