import Vue from 'vue'
import Router from 'vue-router'
import LogIn from '@/components/LogIn'
import Lecturer from '@/components/Lecturer'
import Designer from '@/components/Designer'
import Student from '@/components/Student'
import CourseMain from '@/components/CourseMain'
import DefineDependency from '@/components/DefineDependency'

Vue.use(Router)



export default new Router({
  mode:"history",
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
      component: Designer,
      children:[
        {
          path: '/modify',
          name: 'modifycourse',
          component: () => import('../components/ModifyCourse.vue'),
        },
        {
          path: '/addcourse',
          name: 'addcourse',
          component: () => import('../components/AddCourse.vue'),
        },
        {
          path: '/coursemain',
          name: 'coursemain',
          component: CourseMain
        },
        {
          path: '/definedependency',
          name: 'definedependency',
          component: DefineDependency
        },
      ]
    },
    {
      path: '/student',
      name: 'student',
      component: Student
    },
  ]
})
