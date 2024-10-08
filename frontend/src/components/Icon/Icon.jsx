import styles from './Icon.module.css'
import linkedin from './../../images/default/social/linkedin.svg'
import github from './../../images/default/social/github.svg'
import instagram from './../../images/default/social/instagram.svg'
import telegram from './../../images/default/social/telegram.svg'
import vk from './../../images/default/social/vk.svg'
import youtube from './../../images/default/social/youtube.svg'

export function Icon(props){
    const imgList = {
        'telegram': telegram,
        'linkedin': linkedin,
        'instagram': instagram,
        'youtube': youtube,
        'vk': vk,
        'github': github,
    }
    return <a href={props.url} target='_blank'><img className={styles.icon} alt="Icon" src={imgList[props.src]}/></a>
}