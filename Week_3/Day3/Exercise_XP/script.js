let redbox = document.getElementById('animate');
let position = 0;

function myMove(){
  let anim = setInterval(move, 5);
}

function move(){
  if (position === 350){
    clearInterval(anim);
  }else{
    position ++;
    redbox.style.top = position + "px";
    redbox.style.left = position + "px";
  }
}



