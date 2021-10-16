// 99 Bottles of Beer?

// Prompt the user for a number to begin counting down bottles.
let number = parseInt(prompt("Enter a number"));

// In the song everytime a bottle falls we subtract the bottles by 1.


function bottleBeer(){
    for (i=number; i>0 ; i--){
        if (i===1 && (number-i+1)!==1){
            console.log( "1 bottle of beer on the wall \n".repeat(2) + "1 bottle of beer" );
            console.log(`Take ${number} down, pass them around`)
        }
        else if (i===1 && (number-i+1)===1){
            console.log( "1 bottle of beer on the wall \n".repeat(2) + "1 bottle of beer" );
            console.log(`Take 1 down, pass it around`)
        }else if (i!==1  && (number-i+1)===1){
            console.log(`${i} bottles of beer on the wall \n ${i} bottles of beer on the wall \n ${i} bottles of beer `);
            console.log(`Take 1 down, pass it around`)
        }else{
            console.log(`${i} bottles of beer on the wall \n ${i} bottles of beer on the wall \n ${i} bottles of beer `);
            console.log(`Take ${number-i+1} down, pass them around`)
        }
    }
}

bottleBeer()