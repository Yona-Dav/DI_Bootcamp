// Exercise 1 : Is_Blank

// Write a program to check whether a string is blank or not.
function isBlank(word){
    if (word==='' || word.length ===0){
        return 'True'
    }else{
        return 'False'
    }
}

console.log(isBlank(''))
console.log(isBlank('abc'))


// Exercise 2 : Abbrev_name

// Write a JavaScript function to convert a string into an abbreviated form.

function abbrevName(name){
    let s_name = name.split(' ');
    if (s_name.length>1){
        return(s_name[0]+" "+s_name[1].charAt(0)+'.')
    }else{
        return s_name.charAt(0)+'.'
    }
}

console.log(abbrevName("Robin Singh"))

// Exercise 3 : SwapCase

// Write a JavaScript function which takes a string as an argument and swaps the case of each character.
function swapCase(sentence){
    let s_sentence = sentence.split('');
    for(i=0; i<s_sentence.length; i++){
        if (s_sentence[i] === s_sentence[i].toLowerCase()){
            s_sentence[i]= s_sentence[i].toUpperCase()
        }else{
            s_sentence[i]= s_sentence[i].toLowerCase()
        }
    }let j_sentence = s_sentence.join('')
    return j_sentence
}

console.log(swapCase('The Quick Brown Fox'))



// Exercise 4 : Omnipresent Value

// Create a function that determines whether an argument is omnipresent for a given array.

function isOmnipresent(sub, value){
    let res =0;
    for (i=0; i<sub.length; i++){
        if (sub[i].includes(value)){
            res +=1;
        }
    
    }if (res === sub.length){
        return 'True'
    }else{
        return 'False'
    }

}


console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1))
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6))