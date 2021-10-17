// Exercise 3 : Users And Style

// Add a “light blue” background color and some padding to the <div>.
let div = document.body.firstElementChild;
div.style.backgroundColor = "lightblue";
div.style.padding = '10px';

// Do not display the first name (John) in the list.
let firstname = div.nextElementSibling.firstElementChild;

firstname.style.display = "none";

// Add a border to the second name (Pete).
let secondname = firstname.nextElementSibling;
secondname.style.border = "2px black solid"

// Change the font size of the whole body.
document.body.style.fontSize='30px';

// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).

if (div.style.backgroundColor==='lightblue'){
    alert(`Hello ${firstname.textContent} and ${secondname.textContent}`)
}