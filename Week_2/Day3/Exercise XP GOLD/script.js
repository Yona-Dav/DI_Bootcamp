// Exercise 1 : Building Management

let building = {
    numberLevels : 4,
    numberOfAptByLevel : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
}


// Console.log the number of levels in the building.
console.log(building['numberLevels']);
//console.log(Object.keys(building['numberOfAptByLevel']).length)


// Console.log how many apartments are on levels 1 and 3.
console.log(building['numberOfAptByLevel']['1']);
console.log(building['numberOfAptByLevel']['3']);

// Console.log the name of the second tenant and the number of rooms he has in his apartment.
console.log(`The name of the second tenant is ${building['nameOfTenants'][1]} and he has ${building['numberOfRoomsAndRent']['Dan'][0]} rooms`)

// Check if the sum of Sarah and David’s rent is bigger than Dan’s rent.
rent1 = building['numberOfRoomsAndRent']['Sarah'][1] + building['numberOfRoomsAndRent']['David'][1];
console.log(rent1)

// If it is than increase Dan’s rent.

if (rent1 > building['numberOfRoomsAndRent']['Dan'][1]) {
    building['numberOfRoomsAndRent']['Dan'][1] = rent1;
    console.log(`The new rent of Dan is ${building['numberOfRoomsAndRent']['Dan'][1]}`);

}else{
    console.log('The rent is inchanged')
}



// Exercise 2 : Divisible By Three

let numbers = [123, 8409, 100053, 333333333, 7]

// Loop through the array above and determine whether or not each number is divisible by three.
// Each time you loop console.log “true” or “false”.

for (let element of numbers){
    if (element%3===0){
        console.log('True for' , element)
    }else{
        console.log('False for', element)
    }
}


// Exercise 3 : Playing With Numbers

let age = [20,5,12,43,98,55];

// 1. Console.log the sum of all the numbers in the age array.
let sum = 0;
for (element of age){
    sum+=element;
}
console.log(sum)


// 2. Console.log the largest age in the array.
let largest =0;
for (element of age){
    if (element > largest){
        largest = element;
    }else{
        largest = largest
    }
}
console.log(largest)