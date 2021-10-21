
// Create an array which value is the planets of the solar system.
let planets = ['Mercury', 'Venus', 'Earth', 'Mars','Jupiter','Saturn','Uranus','Neptune'];

let section = document.body.firstElementChild;

let colors =['green','purple','blue','red','orange','yellow','pink','brown']

let moon =[0,0,1,2,79,82,27,14]

function solar_systeme(){
    for (let i=0; i<planets.length; i++){
        let newDiv = document.createElement('div');
        let newText = document.createTextNode(planets[i]);
        newDiv.append(newText);
        newDiv.classList.add('planet');
        newDiv.classList.add(planets[i]);
        section.append(newDiv);
        newDiv.style.color ='white';
        newDiv.style.backgroundColor = colors[i];  

        for(let j=0; j< moon[i];j++){
            let moonDiv = document.createElement('div');
            moonDiv.classList.add('moon');
            newDiv.append(moonDiv);
        }
    }
}

solar_systeme()


