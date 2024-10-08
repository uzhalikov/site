import styles from './Question.module.css'

export function Question({question}){
    return(
        <div className={styles.question__container}>
            <div className={styles.question}>
                <span className={styles.question__label}>Question:</span>
                <p className={styles.question__name}>{question.author}: <span className={styles.question__text}>{question.question}</span></p>
            </div>
            <div className={styles.answer}>
                <span className={styles.question__label}>Answer:</span>
                <p>{question.author} {question.answer}</p>
            </div>
        </div>
    )
}