import { prepareDate } from '../../utils'
import styles from './PostPreview.module.css'
import { Link } from 'react-router-dom'

export function PostPreview(props){
    const title = props.post.read ? styles.post__title : `${styles.post__title} ${styles.new}`
    return (
        <Link className={styles.post} to={`${props.post.slug}`}>           
            <div className={styles.post__main}>
                <h2 className={title}>{props.post.title}</h2>
                <div className={styles.post__container}>
                    <div className={styles.post__text}>{props.post.post.replace(/<[^>]+>/g, '')}</div>
                    <div className={styles.post__info}>
                        <span className={styles.post__author}>{props.post.author}</span>
                        <span>{prepareDate(props.post.created)}</span>
                    </div>
                </div>
            </div>
        </Link>
    )
}