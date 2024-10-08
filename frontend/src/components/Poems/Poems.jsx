import styles from './Poems.module.css'
import { PoemPreview } from '../PoemPreview/PoemPreview'
import { useLoaderData } from 'react-router-dom'
import Helmet from 'react-helmet'

export function Poems(){
    const poems = useLoaderData()
    return (
        <>
            <Helmet
            title='Все стихотворения Халикова У.Ж - halikov.com | Про IT, поэзию и жизнь'
            meta={[
                {'name': 'description', 'content': 'Список стихотворений владельца/разработчика данного сайта. Стихи про жизнь и смерть, любовь и разлуку, про животных, про любимые места.'},
            ]}/>
            <div className={styles.poems}>{poems.map((poem, index) => <PoemPreview key={poem.id} poem={poem} index={index}/>)}</div>
        </>
    )
}
