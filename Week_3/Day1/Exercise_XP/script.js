// Exercise 1 : Change The Navbar

//  <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>


// In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.
let navBar = document.getElementById('navBar');
navBar.setAttribute('id', 'socialNetworkNavigation');


// We are going to add a new <li> to the <ul>.
let newLi = document.createElement("li");
let newText = document.createTextNode("Logout");
newLi.appendChild(newText);
let ulParent = document.querySelector('ul');
ulParent.appendChild(newLi);


// Bonus
// Use the firstElementChild and the lastElementChild properties to retrieve the first and last li elements from their parent element (ul). Display the text of each link. (Hint: use the textContent property).
let ulElements = document.getElementsByTagName('ul');
for (i of ulElements){
    console.log(i.firstElementChild.textContent);
    console.log(i.lastElementChild.textContent)
}

