<template>
  <div id="coursemain">
    <a-layout id="components-layout-demo-custom-trigger">
      <a-layout-header>
      <div class="logo" />
      <a-menu
        theme="dark"
        mode="horizontal"
        :default-selected-keys="['2']"
        :style="{ lineHeight: '64px', margin: auto}"
      >
        <a-menu-item key="1">
          Edit CILOs
        </a-menu-item>
        <a-menu-item key="2">
          Import CILOs
        </a-menu-item>
        <a-menu-item key="3">
          Edit Assessments
        </a-menu-item>
        <a-menu-item key="4">
          Import Assessments
        </a-menu-item>
        
      </a-menu>
    </a-layout-header>
      <a-layout>
        <a-layout-content style="padding: 0 50px">
          <a-breadcrumb style="margin: 16px 0">
            <a-breadcrumb-item>Home</a-breadcrumb-item>
            <a-breadcrumb-item>List</a-breadcrumb-item>
            <a-breadcrumb-item>App</a-breadcrumb-item>
          </a-breadcrumb>
            <a-layout-content :style="{ margin: '24px 16px', padding: '24px', background: '#fff', minHeight: '280px' }">
            Content
            </a-layout-content>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </div>
</template>
<script>
import Search from "./Search";


export default {
  name: 'Designer',
  components: {
    Search,
  },
  data() {
    return {
      collapsed: false,
      selection: 0,
    };
  },
  methods: {
           //路由内容切换
      changeMenu(route){
        if(this.$route.path !== route){
          console.log(route)
          this.$router.push(route)
        }
      }
  }
};
</script>
<style>
#components-layout-demo-custom-trigger .trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

.top-left-buttons {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px 0 6px;
  cursor: pointer;
  transition: color 0.3s;
}

.top-left-buttons:hover {
  color: #BB4444;
}

#components-layout-demo-custom-trigger .trigger:hover {
  color: #1890ff;
}

#components-layout-demo-custom-trigger #logo-collapsed {
  height: 48px;
  width: 48px;
  margin: 16px auto;
  background-image: url('../../static/images/timg.jpg');
  -moz-background-size: 100% 100%;
  background-size: 100% 100%;
}

#components-layout-demo-custom-trigger #logo {
  height: 48px;
  margin: 16px;
  font-size: 20px;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  /*background-color: rgba(185, 104, 66, 0.26);*/
  -moz-background-size: 100%;
  background-size: 100%;
}

#components-layout-demo-custom-trigger {
  height: 100%;
}

#coursemain {
  height: 100%;
}
</style>
