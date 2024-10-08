import { URL as ApiURL } from "../config"

export const prepareDate = (date) => {
    const newDate = new Date(date)
    return newDate.toLocaleDateString()
}
export const sendRequest = async(url, method, data) =>{
    const response = await fetch(url, {
        method: method,
        body: data
    })
    return await response.json()
}
export function getCookie(name) {
	const matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
	return matches ? decodeURIComponent(matches[1]) : undefined;
}
export const action = async ({request}) => {
    const formData = await request.formData()
    let value = formData.get('text')
    return await sendRequest(`${ApiURL}/api/posts/?filter=${value}`)
}
export const capitalize = (word) => {
    return `${word[0].toUpperCase()}${word.slice(1)}`
}
export const copy = (inputText) => {
    const text = document.createTextNode(inputText)
    document.body.appendChild(text)
    const range = document.createRange()
    range.selectNode(text)
    document.getSelection().removeAllRanges()
    document.getSelection().addRange(range)
    document.execCommand("copy")
    document.getSelection().removeAllRanges()
    text.remove()
}
