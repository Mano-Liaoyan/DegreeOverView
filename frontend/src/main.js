import Vue from 'vue';
import App from './App.vue';
import Antd from 'ant-design-vue';
import VueRouter from 'vue-router';
import routers from './routers';
import 'ant-design-vue/dist/antd.css';

Vue.config.productionTip = false;
Vue.use(Antd);
Vue.use(VueRouter);

const router = new VueRouter({
    mode: 'history',
    routes: routers
})


new Vue({
    render: h => h(App), router
}).$mount('#app')
