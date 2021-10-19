let point = ["", ".", "..", "..."];
let word = document.getElementById("word2");
let counter =0;

setInterval(addPoint, 300);

function addPoint() {
    if (counter<text.length){
        elem.innerHTML = text[counter];
        counter++;
    }else{
        { counter = 0; }
    }
        
}

