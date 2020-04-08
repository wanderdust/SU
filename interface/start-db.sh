#!/bin/sh

$HOME/mongodb/bin/mongod --dbpath=$HOME/mongodb-data && node server/src/db/mongoose.js
