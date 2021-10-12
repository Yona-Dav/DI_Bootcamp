const numbers = [5,0,9,1,7,4,2,6,3,8];

// Using the .toString() method convert the array to a string.
numbersStr = numbers.toString();
console.log(numbersStr);

// Using the .join()method convert the array to a string. Try passing different values into the join.
numberStr2 = numbers.join(',');
console.log(numberStr2)


// Bonus : To do this Bonus look up how to work with nested for loops
// Sort the numbers array in descending order, do so using for loops (Not using built-in sort methods).
// The output should be: [9,8,7,6,5,4,3,2,1,0]

let swap = numbers;

for (let i=1; i<swap.length; i++){
    for(let l=0; l<i; l++){
        if ( swap[i]>swap[l]){
            let x = swap[i];
            swap[i]=swap[l];
            swap[l]=x;
        }
    }
        
}
console.log(swap)




