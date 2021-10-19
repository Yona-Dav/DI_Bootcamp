// // Exercise 1 : Change The Article
// Using DOM methods, remove the last paragraph in the <article> tag from the DOM.
let article = document.getElementsByTagName('article')[0];
let lastP = article.lastElementChild;
article.removeChild(lastP);

// Add an event listener which will change the background color of the h2 tag from the DOM when clicked on.
let h2 = document.getElementsByTagName("h2")[0];
h2.addEventListener('click', function(){
    h2.style.backgroundColor = 'red'
})

// Set the font size of the h1 tag to a random pixel size between 0 to 100.(Check out this documentation)
let h1 = document.getElementsByTagName("h1")[0];
let size = (Math.random()*100).toFixed(0)
h1.style.fontSize =`${size}px`;

// Add an event listener which will hide the h3 when it’s clicked on (use the display property).
let h3 = document.getElementsByTagName("h3")[0];
h3.addEventListener('click', function(){
    h3.style.display = 'none';
})

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
let newButton = document.createElement('button');
let newText = document.createTextNode('bold');
newButton.appendChild(newText);
newButton.classList.add('btn');
article.appendChild(newButton);

let allP = document.getElementsByTagName('p');
newButton.addEventListener("click", boldText)

function boldText(){
    for (let i of allP){
        i.style.fontWeight = "bold";

    }
}


// When the “Submit” button of the form is clicked:
// get the values of the input tags
// make sure that they are not empty,
// then append them to a HTML table, in the div, below the form.

let formDetails = document.forms[0]
let table = document.createElement('table');
let div = document.getElementsByClassName("usersAnswer")[0];
div.appendChild(table);
let thead =document.createElement('thead');
let th1 = document.createElement('th');
let th1text = document.createTextNode('First name');
th1.appendChild(th1text);
let th2 = document.createElement('th');
let th2text = document.createTextNode('Last name');
th2.appendChild(th2text);
table.appendChild(thead);
thead.appendChild(th1);
thead.appendChild(th2);

function addInfo(event){
    event.preventDefault();

    let inputFname = event.target.elements.fname;
    let inputLname = event.target.elements.lname;
    
    let fnameValue = inputFname.value;
    let lnameValue = inputLname.value;
    if ( fnameValue.length ===0 || lnameValue.length ==0){
        alert("Please enter a value");
        return;
    }
    let tr = document.createElement('tr');
    table.appendChild(tr);

    let td1 = document.createElement('td');
    let td1Text = document.createTextNode(fnameValue);
    td1.appendChild(td1Text);
    let td2 = document.createElement('td');
    let td2Text = document.createTextNode(lnameValue);
    td2.appendChild(td2Text);
    tr.appendChild(td1);
    tr.appendChild(td2);

    inputFname.value='';
    inputLname.value='';

}

formDetails.addEventListener("submit",addInfo)

// When you hoover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

let secondParag = allP[1];
secondParag.addEventListener('mouseover', function(){
    secondParag.style.opacity = "1"
})

secondParag.addEventListener('mouseout', function(){
    secondParag.style.opacity = "0.5"
})

