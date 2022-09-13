const images = document.querySelectorAll('.slider-line img');
const sliderLine = document.querySelector('.slider-line');
var count = 0;
var width;

function init(){
    console.log('resize')
    width = document.querySelector('.slider').offsetWidth;
    console.log(width);
    sliderLine.style.width = width * images.length + 'px';
    images.forEach( item => {
        item.style.width = width + 'px';
    })
    rollSlider();
};
init();

document.querySelector('.slider-next').addEventListener('click', function(){
    count++;
    if(count >= images.length){
        count = 0;
    }
    rollSlider();
});
document.querySelector('.slider-prev').addEventListener('click', function(){
    count--;
    if(count < 0 ){
        count = images.length-1;
    }
    rollSlider();
});


function rollSlider(){
    sliderLine.style.transform = 'translate(-'+count*width+'px';
}