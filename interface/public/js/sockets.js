let socket = io();

socket.on('signal', message => {

    if (message.object == "tv") {
        console.log("turn the "+ message.object + " "+ message.toggle)
    } else if (message.object == "music") {
        console.log("turn the "+ message.object + " "+ message.toggle)
    } else if (message.object == "lights") {
        console.log("turn the "+ message.object + " "+ message.toggle)
    } else if (message.object == "heating") {
        console.log("turn the "+ message.object + " "+ message.toggle)
    }
})
