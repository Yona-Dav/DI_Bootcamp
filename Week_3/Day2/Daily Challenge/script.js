// Daily Challenge: Tell The Story

let input = document.getElementsByTagName('input');
let listWord = [];
let span = document.getElementsByTagName('span')[0];

function getValues(){
    listWord = [];
    span.innerText = "";
    for (let i=0; i<input.length; i++){
        let idName = input[i].id;
        let inputName = document.getElementById(idName);
        let nameValue = inputName.value;
        if ( nameValue.length ===0 ){
            alert("Please fill all the blank");
        return getValues;}
        listWord.push(nameValue);
        
        inputName.value="";
        
    }
    if (listWord.length===5){
        
        let newText = document.createTextNode(`In the ${listWord[4]}, ${listWord[2]} , a ${listWord[1]} person , ${listWord[3]} on a ${listWord[0]}`);
        span.appendChild(newText);
        return listWord;
      }
}




let button = document.getElementsByTagName("button")[0];
button.addEventListener('click',getValues)




// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly.

let newButton = document.createElement('button');
newButton.classList.add('shuffle');
let newText = document.createTextNode("Change the text");
newButton.appendChild(newText);
let parag = document.getElementsByTagName('p')[0];
parag.appendChild(newButton);

function shuffle() {
    span.innerText = '';
    for (let i = story.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        let x = story[i];
        story[i] = story[j];
        story[j] = x;
        span.innerText= x;
    }
}
let story = [`One day, ${listWord[2]} in a ${listWord[4]} ${listWord[3]} and saw a ${listWord[1]} ${listWord[0]}`, `Today I and my ${listWord[1]} ${listWord[0]} were ${listWord[3]} about ${listWord[2]} in a ${listWord[4]}`, `In the ${listWord[4]}, ${listWord[2]} , a ${listWord[1]} person , ${listWord[3]} on a ${listWord[0]}`, `In the ${listWord[4]}, ${listWord[2]} , a ${listWord[1]} person , ${listWord[3]} on a ${listWord[0]}`];




let shufButton = document.getElementsByClassName('shuffle')[0];
shufButton.addEventListener('click', shuffle)


