// standard JS additions for our jupyter books

window.addEventListener('load',
() => {

    function urlTocEntriesOpenInNewTab() {
        console.log("from my-book.js: url-typed toc entries open in a separate tab")
        document.querySelectorAll("nav a.reference.external")
            .forEach(node => node.target = "_blank")
    }

    // define a keyboard shortcut to open a corrige file
    // which is located under the .teacher folder with an extra "corrige-" suffix
    // e.g. "my-book-nb.html" -> "my-book-nb-corrige.html"
    function corrigeCheatShortcut() {
        console.log("from my-book.js: corrige shortcuts")
        const gotoCorrige = () => {
            const currentLocation = window.location.href
            const newLocation = currentLocation.replace(
                /(.*)\/([a-z0-9-]+)-nb\.html/gm,
                "$1/.teacher/$2-corrige-nb.html"
            )
            console.log(newLocation)
            window.location.href = newLocation
        }
        document.addEventListener("keydown", (event) => {
            if (event.key === "c" && event.ctrlKey) {
                gotoCorrige()
            }
        })
    }

    urlTocEntriesOpenInNewTab()
    corrigeCheatShortcut()
})
