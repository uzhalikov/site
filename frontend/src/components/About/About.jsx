import styles from './About.module.css'
import { Link } from 'react-router-dom'
import photo from './../../images/default/me.jpg'
import { Contacts } from '../Contacts/Contacts'
import { context } from '../Main/Main'
import { useContext } from 'react'
import Helmet from 'react-helmet'

export function About(){
    const device = useContext(context)
    return (
        <>
            <Helmet
            title='Об авторе - halikov.com | Про IT, поэзию и жизнь'
            meta={[
                {'name': 'description', 'content': 'Привет!Меня зовут Ульфат Халиков, я живу в Санкт-Перебурге.Последний год я работаю Web разработчиком.Я занимаюсь разработкой сайтов, telegram ботов, изучением английского языка, а еще иногда пишу стихи.Здесь я буду выкладывать советы для начинающих разработчиков, свои стихи, а также информацию о проектах, в которых принимаю участие.Также, я готов ответить на все ваши вопросы, которые вы можете задать на соответствующей странице, либо лично, через социальные сети.'},
            ]}/>
            <div className={styles.about}>
                <div className={styles.about__block}>
                    <img className={styles.photo} src={photo} alt="" />
                    <div className={`${styles.info} ${styles[device]}`}>
                        <p>Привет!</p>
                        <p>Меня зовут Ульфат Халиков, я живу в Санкт-Перебурге.</p>
                        <p>Последний год я работаю Web разработчиком.</p>
                        <p>Я занимаюсь разработкой сайтов, telegram ботов, изучением английского языка, а еще иногда пишу стихи.</p>
                        <p>Здесь я буду выкладывать советы для начинающих разработчиков, свои стихи, а также информацию о проектах, в которых принимаю участие.</p>
                        <p>Также, я готов ответить на все ваши вопросы, которые вы можете задать на соответствующей <span className={styles.link}><Link to='questions'>странице</Link></span>, либо лично, через социальные сети.</p>
                    </div>
                    {device === 'mobile' && <Contacts/>}
                </div>
            </div>
        </>
    )
}