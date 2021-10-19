// Exercise 1 : Select A Kind Of Music


// Display the value of the selected option.
let select = document.body.firstElementChild;
let selectedValue = select.value ;
console.log(selectedValue);

// Add an additional option to the select tag:
// <option value="classic">Classic</option>
let newOption = document.createElement('option');
let newText = document.createTextNode('Classic');
newOption.appendChild(newText);
newOption.setAttribute('value','classic');
select.appendChild(newOption);

// The newly added option should be selected by default.
let options = document.getElementsByTagName('option');
options[1].selected = false;
options[2].setAttribute('selected', true);