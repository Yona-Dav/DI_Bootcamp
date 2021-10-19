// Exercise 2: Delete Colors

// Create a function called : removecolor() that removes the selected color from the dropdown list.
let select = document.getElementsByTagName('select')[0];
let options = document.getElementsByTagName('option');

function removecolor(){
    for( let i=0; i<options.length; i++){
        if (options[i].selected){
            select.removeChild(options[i])
        }
    }

}

let button = document.getElementsByTagName('input')[0];
button.addEventListener('click', removecolor)