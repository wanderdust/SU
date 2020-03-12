const addHTML = (selector, html, isMusic) => {
    $(`.${selector}`).html("")
    $(`.${selector}`).append(html)

    if (isMusic) {
        const html = `<iframe src="/images/music/Beethoven - 7th Symphony - 2nd movement.mp3" allow="autoplay" id="audio"></iframe>`
        $(`.background-song`).append(html)
    }
}

const removeHTML = (selector, isMusic) => {
    $(`.${selector}`).parent().addClass("off")
    $(`.${selector}`).html("")

    if (isMusic) {
        $(`.background-song`).html("")
    }
}