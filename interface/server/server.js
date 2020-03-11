const path = require("path");
const express = require('express')
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const bodyParser = require("body-parser");
require('./src/db/mongoose')

const populateDB = require("./src/db/populatedb"); // Uncomment code to create db


const publicPath = path.join(__dirname, "..", "public");
const port = process.env.PORT || 3000;

app.use(express.static(publicPath));
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

// API ROUTE
app.post('/webapp/api', (req, res) => {
    let query = req.body
    console.log(query)
});

app.get('*', (req, res) => {
    res.sendFile(path.join(publicPath, "index.html"));
});

io.on('connection', (socket) => {
    let message = {
        object: "music",
        toggle: "off"
    }

    io.sockets.emit('signal', message)
});

http.listen(3000, () => {
    console.log(`Server is up on port ${port}`);
});