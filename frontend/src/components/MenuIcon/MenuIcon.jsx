import styles from './MenuIcon.module.css'
import icon from './../../images/default/menu.svg'

export function MenuIcon(props){
    return <img onClick={props.onClick} className={styles.burger__mobile} src={icon} alt="" />
}