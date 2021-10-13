// Exercise 1: Random Number

// Get a random number between 1 and 100.
// Console.log all even numbers from 0 to the random number.

function randomEven(){
    let x = Math.random()*100;
    x = x.toFixed(1);
    console.log('The random number is', x);
    for ( i=0 ; i<x; i++){
        if(i%2===0){
            console.log (i)
        }
    }
}

randomEven()


// Exercise 2: Capitalized Letters

// Create a function that takes a string as an argument.
// Have the function return:
// The string but all letters in even indexes should be capitalized.
// The string but all letters in odd indexes should be capitalized.

function capitalize(word){
    let str = [];
    let word1 = word.split('');
    let word2 = word.split('');
    for (i=0; i<word1.length; i++){
        if(i%2===0){
            word1[i]=word1[i].toUpperCase();
        }else{
            word1[i]=word1[i]
        };
    }let j_word1= word1.join('');
    str.push(j_word1)
    for (i=0; i<word2.length; i++){
        if(i%2!==0){
            word2[i]=word2[i].toUpperCase();
        }else{
            word2[i]=word2[i]
        }
    }let j_word2= word2.join('');
    str.push(j_word2)
    return str
}

console.log(capitalize('abcdef'))



// Exercise 3 : Is Palindrome?

// Write a JavaScript function that checks whether a string is a palindrome or not.
function isPalindrome(word){
    let s_word = word.split('');
    let r_word = s_word.reverse().join('')
    if (word === r_word){
        return "This is a palindrome"
    }else{
        return 'This is not a palindrome'
    }
}

console.log(isPalindrome('kayak'))
console.log(isPalindrome('madam'))
console.log(isPalindrome('exercise'))


// Exercise 4 : Biggest Number

// Create a function called biggestNumberInArray(arrayNumber) that takes an array as a parameter and returns the biggest number.

function biggestNumberInArray(arrayNumber){
    let biggest = 0;
    for (element of arrayNumber){
        if (element>biggest){
            biggest = element; 
        }else{
            biggest = biggest
        }
    }return biggest

    }

console.log(biggestNumberInArray([-1,0,3,100, 99, 2, 99]))
console.log(biggestNumberInArray(['a', 3, 4, 2]))
console.log(biggestNumberInArray([]))


// Exercise 5: Unique Elements

// Write a JS function that takes an array and returns a new array with only unique elements.

function uniqElement(array){
    let array2 = array
    for (i=0; i<array2.length; i++){
        for (j=0; j<array2.length; j++){
            if(array2[j]=== array2[i] && j!==i){
               array2.splice(j,1)
        
            }
        }

    }return array2
  
}

console.log(uniqElement([1,2,3,3,2,3,3,4,5]))

//Other solution
// function uniqElement(array){
//     let newList = [];
//     for (i=0; i<array.length; i++){
//         if (newList.indexOf(array[i])===-1 ){
//             newList.push(array[i]);
//         }
//     }
//     return newList
// }
