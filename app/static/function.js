var mouseClickTrig = (el, callback) => {
    el.forEach((checkbox) => {
        callback(checkbox)
    })
}

mouseClickTrig(document.getElementsByName('mouseClickTrig'), (item) => {
    item.onclick = (e) => {
        mouseClickTrig(document.getElementsByName('mouseClickTrig'), (item) => {
            item.checked = false;
        })
        e.target.checked = true;

    }
})

var shortPlug = (el, callback) => {
    el.forEach((checkbox) => {
        callback(checkbox)
    })
}

shortPlug(document.getElementsByName('shortPlug'), (item) => {
    item.onclick = (e) => {
        shortPlug(document.getElementsByName('shortPlug'), (item) => {
            item.checked = false;
        })
        e.target.checked = true;

    }
})

var longPlug = (el, callback) => {
    el.forEach((checkbox) => {
        callback(checkbox)
    })
}

longPlug(document.getElementsByName('longPlug'), (item) => {
    item.onclick = (e) => {
        longPlug(document.getElementsByName('longPlug'), (item) => {
            item.checked = false;
        })
        e.target.checked = true;

    }
})

var digTrigUltimateMelee = (el, callback) => {
    el.forEach((checkbox) => {
        callback(checkbox)
    })
}

digTrigUltimateMelee(document.getElementsByName('digTrigUltimateMelee'), (item) => {
    item.onclick = (e) => {
        digTrigUltimateMelee(document.getElementsByName('digTrigUltimateMelee'), (item) => {
            item.checked = false;
        })
        e.target.checked = true;

    }
})

var digTrigUltimate = (el, callback) => {
    el.forEach((checkbox) => {
        callback(checkbox)
    })
}

digTrigUltimate(document.getElementsByName('digTrigUltimate'), (item) => {
    item.onclick = (e) => {
        digTrigUltimate(document.getElementsByName('digTrigUltimate'), (item) => {
            item.checked = false;
        })
        e.target.checked = true;

    }
})

var stabilizedTrigs = (el, callback) => {
    el.forEach((checkbox) => {
        callback(checkbox)
    })
}

stabilizedTrigs(document.getElementsByName('stabilizedTrigs'), (item) => {
    item.onclick = (e) => {
        stabilizedTrigs(document.getElementsByName('stabilizedTrigs'), (item) => {
            item.checked = false;
        })
        e.target.checked = true;

    }
})

var shortenedSpring = (el, callback) => {
    el.forEach((checkbox) => {
        callback(checkbox)
    })
}

shortenedSpring(document.getElementsByName('shortenedSpring'), (item) => {
    item.onclick = (e) => {
        shortenedSpring(document.getElementsByName('shortenedSpring'), (item) => {
            item.checked = false;
        })
        e.target.checked = true;

    }
})

var removedSpring = (el, callback) => {
    el.forEach((checkbox) => {
        callback(checkbox)
    })
}

removedSpring(document.getElementsByName('removedSpring'), (item) => {
    item.onclick = (e) => {
        removedSpring(document.getElementsByName('removedSpring'), (item) => {
            item.checked = false;
        })
        e.target.checked = true;

    }
})

