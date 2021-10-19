let point = ["", ".", "..", "..."];
let word = document.getElementById("word2");
let counter =0;

setInterval(addPoint, 300);

function addPoint() {
    if (counter<point.length){
        word.innerHTML = point[counter];
        counter++;
    }else{
        { counter = 0; }
    }
        
}