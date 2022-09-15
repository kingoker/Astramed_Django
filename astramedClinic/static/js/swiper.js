const images = document.querySelectorAll('.slider .slider-line img');
const sliderLine = document.querySelector('.slider-line');
var count = 0;
var width;

function init(){
    width = document.querySelector('.slider').offsetWidth;
    sliderLine.style.width = width * images.length + 'px';
    sliderLine.style.height = 'auto';
    images.forEach( item => {
        item.style.width = width + 'px';
    });
    rollSlider();
};
window.addEventListener("resize", init);
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
    sliderLine.style.transform = 'translate(-' + count * width + 'px)';
}