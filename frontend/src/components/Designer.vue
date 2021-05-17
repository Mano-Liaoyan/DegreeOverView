<template>
  <div id="designer">
    <a-layout id="components-layout-demo-custom-trigger">
      <a-layout-sider v-model="collapsed" :trigger="null" collapsible>
        <div v-if="collapsed" id="logo-collapsed"></div>
        <div v-else id="logo"></div>
        <a-menu theme="dark" mode="inline" :default-selected-keys="['1']">
          <a-menu-item key="1">
            <a-icon type="plus"/>
            <span>Create a new course</span>
          </a-menu-item>
          <a-menu-item key="2">
            <a-icon type="edit"/>
            <span>Modify a course</span>
          </a-menu-item>
          <a-menu-item key="3">
            <a-icon type="tool"/>
            <span>Define dependencies</span>
          </a-menu-item>
          <a-menu-item key="4">
            <a-icon type="eye"/>
            <span>View dependencies</span>
          </a-menu-item>
          <a-menu-item key="5">
            <a-icon type="link"/>
            <span>Define relationships</span>
          </a-menu-item>
        </a-menu>
      </a-layout-sider>
      <a-layout>
        <a-layout-header style="background: #fff; padding: 0">
          <a-row type="flex" justify="space-between" align="middle">
            <a-icon class="trigger" :type="collapsed ? 'menu-unfold' : 'menu-fold'" @click="() => (this.collapsed = !collapsed)"/>
            <a-col>
              <h2 style="font-weight :bold; margin: 0;"> DegreeOverView </h2>
            </a-col>
            <!--Left top bar-->
            <a-col>
              <a-row>
                <a-col>
                  <a-icon type="smile"></a-icon>
                  Welcome xxx!   
                  <a style="margin-left: 20px;">     Log out   </a>
                  <a-icon class="top-left-buttons" type="logout" style="color: #BB4444"/>
                </a-col>
              </a-row>
            </a-col>
          </a-row>
        </a-layout-header>
        <a-layout-content :style="{ margin: '24px 16px', padding: '24px', background: '#fff', minHeight: '280px' }">
          Content
        </a-layout-content>
      </a-layout>
    </a-layout>
  </div>
</template>
<script>

export default {
  data() {
    return {
      collapsed: false,
    };
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

#designer {
  height: 100%;
}
</style>
