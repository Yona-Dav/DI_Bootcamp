let dragItem = document.getElementById('item');

dragItem.addEventListener("dragstart", startDragging);

function startDragging(event){
    event.dataTransfer.setData('text/plain', event.target.id)
}

let drop = document.getElementsByClassName("dropzone")[0];

drop.addEventListener("dragover", draggingOver);
drop.addEventListener("drop", dropping);

function draggingOver(event){
    event.preventDefault();
}

function dropping(event){
    event.preventDefault();
    let elemToDrop = event.dataTransfer.getData('text/plain');
    let elemNode = document.getElementById(elemToDrop);
    event.target.appendChild(elemNode)
}