function volumeSphere(){
    event.preventDefault();
    let volume=0;
    let inputRadius = document.getElementById('radius');
    let radiusValue = inputRadius.value;
    radiusValue = Math.abs(radiusValue);
    volume = (4/3)*Math.PI*Math.pow(radiusValue, 3);
    volume = volume.toFixed(2);
    let inputVolume = document.getElementById('volume');
    inputVolume.value = volume;
    return false;
}

let calculForm = document.forms[0];
calculForm.addEventListener('click', volumeSphere)
