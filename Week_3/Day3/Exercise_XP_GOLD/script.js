let allLetters = document.getElementsByClassName("letter");

function addTheEvent(){
    for (let letter of allLetters){
        letter.addEventListener("dragstart", startDragging)
        letter.addEventListener("dragend", endDragging)
    }
}

addTheEvent()

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
}

