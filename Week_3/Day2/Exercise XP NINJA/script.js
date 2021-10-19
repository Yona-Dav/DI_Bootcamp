// Exercise 1 : Calculate The Tip
// First Part :

// Create a function called calculateTip() that takes no parameter.

let small = document.getElementById('each');
let totip = document.getElementById('totalTip');



function calculateTip(){
    let billAmount = document.getElementById('billamt').value;
    let serviceQuality = document.getElementById('serviceQual').value;
    let numberOfPeople = document.getElementById('peopleamt').value;

    if (billAmount === "" || serviceQuality == 0) {
        alert("Please enter values");
        return;
    
    }
    if (numberOfPeople.length===0 || numberOfPeople<1 ){
        numberOfPeople = 1;
        small.style.display = 'none';
    }else{
    small.style.display = 'block';}

    
    let total =( billAmount  * serviceQuality ) / numberOfPeople ;
    total = total.toFixed(2);
    totip.style.display = 'block';
    let span = document.getElementById('tip');
    span.innerHTML = total;


}

totip.style.display = 'none';
small.style.display = 'none';

let button = document.getElementById('calculate');
button.onclick=function(){calculateTip()}
