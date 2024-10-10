const questionsSection = document.querySelector('.questions__section')
const questions = document.querySelector('.questions')

function getCookie(name){
    let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

function setActiveElement(current){
    Array.from(questionsSection.children).forEach(item => item.classList.remove('section__item__active'))
    current.add('section__item__active')
}
function addAllContainer(){    
    fetch('api/questions')
    .then(response => response.json())
    .then(result => {
        document.querySelector('.form__content').replaceChildren()
        result.forEach(question => {
            document.querySelector('.form__content').innerHTML += `
            <div class="all_question__container">
                <div class="all_question">
                    <span class="all_question__label">Вопрос:</span>
                    <p class="all_question__name">${question.author}: <span class="all_question__text">${question.question}</span></p>
                </div>
                <div class="all_answer">
                    <span class="all_question__label">Ответ:</span>
                    <p>${question.answer}</p>
                </div>
            </div>`
        })
    })
}

function addAskContainer(){
    const script = document.createElement('script')
    script.src = "https://www.google.com/recaptcha/api.js"
    script.acync = false    
    document.querySelector('.form__content').innerHTML = `
        <div class="ask_question__container">
            <div class="ask_question__field__container">
                <input
                autoComplete='off'
                name='author'
                class="ask_question__field"
                type="text"
                placeholder=''
                required
                minlength=3/>
                <label class="ask_question__label" for="name">Ваше имя</label>
            </div>
            <div class="ask_question__field__container">
                <input
                autoComplete='off'
                name='question'
                class="ask_question__field"
                type="text"
                placeholder=''
                required
                minlength=10/>
                <label class="ask_question__label" for="question">Ваш вопрос</label>
            </div>
            <div class="g-recaptcha" id="block_captcha" data-sitekey="6LdE8VkqAAAAACaFdloFag5VZUVEGavkkGcz62uh"></div>
            <button class="ask_question__button" type="submit">Задать</button>
            <p class="ask_question__message"></p>
        </div>`
        document.body.appendChild(script)
}

questions.addEventListener('click', (e) => {
    const current = e.target.classList
    if(current.contains('section__item') && !current.contains('section__item__active')){
        setActiveElement(current)
        if(e.target.id === 'ask'){
            addAskContainer()
        }
        else{
            addAllContainer()
        }
    }
})
document.addEventListener('submit', (e) => {
    e.preventDefault()
    if(form.reportValidity()){
        if(grecaptcha.getResponse()){
            fetch('api/create_question', {method: 'post', body: new FormData(e.target)})
            .then(response => response.json())
            .then(result => {
                if(result === 'success'){
                    document.querySelector('.ask_question__message').textContent = 'Спасибо за вопрос, он появится в общем списке, как только владелец на него ответит'
                    form.reset()
                    grecaptcha.reset()
                }
            })
        }
    }
})