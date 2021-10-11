// Exercise 1 : Age Difference

// Given the years two people were born, find the date when the younger one is exactly half the age of the older.

let dateone = parseInt(prompt("Enter the year of your birth"));
let datetwo =parseInt(prompt("Enter the year of your birth"));

if (dateone>datetwo){
    let x = dateone - datetwo;
    let date1 = dateone + x;
    console.log(`The date is : ${date1}`)
}else if (dateone<datetwo){
    let x = datetwo - dateone;
    let date2 = datetwo + x;
    console.log(`The date is : ${date2}`)
}else{
    console.log("They have the same age")
}

// Exercise 2 : Zip Codes


// Hint : This exercise has 2 parts. First, do this exercise without Regular Expressions, then do it using Regular Expressions

// While working in a Post Office you must have the clients’ zip code in order to send them their letters.
// Ask the client for their zip code and console.log “success” or “error” based on the following rules.
// Zip codes consists of 5 numbers
// Must only contain numbers
// Must not contain any whitespace (spaces)
// Must not be greater than 5 digits in length


// Without Regular Expressions
let zip = parseInt(prompt('Enter your zip code'));

if ( zip.toString().length === 5 && !isNaN(zip) && zip.toString().indexOf(' ')===-1){
    console.log("Success")
} else{
    console.log('Error')
}

// With Regular Expressions
let zip1 = parseInt(prompt('Enter your zip code'));


if (zip1.toString().length === 5 && zip1.toString().match(/^[0-9]+$/) != null && !/\s/.test(zip1) ){
    console.log("Success")
}else{
    console.log('Error')
}

// Exercise 3 : Secret Word

// Prompt the user for a word and save it to a variable.
let word = prompt('Enter a word').toLowerCase()


// Delete all the vowels of the word and console.log the result.
console.log(word.replace(/[aeiou]/g, ""))

// Bonus: Replace the vowels with another character and console.log the result
let character = {'a':1, 'e':2, 'i':3, 'o':4,'u':5}
console.log(word.replace(/[aeiou]/g, m =>character[m]))