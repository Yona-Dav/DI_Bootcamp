// Prompt the user for several words (separated by commas).
let words = prompt(('Enter several words separated by commas'));

// Put the words into an array.
wordsArray = words.split(',');
console.log(wordsArray)


// Console.log the words one per line, in a rectangular frame as seen below.

let largest ='';
let number = 0;

function longestword(warray){
    for (let i=0; i<warray.length; i++) {
        if (warray[i].length>largest.length){
            largest = warray[i];  
            number = largest.length 
        }
    }return number
}

console.log(longestword(wordsArray))


let space = [];

function rectangularFrame(wordList){
    console.log("*".repeat(longestword(wordList)+4))
    for (let i=0; i<wordList.length; i++){
        if (wordList[i].length<longestword(wordList)){
            space[i] = longestword(wordList) - wordList[i].length;
            console.log('* '+wordList[i]+ " ".repeat(space[i])+' *');

        }else{
            console.log('* '+wordList[i]+' *')
        }
    }console.log("*".repeat(longestword(wordList)+4))
}

rectangularFrame(wordsArray)

// Hello,World,in,a,frame
