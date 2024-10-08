import styles from './Questions.module.css'
import { useState } from 'react'
import { AskQuestion } from '../AskQuestion/AskQuestion'
import { AllQuestions } from '../AllQuestions/AllQuestions'
import Helmet from 'react-helmet'

export function Questions(){
    const [active, setActive] = useState('ask')

    const getClassName = (item) => item === active ? `${styles.active__question} ${styles.section__question}` : styles.section__question
    return (
        <>
            <Helmet
            title='Вопросы - halikov.com | Про IT, поэзию и жизнь'
            meta={[
                {'name': 'description', 'content': 'Задать любой интересующий вопрос владельцу сайта анонимно, просмотреть список заданных вопросов.'},
            ]}/>
            <div className={styles.questions}>
                <section className={styles.questions__section}>
                    <span onClick={() => setActive('ask')} id='ask' className={getClassName('ask')}>Ask a question</span>
                    <span onClick={() => setActive('all')} id='all' className={getClassName('all')}>All the questions</span>
                </section>
                { active === 'ask' ? <AskQuestion/> : <AllQuestions/>}
            </div>
        </>
    )
}