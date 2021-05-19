import Vue from 'vue'
import Router from 'vue-router'
import LogIn from '@/components/LogIn'
import Lecturer from '@/components/Lecturer'
import Designer from '@/components/Designer'
import Student from '@/components/Student'
import CourseMain from '@/components/CourseMain'
import DefineDependency from '@/components/DefineDependency'
import Chart from '@/components/chart'

Vue.use(Router)


export default new Router({
  mode: "history",
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
      name: 'Designer',
      component: Designer,
      children: [
        {
          path: 'modify',
          name: 'ModifyCourse',
          component: () => import('../components/ModifyCourse.vue'),
        },
        {
          path: 'addcourse',
          name: 'AddCourse',
          component: () => import('../components/AddCourse.vue'),
        },
        {
          path: 'coursemain',
          name: 'CourseMain',
          component: CourseMain
        },
        {
          path: 'definedependency',
          name: 'DefineDependency',
          component: DefineDependency
        },
        {
          path: 'chart',
          name: 'Chart',
          component: Chart
        }
      ]
    },
    {
      path: '/student',
      name: 'student',
      component: Student
    },

  ]
})

const VueRouterPush = Router.prototype.push
Router.prototype.push = function push(to) {
  return VueRouterPush.call(this, to).catch(err => err)
}
