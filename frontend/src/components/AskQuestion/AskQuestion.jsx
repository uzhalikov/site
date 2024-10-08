import { useState } from 'react'
import styles from './AskQuestion.module.css'
import { sendRequest } from '../../utils'
import { URL } from '../../../config'
import ReCAPTCHA from 'react-google-recaptcha'

export function AskQuestion(){
    const [author, setAuthor] = useState('')
    const [check, setCheck] = useState(false)
    const [question, setQuestion] = useState('')
    const [message, setMessage] = useState('')
    

    const handleSubmit = () => {
        const formData = new FormData()
        formData.append('question', question)
        formData.append('author', author)
        sendRequest(`${URL}/api/questions/`, 'post', formData)
        .then(result => {
            if(result.status === 'success'){
                setMessage(result.text)
                setAuthor('')
                setQuestion('')
            }
        })
    }
    const onChange = (value) => {
        const key = '6LdE8VkqAAAAAKm70ZAjN8Ax3eM8hQhzQQfI1J8p'
        const formData = new FormData()
        formData.append('key', key)
        formData.append('response', value)

        sendRequest(`${URL}/api/check_captcha/`, 'post', formData)
        .then(result => {
            setCheck(result)
        })

    }
    return(
        <div className={styles.container}>
            <div className={styles.field__container}>
                <input
                onChange={(e) => setAuthor(e.target.value)}
                value={author}
                autoComplete='off'
                name='name'
                className={styles.field}
                type="text"
                placeholder=''
                />
                <label className={styles.label} htmlFor="name">your name</label>
            </div>
            <div className={styles.field__container}>
                <input
                onChange={(e) => setQuestion(e.target.value)}
                value={question}
                autoComplete='off'
                name='question'
                className={styles.field}
                type="text"
                placeholder=''
                />
                <label className={styles.label} htmlFor="question">write your question here</label>
            </div>
            <ReCAPTCHA sitekey='6LdE8VkqAAAAACaFdloFag5VZUVEGavkkGcz62uh' onChange={onChange}/>
            <button onClick={handleSubmit} className={(author && question) ? `${styles.button} ${styles.active__button}`: styles.button} type="button">Ask</button>
            {message && <p className={styles.message}>{message}</p>}
        </div>
    )
}