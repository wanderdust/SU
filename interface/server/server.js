const path = require("path");
var express = require('express')
const app = express();
var http = require('http').createServer(app);
var io = require('socket.io')(http);

const publicPath = path.join(__dirname, "..", "public");
const port = process.env.PORT || 3000;

app.use(express.static(publicPath));


app.get('/', function(req, res){
    res.sendFile(path.join(publicPath, "index.html"));
});

io.on('connection', function(socket){
    const message = {
        object: "music",
        toggle: "on"
    }

    io.emit("event", message)

});

http.listen(3000, function(){
    console.log(`Server is up on port ${port}`);
});
