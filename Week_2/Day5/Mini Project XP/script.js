//  Fisrt Part 

function playTheGame(){
    let result = confirm("Press OK if you want to play the Game");
    if (result === true){
        return userNum();
    }else{
        alert("No problem, Goodbye")
    }
}
let computerNumber=0;

function userNum(){
    let num = parseInt(prompt('Enter a number between 0 and 10'));
    if (isNaN(num)){
        alert("Sorry, Not a number, Goodbye")
    }else if (num>10 || num<0){
        alert("Sorry, it's not a good number, Goodbye")
    }else{
        computerNumber = Math.random()*10;
        computerNumber = parseInt(computerNumber.toFixed(0));
        return test(num,computerNumber);
    }
}


// Seconde Part 

function test(userNumber,computerNumber){
    for (let step = 0; step < 3; step++){
        if(step<2){
            if (userNumber===computerNumber){
                alert('WINNER');
                return;
            }else if(userNumber>computerNumber){
                alert("Your number is bigger then the computer’s, guess again");
                userNumber = parseInt(prompt('Enter a new number'));
            }else{
                alert("Your number is smaller then the computer’s, guess again");
                userNumber = parseInt(prompt('Enter a new number'));
            }
        }else{
            alert("Out of Chances");
            return;
        }    
    }  
}

// // BONUS

// let computerNumber=0;

// function userNum(){
//     let num = parseInt(prompt('Enter a number between 0 and 10'));
//     if (isNaN(num)){
//         alert("Sorry, Not a number, Goodbye")
//         return userNum();
//     }else if (num>10 || num<0){
//         alert("Sorry, it's not a good number, Goodbye")
//         return userNum();
//     }else{
//         computerNumber = Math.random()*10;
//         computerNumber = parseInt(computerNumber.toFixed(0));
//         return test(num,computerNumber);
//     }
    
// }

