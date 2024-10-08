import { useLoaderData } from 'react-router-dom'
import styles from './Post.module.css'
import { prepareDate } from '../../utils'
import eyeLogo from './../../images/default/eye.png'
import { Switcher } from '../Switcher/Switcher'
import Helmet from 'react-helmet'

export function Post(){
    const post = useLoaderData()
    return (
        <>
            <Helmet
            title={`${post.title ? post.title.slice(0, 65) : '***'}`}
            meta={[
                {'name': 'description', 'content': post.post.slice(0, 160)},
            ]}/>
            <article className={styles.post}>
                <Switcher item={post}/>
                {post.image && <img className={styles.post__image} src={post.image} alt="post image"/>}
                <div className={styles.post__text} dangerouslySetInnerHTML={{__html: post.post}}></div>
                <div className={styles.post__footer}>
                    <div className={styles.post__tags}>{post.tags.map(item => <span key={item.id} className={styles.post__tag}>{item.name}</span>)}</div>
                    <div className={styles.post__info}>
                        <div className={styles.views__block}>
                            <img src={eyeLogo} alt="vews image" />
                            <span>{post.views}</span>
                        </div>
                        <span className={styles.post__author}>{post.author}</span>
                        <span>{prepareDate(post.created)}</span>
                    </div>
                </div>
            </article>
        </>
    )
}