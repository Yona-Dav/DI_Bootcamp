// Exercise 1 : Your Favorite Colors

// Create an array called colors where the value is a list of your favorite colors.
let colors = ['blue', 'red', 'orange','purple'];

// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
for (let i=0; i<colors.length; i++) {
    console.log(`My #${i+1} choice is ${colors[i]}`)
}


// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus
let suffixes = ['st','nd','rd','th'];

for (let i=0; i<colors.length; i++) {
    console.log(`My ${i+1}${suffixes[i]} choice is ${colors[i]}`)
}



// Exercise 2 : List Of People

let people = ["Greg", "Mary", "Devon", "James"]

// Write code to remove “Greg” from the people array.
people.shift()
console.log(people)

// Write code to replace “James” to “Jason”.
people.splice(2,1,'Jason')
console.log(people)

// Write code to add your name to the end of the people array.
people.splice(3,0,'Yona')
console.log(people)

// Using a loop, iterate through the people array and console.log each person.
for (let element of people){
    console.log(element)
}

// Using a loop, iterate through the people array and after you console.log “Jason” exit the loop.
for (let element of people){
    if (element==='Jason'){
        break;
    }
    console.log(element)
}

// Write code to make a copy of the people array using slice. The copy should NOT include “Mary” or your name.
let people2 = people.slice(-3);
console.log(people2);

let people3 = people.slice(0,3);
console.log(people3);

// Write code that console.logs Mary’s index.
console.log(people.indexOf('Mary'));


// Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
console.log(people.indexOf('Foo'));
// It returns -1 because it does not exist

// Create a variable called last which value is the last element of the array.
let last = people[people.length-1] ;
console.log(last)


// Exercise 3 : Repeat The Question

// Prompt the user for a number, while the number is smaller than 10 continue asking the user for a new number.
let i = parseInt(prompt('Enter a number'));
while (i<10){
    console.log("The number is " + i)
  i = parseInt(prompt('Enter a number'));
}


// Exercise 4 : Attendance

let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

// Prompt the student for their name :
let names = prompt('Enter a name').toLowerCase();

// If the name is in the object, console.log the name of the student and the country they come from.
// If the name is not in the object, console.log: "Hi! I'm a guest."

if (names in guestList){
    console.log(`Hi! I'm ${names}, and I'm from ${guestList[names]}`);
}else{
    console.log('Hi! I am a guest.');
}


// Exercise 5 : Family

// Create an object called family with a few key value pairs.
let family = {
    firstname: "Lea",
    Lastname: "Smith",
    children: 4,
    city: "London"
  }

// Console.log the keys. (using a for loop).
for (let element in family){
    console.log(element)
}

// Console.log the values. (using a for loop).
for (let element in family){
    console.log(family[element])
}


// Exercise 6

let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

let sentence = []
// Given the object above, console.log “my name is Rudolf the raindeer”
for (let element in details){
    sentence += element+' '+details[element]+' '
}
console.log(sentence)



// Exercise 7 : Secret Group

let surname = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.

let x = surname.toString();
let society = x.match(/\b(\w)/g).join('');
console.log('The name of their secret society is',society)
