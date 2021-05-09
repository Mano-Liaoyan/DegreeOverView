import Login from '@/components/Login.vue'
import StudentHome from "@/components/StudentHome";

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
    {
        path: '/student-home',
        name: 'student-home',
        component: StudentHome
    },
]
export default routers