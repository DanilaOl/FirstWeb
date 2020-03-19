function remove_task(event) {
    const id = event.target.parentNode.parentNode.id
    fetch('/remove/' + id).then(response => window.location.reload())
}

function toggleModal(event) {
    const el = document.getElementsByTagName('form')[0]
    // el.style.display = 'block'
    if (el.style.display == "none") {
    	el.style.display = "block"; } 
    else {
    	el.style.display = "none";
    }
}

const a = document.getElementById('form-toggler')
a.addEventListener('click', toggleModal)