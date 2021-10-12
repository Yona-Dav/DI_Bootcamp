// Exercise 1 : Checking The BMI

// Create two objects, each object should hold a persons details. Here are the details:


let person1 = {
    FullName : 'Lea Smith',
    Mass: 50 ,
    Height:160,
    BMI: BMI(50,160)
}

let person2 = {
    FullName : 'David Smith',
    Mass: 85 ,
    Height:175,
    BMI: BMI(85,175)
}

function BMI(weight,height){
    return (weight / ((height * height) 
    / 10000)).toFixed(2)
}

function compare(weight1,height1,weight2,height2){
    let BMI1 = (weight1 / ((height1 * height1) 
    / 10000)).toFixed(2);
    let BMI2 = (weight2 / ((height2 * height2) 
    / 10000)).toFixed(2);
    if (BMI1>BMI2){
        return person1['FullName']
    }else if(BMI1<BMI2){
        return person2['FullName']
    }

}

console.log(compare(person1['Mass'],person1['Height'],person2['Mass'],person2['Height']))


// Exercise 2 : Grade Average


// In this exercise we will be creating a function which takes an array of grades as an argument and will console.log the average.

// Create a function called findAvg(gradesList) that takes an argument called gradesList.
// Your function must calculate and console.log the average.
// If the average is above 65 let the user know they passed
// If the average is below 65 let the user know they failed and must repeat the course.


// In one function

function findAvge(gradesList){
    let total =0;
    for (let element of gradesList){
        total += element;
        
    }
    let avg = total/gradesList.length;
    if (avg>=65){
        return 'You passed'
    }else{
        return 'You failed and you must repeat the course'
    }
    
}

console.log(findAvge([85,90,80,70,93]))




// Bonus Try and split parts 1,2 and 3,4 of this exercise to two separate functions.

function findAvg(gradesList){
    let total =0;
    for (let element of gradesList){
        total += element;
        
    }
    let avg = total/gradesList.length;
    return avg}

function Passed(avg){
    if (avg>=65){
        return 'You passed'
    }else{
        return 'You failed and you must repeat the course'
            }
}

console.log(Passed(findAvg([85,90,80,70,93])))
