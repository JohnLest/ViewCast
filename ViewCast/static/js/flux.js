var list_image = [];
var timer = 1;
function create_image(src, position, time){
    let dict = {
        src: src,
        position: position,
        time: time
    };
    list_image.push(dict);
}

function slide() {
    var image = document.getElementById('visible');
    var counter = 0;
    var seconde = 0;
    if (counter < list_image.length) {
        setInterval(function () {
            let _image = list_image[counter]
            image.id = _image.id;
            image.src = _image.src;
            timer = _image.time;
            console.log(image.src)
            console.log(counter)

            if (seconde < _image.time)
            {seconde ++;}
            else {
                counter++;
                seconde = 0;
            }
            if (counter === list_image.length) {
                counter = 0;
            }
        }, 1000);
    }
}