// Exercise 1 - Find Nemo
let nemo = prompt("Give me a sentence with the word Nemo");
nemo = nemo.toLowerCase();
nemo = nemo.split(' ');
console.log(nemo);

include = (nemo.includes('nemo'));
console.log(include);

index = nemo.indexOf('nemo');
console.log( "I find Nemo at ", index)

if (include===false) {
  console.log("I can't find Nemo")
} 

// Exercise 1 - Evaluation

// 5 >= 1  >true
// 0 === 1 >false
// 4 <= 1 >false
// 1 != 1 >false
// "A" > "B" >false
// "B" < "C" >true
// "a" > "A" >true
// "b" < "A" >false
// true === false >false
// true != true >false

console.log(5 >= 1)
console.log(0 === 1)
console.log(4 <= 1)
console.log( 1 != 1)
console.log("A" > "B")
console.log("B" < "C")
console.log("a" > "A")
console.log("b" < "A")
console.log( true === false )
console.log(true != true)

// Exercise 2 - Evaluation(2)

// let c; undefined just declaring
// let a = 34; 
// let b = 21;
// a = 2; a is now 2
// a + b 

// 1.So the outcome of a+b = 23
//2. The value of c is undefined

let c;
let a = 34;
let b = 21;
a = 2;
console.log(a + b)
console.log(c)

// 3+4+"5" = 75 because 5 is a string and not a number
console.log(3 + 4 + '5');

// Exercise 3 - Numbers
let number = prompt("Give me a string of number separated by commas");
number = number.split(",");
let res = 0;
for (let i=0; i<number.length;i++){
    if(+number[i]){
    res+= +number[i];
};
};

console.log((res));

// Exercise 4 - Boom
num = parseInt(prompt('Choose a number'));
if (num<2) {
    console.log('boom')}
else {

    if ((num%5 ===0 && num%2===0)){
        console.log(('b'+'o'.repeat(num)+'m!').toUpperCase())
    }

    else if (num%2 === 0){
        console.log('b'+'o'.repeat(num)+'m!')
    }
    
    else if (num%5 === 0){
        console.log(('b'+'o'.repeat(num)+'m').toUpperCase())
    }

    else{
        console.log('b'+'o'.repeat(num)+'m')

    }
}
