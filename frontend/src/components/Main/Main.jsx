import { createContext, useState } from 'react'
import { Outlet, useLocation } from 'react-router-dom'
import styles from './Main.module.css'
import { Nav } from '../Nav/Nav'
import { useDeviceDetect } from '../../hooks/useDeviceDetect'
import { Header } from '../Header/Header'
import { useEffect } from 'react'
import { sendRequest } from '../../utils'
import { URL } from '../../../config'

export const context = createContext()

export function Main(){
    const {device} = useDeviceDetect() 
    const [menu, setMenu] = useState(device !== 'mobile')
    const [unread, setUnread] = useState('')
    useEffect(() => setMenu(device !== 'mobile'), [device])

    useEffect(() => {
        sendRequest(`${URL}/api/posts/unread/`)
        .then(response => setUnread(response.count))
    }, [useLocation().pathname])
    
    return (
        <context.Provider value={device}>
            {menu && <Nav setMenu={setMenu} unread={unread} />}
            <main className={device === 'mobile' ? styles.main__mobile : styles.main}>
                <Header setMenu={setMenu}/>
                <Outlet/>
            </main>
        </context.Provider>
    )
}