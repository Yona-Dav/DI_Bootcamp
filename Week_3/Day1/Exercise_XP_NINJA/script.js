function createCalendar(year, month){
    
    let firstDay = (new Date(year, month-1)).getDay();
    let numberOfDays = (new Date(year, month,0)).getDate();


    let days = ['MO','TU','WE','TH','FR','SA','SU'];

    let table = document.createElement('table');
    let body = document.body;
    body.appendChild(table);
    let thead = document.createElement('thead');
    table.appendChild(thead)

    for(let i of days){
        let newDay = document.createElement('th');
        let newText = document.createTextNode(i);        
        newDay.appendChild(newText);
        thead.appendChild(newDay)
    }

    let date=1;
    for (let i=0; i<6; i++){
        let newRow = document.createElement('tr');
        for (let j=0; j<7; j++){
            let startingDay = firstDay == 0 ? 7 : firstDay;
            if (i===0 && j<startingDay-1){
                let newCell = document.createElement('td');
                let newText = document.createTextNode('-');
                newCell.appendChild(newText);
                newRow.appendChild(newCell);
            }else if (date>numberOfDays){
                break;
            }else{
                let newCell = document.createElement('td');
                let newText = document.createTextNode(date);
                newCell.appendChild(newText);
                newRow.appendChild(newCell);
                date++
            }
    }
        table.appendChild(newRow)

}
let td = document.getElementsByTagName('td');
for (let x of td){
    x.style.borderColor = "black"
}
}

createCalendar(2012, 9)