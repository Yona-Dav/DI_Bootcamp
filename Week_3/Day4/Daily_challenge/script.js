
let toDoForm = document.forms[0]
toDoForm.addEventListener('submit', addTask);

let listTasks = [];


let div = document.getElementsByClassName('listTasks')[0];
let ul = document.createElement('ul');
ul.setAttribute('id','myList');
div.appendChild(ul);

// function addTask (event) {
// 	event.preventDefault();
// 	let inputList= event.target.elements.list

// 	let listValue = inputList.value;
//     

//     if(listValue===""||listValue.length===0){
//         alert('Enter text');
//         return addTask()
//     }else{
//         listTasks.push(listValue);
//         let newList = document.createElement('li')
//         ul.appendChild(newList);
//         newList.style.listStyleType='none';

//         let icon = document.createElement('i');
//         icon.classList.add('fas');
//         icon.classList.add('fa-times-circle');
//         newList.appendChild(icon);

//         let newInput =document.createElement('input');
//         newInput.setAttribute('type','checkbox');
//         newList.appendChild(newInput);
        
//         let newTask = document.createElement('label');
//         let newText = document.createTextNode(listValue);
//         newTask.appendChild(newText);
//         newList.appendChild(newTask);

        
//     }

//     inputList.value="";

// }



//// BONUS

let count = 0;

function addTask (event) {
	event.preventDefault();
	let inputList= event.target.elements.list

	let listValue = inputList.value;
    

    if(listValue===""||listValue.length===0){
        alert('Enter text');
        return addTask()
    }else{
        let listObject = {task_id : count,
            text: listValue,
            done: false
        }
        listTasks.push(listObject);
        let newList = document.createElement('li');
        newList.classList.add('newli');
        ul.appendChild(newList);
        newList.style.listStyleType='none';

        let icon = document.createElement('i');
        icon.classList.add('fas');
        icon.classList.add('fa-times-circle');
        icon.setAttribute('data-task-id', count);
        icon.addEventListener('click', deleteTask);
        newList.appendChild(icon);

        let newInput =document.createElement('input');
        newInput.setAttribute('type','checkbox');
        newInput.setAttribute('data-task-id', count);
        newInput.classList.add('newTask');
        newInput.addEventListener('change', doneTask)
        newList.appendChild(newInput);
        
        let newTask = document.createElement('label');
        newTask.classList.add('element');
        newTask.setAttribute('data-task-id', count);
        newTask.addEventListener('click', showId);
        let newText = document.createTextNode(listValue);
        newTask.appendChild(newText);
        newList.appendChild(newTask);
        
        let newline = document.createElement('hr');
        newList.appendChild(newline);

        count++

        
    }

    inputList.value="";

}

function showId(event){
    let numId = event.target.getAttribute("data-task-id");
  alert("The id of " + event.target.innerHTML + " is " + numId);
}

function doneTask(event){
    let numId = event.target.getAttribute("data-task-id");
    if (this.checked){
        listTasks[numId]['done'] = true;
        let label = document.getElementsByClassName('element')[numId];
        label.style.color = 'red';
        label.style.textDecoration= 'line-through';
    }
}


// /// BONUS 2
function deleteTask(event){
    let numId = event.target.getAttribute("data-task-id");
    let li = document.getElementsByClassName('newli')[numId];
    ul.removeChild(li);
}

let clear = document.createElement('button');
let text = document.createTextNode('Clear');
clear.classList.add('clear');
clear.appendChild(text);
div.append(clear);

clear.addEventListener('click', clearAll);

function clearAll(){
    let li = document.getElementsByClassName('newli');
    ul.remove(li);
}


