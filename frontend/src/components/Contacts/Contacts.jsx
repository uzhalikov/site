import styles from './Contacts.module.css'
import { Icon } from '../Icon/Icon'
import { useLayoutEffect, useState } from 'react'
import { sendRequest } from '../../utils'
import { URL } from '../../../config'


export function Contacts(){
    const [link, setLink] = useState([])
    useLayoutEffect(() => {
        sendRequest(`${URL}/api/users/contacts/`).then(response => {
            setLink(response.map(item => item))
        })
    }, [])

    return (
        <ul className={styles.contacts__list}>
            {link.map(item => <li key={item.id}><Icon url={item.link} src={item.name}/></li>)}
        </ul>
    )
}