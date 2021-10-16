// Player 1

let word = "";
let stars ="";

function checkWord(){
    word = prompt('Enter a word (min 8 letters)').toLowerCase();
    if (!isNaN(word) || word.length<8){
        return checkWord();
    }else{
        stars = "*".repeat(word.length);
        console.log(stars)
    }
}

// Player 2

let letters = [];
let count = 0;
let l ="";

function guessLetter(){
    l = prompt("Enter a letter").toLowerCase();
    if(l.length!==1 || l===null || !isNaN(l)) {
        alert("It is not a letter, try again")
        return guessLetter()
    }else{
        letters.push(l);
        console.log(letters);
        return guessWord()
    }
}   

function guessWord(){
    if (word.indexOf(l)!==-1 && word.lastIndexOf(l)!==-1 && word.indexOf(l)!==word.lastIndexOf(l)){
        let s_stars = stars.split('');
        s_stars.splice(word.indexOf(l),1,l);
        s_stars.splice(word.lastIndexOf(l),1,l);
        let j_stars = s_stars.join('');
        stars = j_stars
        console.log(stars);
        return findWord();
    }else if (word.indexOf(l)!==-1){
        let s_stars = stars.split('');
        s_stars.splice(word.indexOf(l),1,l);
        let j_stars = s_stars.join('');
        stars = j_stars
        console.log(stars);
       return findWord();
    }else{
        return numLifes();
    }         
    
 }

function findWord(){
    if(stars === word){
        console.log("YOU WIN");
        letters = [];
        return checkWord();
    }else{
    return guessLetter()}
}

function numLifes(){
    count ++;
    console.log(`You have ${10-count} chance(s) left`);
    if((10-count)===0){
        console.log("Player 2:YOU LOSE \n Player 1: CONGRATS YOU WIN");
        console.log('The word was', word);
        letter = [];
        return checkWord();
    }else{
        console.log(stars);
        return guessLetter();
    }   
}
