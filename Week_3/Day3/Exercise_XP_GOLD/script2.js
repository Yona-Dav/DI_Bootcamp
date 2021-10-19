let parag = document.getElementsByTagName('p')[0];

parag.setAttribute("draggable", "true");

parag.addEventListener("dragstart", startDragging);
parag.addEventListener("dragend", endDragging)


function startDragging(event){
    event.target.classList.add("startDrag");
    console.log ("dragstart " +  "X: " + event.clientX  + " Y: " +  event.clientY);
}

function endDragging(event){
    event.target.classList.add("endDrag");
    let _x = event.clientX;
    let _y = event.clientY;
    event.target.style.left = _x + "px";
    event.target.style.top = _y + "px";
    event.target.style.position = "absolute"; //Necessary
    console.log ("dragend" + "X: " + event.clientX  + " Y: " +  event.clientY );

    if(event.target.style.left<'400px'){
        event.target.style.fontSize = '50px';
    }else if (event.target.style.left>'800px'){
        event.target.style.fontSize = '10px';
    }else{
        event.target.style.fontSize = '30px';
    }
}
