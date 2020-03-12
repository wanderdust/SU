/*
** Uncomment to create a database of default values

const Object = require("../models/object");

const populateDB = () => {
    const lights = new Object({
        object: "lights",
        toggle: "off"
    })
    
    lights.save().then(() => {
        console.log(lights)
    }).catch(error => console.log(error))
    
    const tv = new Object({
        object: "tv",
        toggle: "off"
    })
    
    tv.save().then(() => {
        console.log(tv)
    }).catch(error => console.log(error))
    
    const music = new Object({
        object: "music",
        toggle: "off"
    })
    
    music.save().then(() => {
        console.log(music)
    }).catch(error => console.log(error))
    
    const heating = new Object({
        object: "heating",
        toggle: "off"
    })
    
    heating.save().then(() => {
        console.log(heating)
    }).catch(error => console.log(error))
    
    
    console.log("database created successfuly")
}

populateDB()


module.exports = populateDB

*/