<template>
  <div id="lecturer">
    <a-layout id="components-layout-demo-custom-trigger">
      <a-layout-sider class="ant-layout-sider-light" v-model="collapsed" :trigger="null" collapsible>
        <div v-if="collapsed" id="logo-collapsed"></div>
        <div v-else id="logo" style="color: grey; font-weight: bold;">DegreeOverview</div>
        <a-menu theme="light" mode="inline" :default-selected-keys="['0']">
          <a-menu-item key="0" @click="changeMenu('lecturerhome')">
            <a-icon type="home"/>
            <span>Home</span>
          </a-menu-item>
          <a-menu-item key="1" @click="changeMenu('inputProgrammeLecturer')">
            <a-icon type="eye"/>
            <span>View dependencies</span>
          </a-menu-item>
          <a-menu-item key="2" @click="changeMenu('CourseListForAnalysis')">
            <a-icon type="file"/>
            <span>View analysis result</span>
          </a-menu-item>
        </a-menu>
      </a-layout-sider>
      <a-layout>
        <a-layout-header style="background: white; padding: 0;">
          <a-row type="flex" justify="space-between" align="middle">
            <!--     Right Notify Button       -->
            <a-col :span="8">
              <a-icon class="trigger" :type="collapsed ? 'menu-unfold' : 'menu-fold'" @click="() => (this.collapsed = !collapsed)"/>
            </a-col>
            <!--     Center Search function       -->
            <a-col>
              <Search></Search>
            </a-col>
            <!--Right top bar-->
            <a-col>
              <a-row>
                <a-col>
                  <a-icon type="smile"></a-icon>
                  Welcome {{ this.$store.state.username }}!
                  <a style="margin-left: 20px"> Log out </a>
                  <a-icon
                    class="top-left-buttons"
                    type="logout"
                    style="color: #bb4444"
                  />
                </a-col>
              </a-row>
            </a-col>
          </a-row>
        </a-layout-header>
        <a-layout-content
          :style="{
            margin: '24px 16px',
            padding: '24px',
            background: '#fff',
            minHeight: '280px',
          }"
        >

          <router-view/>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </div>
</template>
<script>
import Search from "./Search";

export default {
  name: "Lecturer",
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
    changeMenu(route) {
      if (this.$route.path !== route) {
        console.log(route);
        this.$router.push({name: route});
      }
    },
  },
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
  color: #bb4444;
}

#components-layout-demo-custom-trigger .trigger:hover {
  color: #1890ff;
}

#components-layout-demo-custom-trigger #logo-collapsed {
  height: 48px;
  width: 48px;
  margin: 16px auto;
  background-image: url("../../static/images/logo.jpeg");
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

#lecturer {
  height: 100%;
}
</style>
