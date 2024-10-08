import { prepareDate } from '../../utils'
import { Link } from 'react-router-dom'
import styles from './PoemPreview.module.css'

export function PoemPreview({poem}){
    return (
        <Link className={styles.poem} to={`/poems/${poem.id}`}>
            <pre className={styles.poem__text}>{String.raw`${poem.poem}`}...</pre>
            <div className={styles.poem__info}>
                <p className={styles.poem__author}>{poem.author},</p>
                <p>{prepareDate(poem.created)}</p>
            </div>
        </Link>
    )
}