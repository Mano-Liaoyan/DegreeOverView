// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'
import Antd from 'ant-design-vue'
import App from './App'
import router from './router'
import less from 'less'
import 'ant-design-vue/dist/antd.css'
import vuescroll from 'vuescroll';

Vue.config.productionTip = false

Vue.use(Antd)
Vue.use(less)
Vue.use(vuescroll); // install the vuescroll first
Vue.use(Vuex)
Vue.prototype.$vuescrollConfig = {
  bar: {
    background: '#8c8686'
  }
};

const store = new Vuex.Store({
  state: {
    count: 0,
    search_result: undefined,
    new_cilos: [],
    new_related_cilos: [],
    cilo_finished: false,
    as_finished: false,
    create_course_form: {
      course_name: '',
      academic_start_year: '',
      program: '',
      cilos: [],
      assessments: [],
      type: ''
    }
  },
  mutations: {
    increment(state) {
      state.count++;
    },
    setResult(state, data) {
      state.search_result = data;
    },
    setCilos(state, data) {
      /*      if (!state.new_cilos.includes(data))
              state.new_cilos.push(data);*/
      state.new_cilos = data
    },
    pushCilos(state, data) {
      if (!state.new_related_cilos.includes(data))
        state.new_related_cilos.push(data)
    },
    filterCilo(state, data) {
      if (state.new_cilos.includes(data))
        state.new_cilos = state.new_cilos.filter(o => o !== data);
    },
    set_course_form(state, payload) {
      if (payload.course_name)
        state.create_course_form.course_name = payload.course_name;
      if (payload.course_code)
        state.create_course_form.course_code = payload.course_code;
      if (payload.academic_start_year)
        state.create_course_form.academic_start_year = payload.academic_start_year;
      if (payload.program)
        state.create_course_form.program = payload.program;
      if (payload.cilos)
        state.create_course_form.cilos = payload.cilos;
      if (payload.assessments)
        state.create_course_form.assessments = payload.assessments;
      if (payload.type)
        state.create_course_form.type = payload.type;
    },
    change_cilo_finished(state) {
      state.cilo_finished = !state.cilo_finished
    },
    change_as_finished(state) {
      state.as_finished = !state.as_finished
    }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: {App},
  template: '<App/>'
})
