import styles from './H1.module.css'

export function H1({children}){
    return <h1 className={styles.h1}>{children}</h1>
}