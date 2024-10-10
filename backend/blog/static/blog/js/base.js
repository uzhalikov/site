const headerButton = document.querySelector('.header__button')
const closeButton = document.querySelector('.nav__close')
const nav = document.querySelector('nav')


document.addEventListener('DOMContentLoaded', (e) => {
    if(window.innerWidth < 768){
        nav.classList.add('hide', 'nav__hide', 'nav__mobile')
    }
})
window.addEventListener('resize', () => {
    const width = window.innerWidth
    if(width < 768){
        nav.classList.add('hide', 'nav__hide', 'nav__mobile')
    }
    else{
        nav.classList.remove('hide', 'nav__hide', 'nav__mobile')
    }
})
headerButton.addEventListener('click', () => {
    nav.classList.remove('hide', 'nav__hide')
})
closeButton.addEventListener('click', () => {    
    nav.classList.add('nav__hide')
})