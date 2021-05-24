// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
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
Vue.prototype.$vuescrollConfig = {
  bar: {
    background: '#8c8686'
  }
};

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})
