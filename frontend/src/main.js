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
    search_result: undefined
  },
  mutations: {
    increment(state) {
      state.count++;
    },
    setResult(state, data) {
      state.search_result = data;
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
