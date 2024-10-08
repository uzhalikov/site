import styles from './AllQuestions.module.css'
import { Question } from '../Question/Question'
import { useLayoutEffect, useState } from 'react'
import { sendRequest } from '../../utils'
import { URL } from '../../../config'

export function AllQuestions(){
    const [questions, setQuestions] = useState([])

    useLayoutEffect(() => {
        const response = sendRequest(`${URL}/api/questions/`)
        response.then(result => {
            setQuestions(result)
        })
    }, [])

    return(
        <div className={styles.question__container}>
            {questions.map(question => <Question key={question.id} question={question}/>)}
        </div>
    )
}