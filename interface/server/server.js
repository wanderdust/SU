const path = require("path");
const express = require('express')
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const bodyParser = require("body-parser");
const Object = require("./src/models/object")
require('./src/db/mongoose')

const populateDB = require("./src/db/populatedb"); // Uncomment code to create db

const publicPath = path.join(__dirname, "..", "public");
const port = process.env.PORT || 3000;

app.use(express.static(publicPath));
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());



app.get('*', (req, res) => {
    res.sendFile(path.join(publicPath, "index.html"));
});

// SOCKET for real time updates
io.on('connection', (socket) => {

    // API ROUTE
    app.post('/webapp/api', (req, response) => {
        let query = req.body
 
        let doc = Object.findOneAndUpdate({
            object: query.object
        }, {
            toggle: query.toggle
        },
        {
            new: true
        }).then(res => {
            io.sockets.emit('signal', {
                object: res.object,
                toggle: res.toggle
            })
        }).then(res => {
            response.status(200).send({message: "Update successful"})
        }).catch(e => response.status(400).send(e))
    
    });
});

http.listen(3000, () => {
    console.log(`Server is up on port ${port}`);
});