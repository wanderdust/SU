let socket = io();

socket.on('signal', message => {

    if (message.object == "tv") {
        if (message.toggle == "on") {
            console.log("turn the "+ message.object + " "+ message.toggle)

            const html = `<img class="tv-on" src="/images/futurama_intro.gif" alt="tv">`
            addHTML("tv-container", html)
        } else {
            removeHTML("tv-container")
        }
    } else if (message.object == "music") {
        console.log("turn the "+ message.object + " "+ message.toggle)

        if (message.toggle == "on") {
            const html = `<img class="music-on" src="/images/music_on.gif" alt="music">`
            addHTML("music-container", html, true)
        } else {
            removeHTML("music-container", true)
        }
    } else if (message.object == "lights") {
        console.log("turn the "+ message.object + " "+ message.toggle)

        if (message.toggle == "on") {
            const html = `<img class="lights-on" src="/images/lights_on.png" alt="lights">`
            addHTML("lights-container", html)
        } else {
            removeHTML("lights-container")
        }
    } else if (message.object == "heating") {
        console.log("turn the "+ message.object + " "+ message.toggle)

        if (message.toggle == "on") {
            const html = `<img class="heating-on" src="/images/fire_on.gif" alt="tv">`
            addHTML("heating-container", html)
        } else {
            removeHTML("heating-container")
        }
    }
})
