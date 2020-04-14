package furhatos.app.quiz

import furhatos.flow.kotlin.*
import furhatos.flow.kotlin.voice.PollyVoice
import furhatos.gestures.Gestures
import furhatos.util.Language
import furhatos.nlu.common.Goodbye
import furhatos.nlu.common.No
import furhatos.nlu.common.RequestRepeat
import furhatos.nlu.common.Yes
import furhatos.records.User
import furhatos.util.Gender
import Client

// Variables
val Idle: State = state {

    init {
        furhat.setVoice(Language.ENGLISH_US, Gender.MALE)
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
        furhat.say("What can i do for you")
        goto(SendMessages)
    }
/*
    onResponse {
        furhat.say("I understood that you said ${it.text}")
    }*/

}

val sayAgain : State = state(Interaction) {

    onEntry {
        furhat.ask("tell me")
    }

    onResponse{
        var resp:String = "furhat,${it.text},"

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

            else if (text.contains("Bye")) {
                furhat.say(text)
                goto(Idle)
            }
            else{
                furhat.say(text)
            }


        }
        if (resp.contains("nothing"))
        {
            furhat.say("Thank you, i enjoyed helping you today")
            goto(Idle)
        }

        client.reader.close()
        client.connection.close()

        goto(SendMessages)

    }


}


val SendMessages : State = state(Interaction) {

    onEntry {
        furhat.ask("Please say")
    }

    onResponse{
        var resp:String = "furhat,${it.text},"

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



        if (resp.contains("nothing"))
        {
            furhat.say("Thank you, i enjoyed helping you today")
            goto(Idle)
        }

        goto(sayAgain)
        //goto(Start)


        //furhat.say("I like humans.")
    }

}
