const mongoose = require('mongoose')

// Schema
const objectSchema = new mongoose.Schema({
    object: {
        type: String,
        required: true,
        trim: true
    },
    toggle: {
        type: String,
        required: true,
        trim: true
    }
})

// Middleware
objectSchema.post('findOneAndUpdate', (doc, next) => {

    next()
})

const Object = mongoose.model('Object', objectSchema)

module.exports = Object