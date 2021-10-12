// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”. For example, “The movie is not that bad, I like it”.

let sentence = 'This dinner is not that bad ! You cook well';

// Create a variable called wordNot where it’s value is the first appearance of the substring “not” (from the sentence variable).

let wordNot = sentence.indexOf("not");
console.log(wordNot);

// Create a variable called wordBad where it’s value is the first appearance of the substring “bad” (from the sentence variable).
let wordBad = sentence.indexOf("bad");
console.log(wordBad);

// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
if (wordNot < wordBad && wordNot!==-1 && wordBad!==-1){
console.log(`${(sentence.substr(0, wordNot))} good ${(sentence.substr(wordBad+3, sentence.length))} `)
}else {
    console.log(sentence)
}
