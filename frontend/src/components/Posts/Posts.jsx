import styles from './Posts.module.css'
import { PostPreview } from '../PostPreview/PostPreview'
import { useLoaderData, Outlet } from 'react-router-dom'
import Helmet from 'react-helmet'

export function Posts(){
    const posts = useLoaderData()
    return (
        <>
            <Helmet
                title={`Все статьи Халикова У.Ж - halikov.com | Про IT, поэзию и жизнь`}
                meta={[
                    {'name': 'description', 'content': 'Список статей владельца/разработчика данного сайта. Статьи про жизнь, разработку на языках программирования python/javascript, HTML верстку, CSS стилизацию, различные проекты.'},
                ]}/>
            <div className={styles.posts}>
                {posts && <div className={styles.posts}>{posts.map(post => <PostPreview key={post.id} post={post}/>)}</div>}
            </div>
            <Outlet/>
        </>
    )
}
