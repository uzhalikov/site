import styles from './Switcher.module.css'
import { Link } from 'react-router-dom'


export function Switcher({item}){
    const current = window.location.pathname.split('/')[1]
    return (
        <section className={styles.switcher}>
            <Link className={styles.arrow} to={`/${current}/${item.prev_p}`}>{item.prev_p && '←'}</Link>
            <h2 className={styles.title}>{item.title ? item.title : '***'}</h2>
            <Link className={styles.arrow} to={`/${current}/${item.next_p}`}>{item.next_p && '→'}</Link>
        </section>
    )
}