import styles from './Poem.module.css'
import { prepareDate } from '../../utils'
import { useLoaderData } from 'react-router-dom'
import { Switcher } from '../Switcher/Switcher'
import Helmet from 'react-helmet'

export function Poem(){
    const poem = useLoaderData()
    const poemTheme = poem.theme ? poem.theme : 'без темы'
    return (
        <>
            <Helmet
                title={`Стихотворение ${poemTheme} - halikov.com | Про IT, поэзию и жизнь`}
                meta={[
                    {'name': 'description', 'content': `${poem.poem.slice(0, 160)}`},
                ]}/>
            <article className={styles.poem}>
                <Switcher item={poem}/>
                <pre className={styles.poem__text}>
                    {String.raw`${poem.poem}`}
                </pre>
                <div className={styles.poem__info}>
                    <p className={styles.poem__author}>{poem.author_name},</p>
                    <p>{prepareDate(poem.created)}</p>
                </div>
            </article>
        </>

    )
}