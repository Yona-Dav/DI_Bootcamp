
// Exercise 1: Simple If/Else Statement

// Create 2 variables, x and y. Each of them should have a different numeric value.
// Write an if/else statement that checks which number is bigger.

let x = parseInt(prompt('Give me a number'));
let y = parseInt(prompt('Give me an other number'));

if (x>y) {
    console.log(`x = ${x} is the biggest`)
}else if (x<y) {
   console.log( `y = ${y} is the biggest`)
}else{
    console.log('There are equal')
}



// Exercise 2: Chihuahua


// Create a variable called newDog where it’s value is “Chihuahua”.
let newDog = 'Chihuahua';
console.log(newDog);

// Check and display how many letters are in newDog.
console.log(newDog.length); 

// Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
console.log(newDog.toLowerCase());
console.log(newDog.toUpperCase());

// Check if the variable newDog is equal to “Chihuahua”
// if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’

if (newDog === 'Chihuahua'){
    console.log("I love Chihuahuas, it's my favorite dog breed")
}else{
    console.log("I dont care, I prefer cats")
}



// Exercise 3: Even Or Odd

// Prompt the user for a number and save it to a variable.
let z = parseInt(prompt('Enter a number'));

// Check whether the variable is even or odd.
// If it is even, display: “x is an even number”. Where x is the actual number the user chose.
// If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.
if (x%2 == 0) {
    console.log('z is an even number')
}else{
    console.log('z is an odd number')
}



// Exercise 4: Group Chat

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]

// Using the array above, console.log the number of users in a group chat based on the following rules:
// If there is no users (the users array is empty), console.log “no one is online”.
// If there is 1 user, console.log “<name_user> is online”.
// If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
// If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.



if (users.length === 0){
    console.log("No one is online")
}else if (users.length === 1){
    console.log(`${users[0]} is online`)
}else if (users.length === 2) {
    console.log(`${users[0]} and ${users[1]} are online`)
}else {
   console.log( `${users[0]} , ${users[1]} and ${users.length - 2} more are online`)
}

