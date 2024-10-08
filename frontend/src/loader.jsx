import { sendRequest } from "./utils"
import { URL as ApiURL } from "../config"

export const getPosts = async ({request}) => {
    const url = new URL(request.url)
    const keyWord = url.searchParams.get("filter")
    const currentURL = `${ApiURL}/api/posts/?filter=${keyWord ? keyWord : ''}`
    return await sendRequest(currentURL)
}
export const getPoems = async () => {
    const currentURL = `${ApiURL}/api/poems/`
    return await sendRequest(currentURL)
}
export const getPost = async ({params: {slug}}) => {
    const post = await sendRequest(`${ApiURL}/api/post/${slug}`, 'put')
    return post[0]
}
export const getPoem = async ({params: {id}}) => {
    const poem = await sendRequest(`${ApiURL}/api/poem/${id}`)
    return poem[0]
}
