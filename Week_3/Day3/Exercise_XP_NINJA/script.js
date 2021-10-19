let button = document.getElementById('firstbox');

button.addEventListener('click', addbox)

function addbox(){
    let box = document.createElement('div');
    box.classList.add('box');
    let section = document.getElementById('all');
    section.append(box);
    box.style.backgroundColor = randomColor()
}

function randomColor(){
    let x = Math.floor(Math.random() * 256);
    let y = Math.floor(Math.random() * 256);
    let z = Math.floor(Math.random() * 256);
    let bgColor = "rgb(" + x + "," + y + "," + z + ")";
    return bgColor;
}
