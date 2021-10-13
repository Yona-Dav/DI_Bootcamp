// Exercise 1 : Information

// Part I
// Create a function called infoAboutMe() that takes no parameter.
// The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
// Call the function. 

function infoAboutMe(){
    console.log("My name is Yona, I am 27 years old")
}

infoAboutMe()

// Part II
// Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.
// The function should console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
function infoAboutPerson(personName, personAge, personFavoriteColor){
    console.log(`You name is ${personName}, You are ${personAge} years old, your favorite color is ${personFavoriteColor}` );
}
// Call the function twice with the following arguments:
infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")


// Part III
// Add a parameter personHobbies to the function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies).
function infoAboutPersons(personName, personAge, personFavoriteColor, personHobbies){
    console.log(`You name is ${personName}, You are ${personAge} years old, your favorite color is ${personFavoriteColor}` );
    for (element of personHobbies){
        console.log(`your hobies are ${element}`)    
    }
}

// Call the function twice with the following arguments:
infoAboutPersons("David", 45, "blue", ["tennis", "painting"])
infoAboutPersons("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])



// Exercise 2 : Keyless Car

// Ask the user for their age, and save the value to a variable.
let age = parseInt(prompt('Enter your age'));

// Create a function called checkDriverAge() that will notify the user if they are permitted to drive. They must be at least 18 to drive.
function checkDriverAge(){
    if (age < 18){
        alert('Sorry, you are too young to drive this car. Powering off')
    }else if (age > 18){
        alert('You are old enough to drive, Powering On. Enjoy the ride!')
    }else{
        alert('Congratulations on your first year of driving. Enjoy the ride!')
    }
}


// Call the function.
checkDriverAge()

// Instead of using prompt to ask the user for their age, have the checkDriverAge() function accept an argument age.
function checkDriverAges(age){
    if (age < 18){
        alert('Sorry, you are too young to drive this car. Powering off')
    }else if (age > 18){
        alert('You are old enough to drive, Powering On. Enjoy the ride!')
    }else{
        alert('Congratulations on your first year of driving. Enjoy the ride!')
    }
}
checkDriverAges(25)


// Exercise 3: Odd Or Even

function checkNumber(){
    for (i=0; i<101; i++){
        if (i%2===0){
            console.log(`The number ${i} is even`)
        }else{
            console.log(`The number ${i} is odd`)
        }
    }
}

checkNumber()



// Exercise 4: Find The Numbers Divisible By 23

// All in one function
// function isDivisible(){
//     let y = [];
//     let sum=0;
//     for(i=0; i<501; i++){
//         if(i%23===0){
//             y.push(i);   
//         }
//     }console.log(y);
//     for (num of y){
//         sum += num;

//     }console.log('Sum:', sum)
// }

// In two functions
function isDivisible(){
    let y = [];
    for(i=0; i<501; i++){
        if(i%23===0){
            y.push(i);   
        }
    }console.log(y);
    return y
}

function sumOfDivisible(){
    let sum=0;
    for (num of isDivisible()){
        sum += num
    }console.log('Sum:', sum)
}

isDivisible()
sumOfDivisible()

// Bonus: Add a parameter divisor to the function.
function isDivisibles(divisor){
    let y = [];
    let sum=0;
    for(i=0; i<501; i++){
        if(i%divisor===0){
            y.push(i);   
         }
    }
    for (num of y){
        sum += num;
    
     }console.log(`The numbers divisible by ${divisor} are ${y} and their sum is ${sum}`)
    }

isDivisibles(3)
isDivisibles(45)



// Exercise 5 : Amazon Shopping

let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function checkBasket(){
    let item = prompt('Which item do you want');
    if (item in amazonBasket){
        console.log('The item is in the basket')
    }else{
        console.log('The item is not in the basket')
    }
}

checkBasket()


// Exercise 6 : What’s In My Wallet ?

function changeEnough([quarters, dimes, nickels, pennies], price ){
    let amount = quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01;
    if (amount >= price){
        console.log('You can afford the item')
    }else{
        console.log('Sorry ... You cannot afford the item')
    }
}

changeEnough([2, 100, 0, 0], 14.11)
changeEnough([0, 0, 20, 5], 0.75)

// Exercise 7 : Shopping List

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

// Create an array called shoppingList
let shoppingList = ['banana','apple','orange']

// Create a function called myBill() that return the total price of your shoppingList.
function myBill(){
    let price = 0;
    for (element of shoppingList){
        if(element in stock){
            price += prices[element]
            prices[element] -= 1;

        }
    }console.log(price);
    console.log(prices)
}

myBill()



// Exercise 8 : Tips

function TipAmount(){
    let amount = parseFloat(prompt('Enter the amount of the bill'));
    let tip =0;
    let bill = amount;
    if (amount < 50){
        tip += amount*0.2;
        bill += tip;
        console.log(`The amount of the tip is ${tip} and the total bill is ${bill}`)
    }else if ( amount<= 200 && amount >= 50){
        tip += amount*0.15;
        bill += tip;
        console.log(`The amount of the tip is ${tip} and the total bill is ${bill}`)
    }else{
        tip += amount*0.1;
        bill += tip;
        console.log(`The amount of the tip is ${tip} and the total bill is ${bill}`)
    }
}

TipAmount()



// Exercise 9 : Vacations Costs

function hotelCost(){
    let night = (prompt('How many nights would you like to stay in the hotel'));
    if ( isNaN(+night) || night==="" ){
        return hotelCost()
    }else{
        let cost = +night * 140;
        return cost
    }
}
// console.log(hotelCost())

function planeRideCost(){
    let destination = (prompt('Enter your destination')).toLowerCase();
    if ( !isNaN(+destination) || destination==="" ){
        return planeRideCost()}
        else{
            if (destination==='london'){
                return 183
            }
            else if(destination === 'paris'){
                return 220
            }else{
                return 300
            }
        }
}

// console.log(planeRideCost())

function rentalCarCost(){
    let days = (prompt('Enter number of days '));
    let rentalCost = 0;
    if ( isNaN(+days) || days==="" ){
        return rentalCarCost()
    }else{
        if(days>10){
            rentalCost = 0.95*(days*40);
            return rentalCost
        }else{
            rentalCost = days*40;
            return rentalCost
        }
    }
}

// console.log(rentalCarCost())

function totalVacationCost1(){
    let hotel = hotelCost();
    let plane = planeRideCost();
    let car = rentalCarCost();
    let total = hotel + plane + car ;
    console.log(`The car cost: ${car}$, the hotel cost: ${hotel}$, the plane tickets cost: ${plane}$ so the total cost : ${total}$`)
}

// totalVacationCost1()


//BONUS

function hotelCost2(night){
    let cost = +night * 140;
    return cost    
}

function planeRideCost2(destination){
    if (destination==='london'){
        return 183
    }else if(destination === 'paris'){
        return 220
    }else{
        return 300
                }
        
}


function rentalCarCost2(days){
    if(days>10){
        rentalCost = 0.95*(days*40);
        return rentalCost
    }else{
        rentalCost = days*40;
        return rentalCost
        
    }
}


function totalVacationCost2(){

    let q1 = prompt(('How many nights would you like to stay in the hotel'));
    hotel = hotelCost2(q1)
    let q2 = (prompt('Enter your destination')).toLowerCase()
    let plane = planeRideCost2(q2);
    let q3 = (prompt('Enter number of days '));
    let car = rentalCarCost2(q3);
    let total = hotel + plane + car ;
    console.log(`The car cost: ${car}$, the hotel cost: ${hotel}$, the plane tickets cost: ${plane}$ so the total cost : ${total}$`)
}


totalVacationCost2()

