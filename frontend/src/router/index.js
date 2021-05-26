import Vue from 'vue'
import Router from 'vue-router'
import LogIn from '@/components/LogIn'
import Lecturer from '@/components/Lecturer'
import Designer from '@/components/Designer'
import Student from '@/components/Student'
import CourseMain from '@/components/CourseMain'
import DefineDependency from '@/components/DefineDependency'
import Chart from '@/components/chart'
import courseListModify from '@/components/CourseListForModify'
import CourseListForAnalysis from '@/components/CourseListForAnalysis'

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
      component: Lecturer,
      children: [
        {
          path: 'analysislist',
          name: 'CourseListForAnalysis',
          component: CourseListForAnalysis
        },
        {
          path: 'chart',
          name: 'Chart',
          component: Chart
        },
      ]
    },
    {
      path: '/designer',
      name: 'Designer',
      component: Designer,
      children: [
        {
          path: 'search-result',
          name: 'SearchResult',
          component: () => import('../components/SearchResult.vue'),
        },
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
          component: CourseMain, 
          childern: [
            {
              path: 'editassessment',
              name: 'editassessment',
              component: () => import('../components/aaa1.vue'),
            }
          ]
        },
        {
          path: 'definedependency',
          name: 'DefineDependency',
          component: DefineDependency
        },
        {
          path: 'courseListModify',
          name: 'CourseListForModify',
          component: courseListModify
        },
      ]
    },
    {
      path: '/student',
      name: 'student',
      component: Student
    },
    {
      path: '/modal',
      name: 'modal',
      component: () => import('../components/modal.vue'),
    },

  ]
})

const VueRouterPush = Router.prototype.push
Router.prototype.push = function push(to) {
  return VueRouterPush.call(this, to).catch(err => err)
}
