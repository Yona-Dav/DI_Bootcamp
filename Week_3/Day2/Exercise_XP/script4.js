let div = document.body.firstElementChild

let newButton = document.createElement('button');
let newText = document.createTextNode('Click me!');
newButton.appendChild(newText);
div.appendChild(newButton);

let button = div.firstElementChild;

button.addEventListener("click", function (){
	document.body.style.backgroundColor="blue"
})

button.addEventListener('mouseover', function(){
    button.style.fontSize = "50px"
})

button.addEventListener('mouseout', function(){
    button.style.fontSize = "10px"
})

button.addEventListener('contextmenu', function(){
    alert('You right clicked')
})

button.addEventListener('dblclick', function(){
    button.style.color = 'red'
})

