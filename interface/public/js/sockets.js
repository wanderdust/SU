let socket = io();

socket.on('signal', message => {
    console.log(message)
})
