<template>
  <div id="designer">
    <a-layout id="components-layout-demo-custom-trigger">
      <a-layout-sider v-model="collapsed" :trigger="null" collapsible>
        <div v-if="collapsed" id="logo-collapsed"></div>
        <div v-else id="logo">DegreeOverview</div>
        <a-menu theme="dark" mode="inline" :default-selected-keys="['0']">
          <a-menu-item key="0" @click="changeMenu('/designer')">
            <a-icon type="home" />
            <span>Home</span>
          </a-menu-item>
          <a-menu-item key="1" @click="changeMenu('addcourse')">
            <a-icon type="plus" />
            <span>Create a new course</span>
          </a-menu-item>
          <a-menu-item key="2" @click="changeMenu('modify')">
            <a-icon type="edit" />
            <span>Modify a course</span>
          </a-menu-item>
          <a-menu-item key="3" v-model="selection">
            <a-icon type="tool" />
            <span>Define dependencies</span>
          </a-menu-item>
          <a-menu-item key="4" v-model="selection">
            <a-icon type="eye" />
            <span>View dependencies</span>
          </a-menu-item>
          <a-menu-item key="5" v-model="selection">
            <a-icon type="link" />
            <span>Define relationships</span>
          </a-menu-item>
        </a-menu>
      </a-layout-sider>
      <a-layout>
        <a-layout-header style="background: #fff; padding: 0">
          <a-row type="flex" justify="space-between" align="middle">
            <!--     Right Notify Button       -->
            <a-col> </a-col>
            <!--     Center Search function       -->
            <a-col>
              <Search></Search>
            </a-col>
            <!--Right top bar-->
            <a-col>
              <a-row>
                <a-col>
                  <a-icon type="smile"></a-icon>
                  Welcome xxx!
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
          <router-view />
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
        this.$router.push(route);
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
  background-image: url("../../static/images/timg.jpg");
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

#designer {
  height: 100%;
}
</style>
