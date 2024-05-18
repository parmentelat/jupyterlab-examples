// standard JS additions for our jupyter books

// expose to the console
const cheatCorrige = () => {
    // open a corrige file which is located under
    // the .teacher folder with an extra "corrige-" suffix
    // e.g. "my-book-nb.html" -> ".teacher/my-book-nb-corrige.html"
    const currentLocation = window.location.href
    const newLocation = currentLocation.replace(
        /(.*)\/([a-z0-9-]+)-nb\.html/gm,
        "$1/.teacher/$2-corrige-nb.html"
    )
    // console.log(newLocation)
    window.location.href = newLocation
}

// run the following code when the page is loaded
window.addEventListener('load',
() => {

    const urlTocEntriesOpenInNewTab = () => {
        console.log("from my-book.js: url-typed toc entries open in a separate tab")
        document.querySelectorAll("nav a.reference.external")
            .forEach(node => node.target = "_blank")
    }

    // define a keyboard shortcut to
    const cheatCorrigeShortcut = () => {
        console.log("from my-book.js: corrige shortcuts")
        document.addEventListener("keydown", (event) => {
            if (event.key === "?" && event.ctrlKey & event.shiftKey) {
                cheatCorrige()
            }
        })
    }

    const outlineCorrige = () => {
        if (window.location.href.includes("corrige")) {
            document.body.classList.add("corrige")
        }
    }

    // our setup
    urlTocEntriesOpenInNewTab()
    outlineCorrige()
    cheatCorrigeShortcut()
})
