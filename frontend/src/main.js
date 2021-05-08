// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import { Button, message } from 'ant-design-vue'
import App from './App'
import router from './router'
import 'ant-design-vue/dist/antd.css'

Vue.config.productionTip = false

Vue.use(Button)

Vue.prototype.$message = message

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

// import Vue from 'vue'
// import { Button, message } from 'ant-design-vue'
// import App from './App'

// Vue.config.productionTip = false

// /* v1.1.2 */
// Vue.component(Button.name, Button)
// Vue.component(Button.Group.name, Button.Group)

// /* v1.1.3+ 自动注册Button下组件，如Button.Group */
// Vue.use(Button)

// Vue.prototype.$message = message

// /* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   components: { App },
//   template: '<App/>'
// })
