<template>
  <div id="designer">
    <a-layout id="components-layout-demo-custom-trigger">
      <a-layout-sider class="ant-layout-sider-light" v-model="collapsed" :trigger="null" collapsible>
        <div v-if="collapsed" id="logo-collapsed"></div>
        <div v-else id="logo" style="color: grey; font-weight: bold;">DegreeOverview</div>
        <a-menu theme="light" mode="inline" :default-selected-keys="['0']">
          <a-menu-item key="0" @click="changeMenu('designerhome')">
            <a-icon type="home"/>
            <span>Home</span>
          </a-menu-item>
          <a-menu-item key="1" @click="changeMenu('AddCourse')">
            <a-icon type="plus"/>
            <span>Create a new course</span>
          </a-menu-item>
          <a-menu-item key="2" @click="changeMenu('CourseListForModify')">
            <a-icon type="edit"/>
            <span>Modify a course</span>
          </a-menu-item>
          <a-menu-item key="3" @click="changeMenu('CourseListForDependency')">
            <a-icon type="tool"/>
            <span>Define dependencies</span>
          </a-menu-item>
          <a-menu-item key="4" @click="changeMenu('dependencyDesigner')">
            <a-icon type="eye"/>
            <span>View dependencies</span>
          </a-menu-item>
          <a-menu-item key="5" @click="changeMenu('CourseListForRelationship')">
            <a-icon type="link"/>
            <span>Define relationships</span>
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
            <a-col :span="8">
              <Search></Search>
            </a-col>
            <!--Right top bar-->
            <a-col :span="8">
              <a-row type="flex" justify="end" align="middle">
                <a-col>
                  <a-icon type="smile"></a-icon>
                  Welcome xxx!
                  <a style="margin-left: 20px"> Log out </a>
                  <a-icon class="top-left-buttons" type="logout" style="color: #bb4444"/>
                </a-col>
              </a-row>
            </a-col>
          </a-row>
        </a-layout-header>
        <a-layout-content :style="{
            margin: '24px 16px',
            padding: '24px',
            background: '#fff',
            
            // minHeight: '100%',
            // minHeight: '280px',
          }">
          <vuescroll style="height: 100%">
            <router-view/>
          </vuescroll>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </div>
</template>
<script>
import Search from "./Search";

export default {
  name: "Designer",
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
#right-logo {
  text-align: right;
}

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
  -moz-background-size: 100%;
  background-size: 100%;
}

#components-layout-demo-custom-trigger {
  height: 100%;
}

#designer {
  height: 100%;
}
</style>
