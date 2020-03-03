function remove_task() {
    const id = event.target.parentNode.id
    fetch('/remove/' + id).then(response => window.location.reload())
}