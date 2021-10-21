// write some Javascript code to color all diagonal table cells in red.

let table = document.body.firstElementChild;
for (i=0; i<table.rows.length; i++){
    let row = table.rows[i];
    let cell = row.cells[i];
    cell.style.backgroundColor = 'red'

}