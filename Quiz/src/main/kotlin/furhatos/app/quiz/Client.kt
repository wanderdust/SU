import java.io.OutputStream
import java.net.Socket
import java.nio.charset.Charset
import java.util.*
import kotlin.concurrent.thread

fun main(args: Array<String>) {
    //val address = "127.0.0.1"
    //val port = 65432

    //val client = Client(address, port)
    //client.run()
}

class Client(address: String, port: Int) {
    public val connection: Socket = Socket(address, port)
    public var connected: Boolean = true

    init {
        println("Connected to server at $address on port $port")
    }

    public val reader: Scanner = Scanner(connection.getInputStream())
    public val writer: OutputStream = connection.getOutputStream()

    fun run(message: String) {
        // thread { read() }
        //while (connected) {
            ///val input = readLine() ?: ""
            val input = message

            if (input != ""){
                if ("exit" in input) {
                    connected = false

                } else {

                    write(input)


                }
            }

        //}

    }

    private fun write(message: String) {
        writer.write((message + '\n').toByteArray(Charset.defaultCharset()))
    }

    private fun read() {
       /* while (connected) {
            val text = reader.nextLine()
            println(text)
            connected = false
            reader.close()
            connection.close()

        }*/
    }
}