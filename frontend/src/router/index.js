import Vue from 'vue'
import Router from 'vue-router'
import LogIn from '@/components/LogIn'
import Lecturer from '@/components/Lecturer'
import Designer from '@/components/Designer'
import Student from '@/components/Student'
import CourseMain from '@/components/CourseMain'
import DefineDependency from '@/components/DefineDependency'
import PerformanceChart from '@/components/performanceChart'
import courseListModify from '@/components/CourseListForModify'
import CourseListForAnalysis from '@/components/CourseListForAnalysis'
import CreateNewCourse from "../components/CreateNewCourse";
import CourseListForDependency from "../components/CourseListForDependency";
import CourseListForRelationship from "../components/CourseListForRelationship";
import CourseListForPerformance from "../components/CourseListForPerformance";
import AsAndCiloTable from "../components/AssessmentTable";

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
      name: 'Lecturer',
      component: Lecturer,
      children: [
        {
          path: 'analysislist',
          name: 'CourseListForAnalysis',
          component: CourseListForAnalysis
        },
        {
          path: '/analysisResult',
          name: 'AnalysisResult',
          component: () => import('../components/Analysis.vue'),
        },
        {
          path: '/dependencyLecturer',
          name: 'dependencyLecturer',
          component: () => import('../components/ViewDependency.vue'),
        },
        {
          path: '/lecturerhome',
          name: 'lecturerhome',
          component: () => import('../components/Homepage.vue'),
        },
      ]
    },
    {
      path: '/designer',
      name: 'Designer',
      component: Designer,
      children: [
        {
          path: '/designerhome',
          name: 'designerhome',
          component: () => import('../components/Homepage.vue'),
        },
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
          component: CreateNewCourse
        },

        {
          path: 'definedependency',
          name: 'DefineDependency',
          component: DefineDependency
        },
        {
          path: 'courseListDefinedependency',
          name: 'CourseListForDependency',
          component: CourseListForDependency
        },
        {
          path: 'courseListModify',
          name: 'CourseListForModify',
          component: courseListModify
        },
        {
          path: 'courseLisRelationship',
          name: 'CourseListForRelationship',
          component: CourseListForRelationship
        },
        {
          path: 'ascilotable',
          name: 'AsAndCiloTable',
          component: AsAndCiloTable
        },
        {
          path: '/dependencyDesigner',
          name: 'dependencyDesigner',
          component: () => import('../components/ViewDependency.vue'),
        },
        {
          path: 'searchResultDesigner',
          name: 'searchResultDesigner',
          component: () => import('../components/SearchResult.vue'),
        },
        {
          path: 'courseInfo',
          name: 'courseInfo',
          component: () => import('../components/CourseInfo.vue'),
        },
      ]
    },
    {
      path: '/student',
      name: 'Student',
      component: Student,
      children: [
        {
          path: '/studenthome',
          name: 'studenthome',
          component: () => import('../components/Homepage.vue'),
        },
        {
          path: 'performanceChart',
          name: 'PerformanceChart',
          component: PerformanceChart
        },
        {
          path: 'courseListPerformance',
          name: 'CourseListForPerformance',
          component: CourseListForPerformance,
          children: []
        },
        {
          path: '/dependencyStudent',
          name: 'dependencyStudent',
          component: () => import('../components/ViewDependency.vue'),
        },
      ]
    },
    {
      path: '/modal',
      name: 'modal',
      component: () => import('../components/modal.vue'),
    },
    {
      path: '/dependencychart',
      name: 'dependencychart',
      component: () => import('../components/ViewDependency.vue'),
    },
  ]
})

const VueRouterPush = Router.prototype.push
Router.prototype.push = function push(to) {
  return VueRouterPush.call(this, to).catch(err => err)
}
