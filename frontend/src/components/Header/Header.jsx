import styles from './Header.module.css'
import { H1 } from '../H1/H1'
import { useLocation } from 'react-router-dom'
import { capitalize } from '../../utils'
import { MenuIcon } from '../MenuIcon/MenuIcon'
import { useContext } from 'react'
import { context } from '../Main/Main'
import { Link } from 'react-router-dom'
import { Search } from '../Search/Search'

export function Header(props){
    const device = useContext(context)
    const currentPath = useLocation().pathname.split('/')[1]
    

    return(
        <header className={styles.header}>
            <H1><Link to={currentPath}>{capitalize(currentPath || 'About me')}</Link></H1>
            <div className={styles.flex}>
                {currentPath === 'posts' && <Search/>}
                {device === 'mobile' && <MenuIcon onClick={props.setMenu}/>}
            </div>
        </header>
    )
}