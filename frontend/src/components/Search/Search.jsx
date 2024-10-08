import styles from './Search.module.css'
import searchImg from './../../images/default/search.svg'
import { useState } from 'react'
import { Form } from 'react-router-dom'


export function Search(){
    const [value, setValue] = useState('')

    return (
        <Form className={styles.search__form} method='get' action='/posts'>
            <input autoComplete='off' name='filter' value={value} onChange={(e) => setValue(e.target.value)} type="text" placeholder='Поиск'/>
            <button type='submit'><img src={searchImg} alt="Search"/></button>
        </Form>
    )
}