

//#region numeros incrementando
function startIncrementData(){
    let valueDisplays = document.querySelectorAll(".num");
    let interval = 5000;

    valueDisplays.forEach((valueDisplays) => {

        let startValue = 0;
        let endValue = parseInt(valueDisplays.getAttribute("data-val"));
        let duration = Math.floor(interval/endValue);
    
        let counter = setInterval(function(){
            startValue +=2;
            valueDisplays.textContent = startValue + "+";
    
            if (startValue == endValue){
                clearInterval(counter);
            }
        }, duration
    )
    })
}
//#endregion

//#region revelar contenido
let incrementExecuted = false;

window.addEventListener('scroll', reveal);

window.addEventListener('scroll', reveal2);

function reveal(){

    var reveals = document.querySelectorAll('.reveal');

    for (var i = 0; i < reveals.length; i++){

        var windowHeight = window.innerHeight;
        var revealtop = reveals[i].getBoundingClientRect().top;
        var revealPoint = 150;

        if (revealtop < windowHeight - revealPoint){
            reveals[i].classList.add('activate');
            if (!incrementExecuted) {
                startIncrementData();
                incrementExecuted = true;
            }
        }
        else{
            reveals[i].classList.remove('activate');
        }
    }
}

function reveal2(){

    var reveals = document.querySelectorAll('.reveal2');

    for (var i = 0; i < reveals.length; i++){

        var windowHeight = window.innerHeight;
        var revealtop = reveals[i].getBoundingClientRect().top;
        var revealPoint = 150;

        if (revealtop < windowHeight - revealPoint){
            reveals[i].classList.add('activate');
            if (!incrementExecuted) {
                startIncrementData();
                incrementExecuted = true;
            }
        }
        else{
            reveals[i].classList.remove('activate');
        }
    }
}
//#endregion