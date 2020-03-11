let socket = io();


socket.on('event', function(msg) {

    if (msg.obj == "ligths") {
        console.log("Turn the " + msg.object + " " + msg.toggle)

    } else if (msg.obj == "music") {
        console.log("foo")

        console.log("Turn the " + msg.object + " " + msg.toggle)

    } else if (msg.obj == "heating") {
        console.log("Turn the " + msg.object + " " + msg.toggle)

    } else if (msg.obj == "tv") {
        console.log("Turn the " + msg.object + " " + msg.toggle)

    }
})
