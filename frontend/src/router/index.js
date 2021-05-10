import Vue from 'vue'
import Router from 'vue-router'
import LogIn from '@/components/LogIn'
import Lecturer from '@/components/Lecturer'
import Designer from '@/components/Designer'
import Student from '@/components/Student'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'LogIn',
      component: LogIn
    },
    {
      path: '/lecturer',
      name: 'lecturer',
      component: Lecturer
    },
    {
      path: '/designer',
      name: 'designer',
      component: Designer
    },
    {
      path: '/student',
      name: 'student',
      component: Student
    }
  ]
})
