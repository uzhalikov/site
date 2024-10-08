import styles from './Nav.module.css'
import { useContext, useRef } from 'react'
import { context } from '../Main/Main'
import { NavLink } from 'react-router-dom'
import { Contacts } from '../Contacts/Contacts'
import myPhoto from './../../images/default/me.jpg'

export function Nav(props){
    const device = useContext(context)
    const navRef = useRef()

    const hideMenu =() => {
        navRef.current.classList.add(styles.nav__hide)
        const timer = setTimeout(() => props.setMenu(false), 600)
        return () => {
            clearTimeout(timer)
        }
    }
    const handleClick = () => device === 'mobile' && hideMenu()
    const getActiveLink = (isActive) => isActive ? styles.active__item : styles.nav__item

    return (
        <nav ref={navRef} className={device === 'mobile' ? styles.nav__mobile : styles.nav}>
            <button onClick={hideMenu} className={styles.nav__close}>&times;</button>
            <img className={styles.nav__logo} src={myPhoto} alt="Ulfat Khalikov's photo"/>            
            <h2 className={styles.nav__author}>Ulfat Khalikov</h2>
            <div className={styles.nav__list}>
                <NavLink className={({isActive}) => getActiveLink(isActive)} to='' onClick={handleClick}>Об авторе</NavLink>
                <NavLink className={({isActive}) => getActiveLink(isActive)} to='posts' onClick={handleClick}>Статьи <span className={styles.unread__posts}>{props.unread > 0 && `[${props.unread}]`}</span></NavLink>
                <NavLink className={({isActive}) => getActiveLink(isActive)} to='poems' onClick={handleClick}>Стихи</NavLink>
                <NavLink className={({isActive}) => getActiveLink(isActive)} to='questions' onClick={handleClick}>Вопросы</NavLink>
            </div>     
            <Contacts/>
        </nav>
    )
  }