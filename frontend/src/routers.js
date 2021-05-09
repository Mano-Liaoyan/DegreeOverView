import Login from './components/Login.vue'

const routers = [
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/',
        component: Login
    },
]
export default routers