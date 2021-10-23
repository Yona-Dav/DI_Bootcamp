let table = document.getElementById("table");
for (let r=0; r<6;r++){
    let row = table.insertRow(r);
    for (let c=0;c<6;c++){
        let cell = row.insertCell(c);
    }
}


for (i=1; i<6; i++){
    table.rows[i].cells[1].innerHTML = "*";
    table.rows[i].cells[5].innerHTML = "*";
}

for (i=2; i<5;i++){
    table.rows[0].cells[i].innerHTML = "*";
}

for (i=1; i<6;i++){
    table.rows[3].cells[i].innerHTML = "*";
}