// Exercise 1 - Favorite color
let me = ["my","favorite","color","is","blue"];
console.log(me.join(" "));

// Exercise 2 - Mixup
let str1 = "mix";
let str2 = "pod";

let newword = str2.slice(0,2) + str1.slice(2,3)+" " +str1.slice(0,2) + str2.slice(2,3);
console.log(newword)

let firstWord = "Hello"
let secondWord = "World"

let thirdword = secondWord.slice(0,4) + firstWord.slice(4,5)+" " +firstWord.slice(0,4) + secondWord.slice(4,5);
console.log(thirdword)

// Exercise 3 - Calculator
let num1 = parseInt(prompt('What is the first number?'))
let num2 = parseInt(prompt("What is the second number?"))
alert("The sum is:" + (num1 + num2) )
alert("The substract is " + (num1-num2))
alert ("The multiply is " + (num1*num2))
alert("The divide is " +(num1/num2))
