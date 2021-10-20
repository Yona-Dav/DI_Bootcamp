let colors = ['red','orangered', 'orange','yellow','yellowgreen','green', 'blue','pink','purple', 'turquoise', 'brown', 'white', 'black', 'salmon', 'lightblue','ligthgreen', 'lightpink', 'lightsalmon', 'blueviolet','gold','violet'];

let palet = document.getElementById('palet');

for (i = 0; i < (7 * 3); i++) {
    let block = document.createElement("div");
    block.style.backgroundColor = colors[i];
    block.addEventListener('click',getColor);
    block.classList.add('colors');
    palet.appendChild(block);
};

let paint = document.getElementById('painting');

for (c = 0; c < (24 * 60); c++) {
    let cell = document.createElement("div");
    cell.addEventListener('click',setColor);
    cell.addEventListener('mousedown', draw);
    cell.addEventListener('mouseover', ifdraw);
    cell.addEventListener('mouseup', nodraw);
    cell.classList.add('cell');
    paint.appendChild(cell);
};

let clear = document.getElementById('clear');

clear.addEventListener('click',deleteColor);
function deleteColor(event){
    let div = document.getElementsByClassName('cell');
    for (let i of div){
        i.style.backgroundColor = 'white'
    }
}


let myColor = "";
function getColor(event){
    myColor = event.target.style.backgroundColor;
    console.log(myColor)
    
}

function setColor(event){
    event.target.style.backgroundColor = myColor;
}

let isMouseDown = Boolean;
function draw(){
    isMouseDown = true;
}

function nodraw(){
    isMouseDown = false;
}

function ifdraw(event){
    if (isMouseDown==true){
        event.target.style.backgroundColor = myColor;
    }
}

