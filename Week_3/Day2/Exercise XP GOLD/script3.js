// Exercise 3 : Create A Shopping List

// In your js file:
// Create an empty array. For example: let shoppingList=[].
let shoppingList = [];

// Create a form containing : a text input field and an “AddItem” button. Add this form to the DOM.
let div = document.getElementById('root');
let newForm = document.createElement('form');
div.appendChild(newForm);

let newInput = document.createElement('input');
newInput.setAttribute('type', 'text');
newInput.setAttribute('id', 'item');
newInput.setAttribute('name', 'item');
newForm.appendChild(newInput);

let newButton = document.createElement('button');
newButton.setAttribute('id', 'addItem');
let newText = document.createTextNode('AddItem');
newButton.appendChild(newText);
newForm.appendChild(newButton);


// Type what you need to buy in the text input field, then add the new item to the array as soon as you click on the “AddItem” button (Hint: create a function named addItem()).
let shopForm = document.forms[0]

function addItem(){
    let inputValue = document.getElementById('item').value;shoppingList.push(inputValue);
    console.log(shoppingList);
}

let button = document.getElementById('addItem');
button.addEventListener('submit', addItem);

// Add a “ClearAll” button to the DOM, that when clicked on, should call the clearAll() function (see below).
// Create a function named clearAll() that should clear out all the items in the shopping list.

let newButton2 = document.createElement('button');
newButton2.setAttribute('id', 'ClearAll');
let newText2 = document.createTextNode('Clear All');
newButton2.appendChild(newText2);
newForm.appendChild(newButton2);

function clearAll(){
    shoppingList = [];
}

let button2 = document.getElementById('ClearAll');
button2.addEventListener('submit', clearAll);

