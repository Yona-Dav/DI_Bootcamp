// by using a loop
let pattern='';
for (let i=1; i<7;i++){
    pattern += '* '.repeat(i)+'\n'
}
console.log(pattern)


// by using nested for loops
let star = '';
for (let j=1 ; j<7 ; j++){
    for (let k=0 ; k<j ; k++){
        star += '* ';
    }
    star += '\n';
}
console.log(star);
