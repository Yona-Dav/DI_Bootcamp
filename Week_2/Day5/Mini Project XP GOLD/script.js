
function number(num){
    document.getElementById("display").value+=num
}

function operator(op){
    document.getElementById("display").value+=op
}

function equal(){
    document.getElementById("display").value = eval(document.getElementById("display").value)
}


function clr(){
    document.getElementById("display").value = document.getElementById("display").value.slice(0, -1);
}

function reset(){
    document.getElementById("display").value = ""
}

