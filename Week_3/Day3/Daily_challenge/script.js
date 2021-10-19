let inputText = document.getElementById('letters');


inputText.addEventListener('keyup', function(event) {
    this.value = this.value.replace(/[^a-zA-Z]/g, '');
});



