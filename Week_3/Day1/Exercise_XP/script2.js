// Exercise 2 : Users


// In the HTML above change the name “Pete” to “Richard”.
let secondli = document.getElementById("container").nextElementSibling.children[1];

secondli.innerText = 'Richard'


// Change each first name of the two <ul>'s to your name.
let ulElements = document.getElementsByClassName('list');
for (ul of ulElements){
    ul.children[0].innerText = "Yona"
}

// At the end of each <ul> add a <li> that says “Hey students”.
for (ul of ulElements){
    let newLi = document.createElement('li');
    let newText = document.createTextNode('Hey Students');
    newLi.appendChild(newText);
    ul.appendChild(newLi);
}

// Delete the name Sarah from the second <ul>.
let secondli2 = document.getElementById("container").nextElementSibling.nextElementSibling.children[1];

let ul2 = document.getElementById("container").nextElementSibling.nextElementSibling;

ul2.removeChild(secondli2)


// Bonus
// Add a class called student_list to both of the <ul>'s.
for (ul of ulElements){
    ul.classList.add('student_list');
}
// Add the classes university and attendance to the first <ul>.
let ul1 = document.getElementById("container").nextElementSibling;
ul1.classList.add('universtiy');
ul1.classList.add('attendance')