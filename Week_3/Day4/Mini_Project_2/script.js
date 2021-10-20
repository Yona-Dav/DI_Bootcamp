let audios = ['sounds_boom.mp3','sounds_clap.mp3','sounds_hihat.mp3','sounds_kick.mp3','sounds_openhat.mp3','sounds_ride.mp3','sounds_snare.mp3','sounds_tink.mp3','sounds_tom.mp3']

let buttons = document.getElementsByTagName('button');

for (i=0; i<buttons.length; i++){
    let audio = new Audio(audios[i]);
    buttons[i].addEventListener('click', function(){
        audio.play();
    })
}

document.body.addEventListener('keydown', playMusic);
document.body.addEventListener('keyup', stopPlay);

function playMusic(event){
    let letter = event.keyCode;
    
    if(letter === 65){
        let audio = new Audio(audios[0]);
        audio.play();
        buttons[0].style.boxShadow = "10px 10px 20px 20px gold" ;
        buttons[0].style.transform = 'scale(1.1)';
    }else if(letter === 83){
        let audio = new Audio(audios[1]);
        audio.play();
        buttons[1].style.boxShadow = "10px 10px 20px 20px gold" ;
        buttons[1].style.transform = 'scale(1.1)';
    }else if(letter === 68){
        let audio = new Audio(audios[2]);
        audio.play();
        buttons[2].style.boxShadow = "10px 10px 20px 20px gold" ;
        buttons[2].style.transform = 'scale(1.1)';
    }else if (letter === 70){
        let audio = new Audio(audios[3]);
        audio.play();
        buttons[3].style.boxShadow = "10px 10px 20px 20px gold" ;
        buttons[3].style.transform = 'scale(1.1)';
    }else if (letter === 71){
        let audio = new Audio(audios[4]);
        audio.play();
        buttons[4].style.boxShadow = "10px 10px 20px 20px gold" ;
        buttons[4].style.transform = 'scale(1.1)';
    }else if (letter === 72){
        let audio = new Audio(audios[5]);
        audio.play();
        buttons[5].style.boxShadow = "10px 10px 20px 20px gold" ;
        buttons[5].style.transform = 'scale(1.1)';
    }else if (letter === 74){
        let audio = new Audio(audios[6]);
        audio.play();
        buttons[6].style.boxShadow = "10px 10px 20px 20px gold" ;
        buttons[6].style.transform = 'scale(1.1)';
    }else if (letter === 75){
        let audio = new Audio(audios[7]);
        audio.play();
        buttons[7].style.boxShadow = "10px 10px 20px 20px gold" ;
        buttons[7].style.transform = 'scale(1.1)';
    }else if (letter === 76){
        let audio = new Audio(audios[8]);
        audio.play();
        buttons[8].style.boxShadow = "10px 10px 20px 20px gold" ;
        buttons[8].style.transform = 'scale(1.1)';}
}

function stopPlay(event){
    let letter = event.keyCode;

    if(letter === 65){
        buttons[0].style.boxShadow = "none" ;
        buttons[0].style.transform = 'none';
    }else if(letter === 83){
        buttons[1].style.boxShadow = "none" ;
        buttons[1].style.transform = 'none';
    }else if(letter === 68){
        buttons[2].style.boxShadow = "none" ;
        buttons[2].style.transform = 'none';
    }else if (letter === 70){
        buttons[3].style.boxShadow = "none" ;
        buttons[3].style.transform = 'none';
    }else if (letter === 71){
        buttons[4].style.boxShadow = "none" ;
        buttons[4].style.transform = 'none';
    }else if (letter === 72){
        buttons[5].style.boxShadow = "none" ;
        buttons[5].style.transform = 'none';
    }else if (letter === 74){
        buttons[6].style.boxShadow = "none" ;
        buttons[6].style.transform = 'none';
    }else if (letter === 75){
        buttons[7].style.boxShadow = "none" ;
        buttons[7].style.transform = 'none';
    }else if (letter === 76){
        buttons[8].style.boxShadow = "none" ;
        buttons[8].style.transform = 'none';}
}