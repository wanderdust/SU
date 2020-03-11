const mongoose = require('mongoose')

const Object = mongoose.model('Object', {
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

module.exports = Object