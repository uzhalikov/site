import { About } from './components/About/About.jsx'
import { Posts } from './components/Posts/Posts.jsx'
import { Post } from './components/Post/Post.jsx'
import { Poem } from './components/Poem/Poem.jsx'
import { Poems } from './components/Poems/Poems.jsx'
import { Main } from './components/Main/Main.jsx'
import { ErrorPage404 } from './components/ErrorPage404/ErrorPage404.jsx'
import { Questions } from './components/Questions/Questions.jsx'
import { getPosts, getPost, getPoems, getPoem } from './loader.jsx'
import { createBrowserRouter } from 'react-router-dom'

export const router = createBrowserRouter([
    {
        path: '/',
        element: <Main/>,
        errorElement: <ErrorPage404 />,
        children: [
            {
                path: '',
                element: <About/>
            },
            {
                path: 'posts/:slug',
                element: <Post/>,
                loader: getPost
            },
            {
                path: 'posts',
                element: <Posts/>,
                loader: getPosts,
                action: getPosts
            },
            {
                path: 'poems/:id',
                element: <Poem/>,
                loader: getPoem
            },
            {
                path: 'poems',
                element: <Poems/>,
                loader: getPoems
            },
            {
                path: 'questions',
                element: <Questions/>
            },
        ]
    }
])