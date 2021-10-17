allBooks = [
    {
        title: "Tell No One",
        author:"Harlan Coben",
        image: "https://upload.wikimedia.org/wikipedia/en/a/a8/Tell_No_One_%28novel%29.jpg",
        alreadyRead:true
    },
    {
        title: "The Innocent",
        author:"Harlan Coben",
        image: "https://cdn.shopify.com/s/files/1/0517/5915/3314/products/0619365.jpg?v=1627435022",
        alreadyRead:false
    }
]

let div = document.querySelector(".listBooks");
let newTable = document.createElement('table');
div.append(newTable);



let newRow = document.createElement('thead');
newTable.appendChild(newRow)
for (let j in allBooks[1]){
    let newD = document.createElement('th');
    let newText = document.createTextNode(j);        
    newD.append(newText);
    newRow.appendChild(newD)}


for (let i in allBooks){
    let newRow = document.createElement('tr');
    newTable.appendChild(newRow)
    for (let j in allBooks[i]){
        let newD = document.createElement('td');
        let newText = document.createTextNode(allBooks[i][j]);
        newD.append(newText);
        newRow.appendChild(newD)}
}

let tr = document.getElementsByTagName('tr');

for (let i=0 ; i<allBooks.length; i++){
    let tdimg = tr[i].children[2];
    let img = document.createElement('img');
    img.setAttribute('src', allBooks[i]['image']);
    img.setAttribute('width',"100")
    tdimg.innerHTML = '';
    tdimg.appendChild(img);    
}


for (let i=0 ; i<allBooks.length; i++){
    if (allBooks[i]["alreadyRead"]===true){
        tr[i].style.color = "red"
    }
}