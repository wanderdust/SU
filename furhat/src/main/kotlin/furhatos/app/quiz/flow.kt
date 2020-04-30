package furhatos.app.quiz

import furhatos.flow.kotlin.*
import furhatos.flow.kotlin.voice.PollyVoice
import furhatos.gestures.Gestures
import furhatos.util.Language
import furhatos.records.User
import furhatos.util.Gender
import Client
import furhatos.nlu.Intent
import furhatos.nlu.common.*

// Variables
val Idle: State = state {

    init {
        furhat.setVoice(Language.ENGLISH_GB, Gender.FEMALE)
        if (users.count > 0) {
            furhat.attend(users.random)
            goto(Start)
        }
    }

    onEntry {
        furhat.attendNobody()
    }

    onUserEnter {
        furhat.attend(it)
        goto(Start)
    }
}

val Interaction: State = state {

    onUserLeave(instant = true) {
        if (users.count > 0) {
            if (it == users.current) {
                furhat.attend(users.other)
                goto(Start)
            } else {
                furhat.glance(it)
            }
        } else {
            goto(Idle)
        }
    }

    onUserEnter(instant = true) {
        furhat.glance(it)
    }

}


val Start : State = state(Interaction) {

    onEntry {
        random(
            { furhat.ask("How can I help you?") },
            { furhat.ask("What can I do for you?") }
        )
        //goto(SendMessages)
    }

    onResponse{
        var resp:String = "furhat,${it.text},"
        println(resp)

        val address = "127.0.0.1"
        val port = 9999

        val client = Client(address, port)
        client.run(resp)

        while (client.connected) {
            val text = client.reader.nextLine()
            println(text)
            client.connected = false
            if (!text.contains("no message"))
                furhat.say (text)

        }

        client.reader.close()
        client.connection.close()


        var connect:Boolean = true
        while (connect) {
            var client = Client(address, port)
            client.run("test")
            val text = client.reader.nextLine()
            println(text)
            if (text.contains("no message"))
                connect = true
            else {

                furhat.say (text)
                connect = false
                client.reader.close()
                client.connection.close()
                break

            }
            client.reader.close()
            client.connection.close()
            if (connect)
                Thread.sleep(2000L)
        }

        goto(SendMessages)
    }
}

val SendMessages : State = state(Interaction) {

    onEntry {
        furhat.ask("Please tell me")
    }

    onResponse{
        var resp:String = "furhat,${it.text},"
        println(resp)

        val address = "127.0.0.1"
        val port = 9999

        val client = Client(address, port)
        client.run(resp)

        while (client.connected) {
            val text = client.reader.nextLine()
            println("text")
            println(text)
            client.connected = false
            if (!text.contains("no message"))
                furhat.say (text)

        }

        client.reader.close()
        client.connection.close()

        var connect:Boolean = true
        while (connect) {
            var client = Client(address, port)
            client.run("test")
            val text = client.reader.nextLine()
            println(text)
            if (text.contains("no message"))
                connect = true
            else {

                furhat.say (text)
                connect = false
                client.reader.close()
                client.connection.close()
                break

            }
            client.reader.close()
            client.connection.close()
            if (connect)
                Thread.sleep(2000L)
        }
    }
}


val SayAgain : State = state(Interaction) {

    onEntry {
        furhat.ask("Tell me again Please")
    }

    onResponse{
        var resp:String = "furhat,${it.text},"

        val address = "127.0.0.1"
        val port = 9999

        val client = Client(address, port)
        client.run(resp)
        println("Respose above ^^ŝ")

        while (client.connected) {
            val text = client.reader.nextLine()
            println(text)
            client.connected = false
            if (!text.contains("no message"))
                furhat.say (text)
            else if (text.contains("Do you mean Music? Do you mean TV? or Do you mean heating?")) {
                println("Hello")
            }

        }

        client.reader.close()
        client.connection.close()

    }
}