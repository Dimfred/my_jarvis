package de.dimfred.jarvis.core


import android.os.AsyncTask
import android.util.Log
import java.lang.Exception
import java.net.*
import java.nio.charset.Charset
import java.net.DatagramSocket

class PiDiscoverer: AsyncTask<String, Void, String?>
{
    private val broadcastAddr = Inet4Address.getByName("255.255.255.255" )
    private val port = 55555
    private var socket = makeDatagramSocket()


    constructor()
    {
    }

    override fun doInBackground(vararg params: String?): String?
    {
        var packet = makeDiscoveryPacket()

        var success = performDiscovery( packet )
        socket.close()

        if( !success )
            return null

        if( !isPacketFromPi( packet) )
            return null

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
        return DatagramPacket( discoverySend.clone(), discoverySend.size, broadcastAddr, port )
    }

    private fun performDiscovery( packet: DatagramPacket ): Boolean
    {
        var success = sendDiscoveryPacket( packet )
        if( !success ) {
            return false
        }

        success = recvDiscoveryPacket( packet )
        if( !success ) {
            return false
        }

        return true
    }

    private fun sendDiscoveryPacket( packet: DatagramPacket ): Boolean
    {
        try {
            socket.send(packet)
            // first packet is from the sender
            socket.receive(packet)
        }
        catch( e: Exception ) {
            Log.e(TAG, e.toString() )
            return false
        }

        return true
    }

    private fun recvDiscoveryPacket( packet: DatagramPacket ): Boolean
    {
        try {
            socket.receive(packet)
        }
        catch( e: SocketTimeoutException ) {
            Log.e(TAG, e.toString() )
            return false
        }
        catch( e: Exception ) {
            Log.e(TAG, e.toString() )
            return false
        }

        return true
    }

    private fun isPacketFromPi(packet: DatagramPacket ): Boolean
    {
        var response = packet.data.toString( Charset.defaultCharset() )

        if( response == discoveryRecv)
            return true

        return false
    }

    private fun extractIpAddr(packet: DatagramPacket ): String
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