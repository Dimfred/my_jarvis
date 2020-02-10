package de.dimfred.jarvis

import androidx.test.platform.app.InstrumentationRegistry
import androidx.test.ext.junit.runners.AndroidJUnit4
import de.dimfred.jarvis.core.messages.CommandMessage
import de.dimfred.jarvis.core.messages.TrainActionMessage

import org.junit.Test
import org.junit.runner.RunWith

import org.junit.Assert.*

/**
 * Instrumented test, which will execute on an Android device.
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
@RunWith(AndroidJUnit4::class)
class ExampleInstrumentedTest
{
    companion object {
        val TAG = ExampleInstrumentedTest::class.java.name
    }
    @Test
    fun useAppContext() {
        // Context of the app under test.
        val appContext = InstrumentationRegistry.getInstrumentation().targetContext
        assertEquals("de.dimfred.Jarvis", appContext.packageName)
    }

    @Test
    fun testMessageSerialization()
    {
        val trainExpected = "{\"action_to_train\":\"light on\",\"method\":\"train_action\",\"speech_results\":[\"light on\",\"lights on\"]}"
        val trainMsg = TrainActionMessage( "light on", arrayListOf("light on", "lights on") )
        assertEquals(trainExpected , trainMsg.serialize() )

        val commandExpected = "{\"commands\":[\"light on\"],\"method\":\"command\"}"
        val commandMsg = CommandMessage( arrayListOf("light on") )
        assertEquals(commandExpected, commandMsg.serialize())

    }
}


