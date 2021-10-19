// Exercise 2 : Transform The Sentence


// Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph.
let bold = document.getElementsByTagName("strong");
let boldText = [];

function getBold_items(){
    for (let i of bold){
        boldText.push(i.textContent)
    }
    console.log(boldText)
}

getBold_items()

// Create a function called highlight() that changes the color of all the bold text to blue.
function highlight(){
    for (let i of bold){
        i.style.color = "blue"
    }
}



// Create a function called return_normal() that changes the color of all the bold text back to black.
function return_normal(){
    for (let i of bold){
        i.style.color = "black"
    }
}

// Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example

let paragraphe = document.body.firstElementChild;
paragraphe.addEventListener('mouseover', highlight)

paragraphe.addEventListener('mouseout', return_normal)