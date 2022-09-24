//Запрет на копирование
document.ondragstart = noselect;
document.onselectstart = noselect;
function noselect() {return false;}


// Поиск
const icon = document.querySelector('.search__icon');
const search = document.querySelector('.search');
icon.onclick = function(){
    search.classList.toggle('search__active');
}
document.addEventListener( 'click', (e) => {
    const click = e.composedPath().includes(search);
	if ( !click ) {
		search.classList.remove('search__active');
	}
})



// Бергер меню
const iconMenu = document.querySelector('.menu__burger');
const menuBody = document.querySelector('.header__body');
const menuItem = document.querySelectorAll('.header__link');

if(iconMenu){
    iconMenu.addEventListener("click", function(e){
        document.body.classList.toggle('lock');
        iconMenu.classList.toggle('active');
        menuBody.classList.toggle('active');
    });
    menuItem.forEach(item => {
        item.addEventListener('click', event => {
            document.body.classList.remove('lock');
            iconMenu.classList.remove('active');
            menuBody.classList.remove('active');
        })
    })
}

// Карусель
if(document.querySelector('.swiper')){
    var swiper = new Swiper(".swiper", {
        loop: true,
        slidesPerView: 1,
        spaceBetween: 50,
        navigation: {
            nextEl: ".next__icon",
            prevEl: ".prev__icon",
          },
          breakpoints:{
            450:{
                slidesPerView: 2,
            },
            690:{
                slidesPerView: 2,
            }
          }
    });
}

// Расскрывающийся список
if(document.querySelector('.accordion')){
    const accordingLink = document.querySelector('.according__link');
        const accordion = document.querySelector('.accordion');
        accordingLink.onclick = function(){
            accordion.classList.toggle('accordion-active');
    }
}

//Скролл на странице блога остаётся на месте
if(document.querySelector('.blog__categories')){
    let cords = ['scrollX','scrollY'];
    window.addEventListener('unload', e => cords.forEach(cord => localStorage[cord] = window[cord]));
    window.scroll(...cords.map(cord => localStorage[cord]));
}