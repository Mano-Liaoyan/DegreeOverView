<!--<template>
  <div id="designer">
      <div class="top">
        <a-row type="flex" justify="space-between">
          <a-col :span="12">
            <h2>Designer homepage</h2>
          </a-col>
          <a-col :span="12" justify="end"> 
            <p>welcome xxx!</p>
            <p>Log out</p>
          </a-col>
        </a-row>
      </div>
      <div class="middle">
        <a-row type="flex" justify="flex-start">
              <a-form :label-col="{ span: 24 }" :wrapper-col="{ span: 24 }" @submit.native.prevent>
                <a-form-item>
                  <a-input
                    v-model="infos.keyword" placeholder="Search Keywords">
                   <a-icon slot="prefix" type="search" style="color:rgba(0,0,0,.25)" />
                 </a-input>
                  <a-select default-value="Choose Search Function..." style="width: 30px" @change="handleChange">
                    <a-select-option value="course">
                     Search by Course
                    </a-select-option>
                    <a-select-option value="cilo">
                      Search by CILOs
                    </a-select-option>
                    <a-select-option value="keyword">
                     Search by Keywords
                   </a-select-option>
                  </a-select>
                </a-form-item>
                <a-form-item>
                <!-- <a-button type="primary" html-type="submit" :disabled="hasErrors(form.getFieldsError())"> 
                <a-button type="primary" html-type="submit">
                  Search
                </a-button>
              </a-form-item>
            </a-form>
            </a-row>
            
            <a-button>View Dependencies</a-button>
            <a-button>View Analysis Result</a-button>
          
        </div>

          </div>
    
</template>

<script>
export default {
  name: 'Designer',
  data() {
    return {
      infos: {
        keyword: '',
      }
    }
  }
}
</script>-->

<!-- Add "scoped" attribute to limit CSS to this component only -->
<!--
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
#designer {
  display: flex;
  height: 600px;
  width: 1000px;
  padding: 0 20px;
  background-color: #cccccc;
  justify-content: "center";
  flex-wrap: wrap;
}
.top {
  display: flex;
  height: 100px;
  width: 1000px;
}

</style>-->

<template>
  <a-layout id="components-layout-demo-top-side-2">
    <a-layout-header class="header">
      <div class="logo" />
      <a-menu
        theme="dark"
        mode="horizontal"
        :default-selected-keys="['2']"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1">
          nav 1
        </a-menu-item>
        <a-menu-item key="2">
          nav 2
        </a-menu-item>
        <a-menu-item key="3">
          nav 3
        </a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout>
      <a-layout-sider width="200" style="background: #fff">
        <a-menu
          mode="inline"
          :default-selected-keys="['1']"
          :default-open-keys="['sub1']"
          :style="{ height: '100%', borderRight: 0 }"
        >
          <a-sub-menu key="sub1">
            <span slot="title"><a-icon type="user" />subnav 1</span>
            <a-menu-item key="1">
              option1
            </a-menu-item>
            <a-menu-item key="2">
              option2
            </a-menu-item>
            <a-menu-item key="3">
              option3
            </a-menu-item>
            <a-menu-item key="4">
              option4
            </a-menu-item>
          </a-sub-menu>
          <a-sub-menu key="sub2">
            <span slot="title"><a-icon type="laptop" />subnav 2</span>
            <a-menu-item key="5">
              option5
            </a-menu-item>
            <a-menu-item key="6">
              option6
            </a-menu-item>
            <a-menu-item key="7">
              option7
            </a-menu-item>
            <a-menu-item key="8">
              option8
            </a-menu-item>
          </a-sub-menu>
          <a-sub-menu key="sub3">
            <span slot="title"><a-icon type="notification" />subnav 3</span>
            <a-menu-item key="9">
              option9
            </a-menu-item>
            <a-menu-item key="10">
              option10
            </a-menu-item>
            <a-menu-item key="11">
              option11
            </a-menu-item>
            <a-menu-item key="12">
              option12
            </a-menu-item>
          </a-sub-menu>
        </a-menu>
      </a-layout-sider>
      <a-layout style="padding: 0 24px 24px">
        <a-breadcrumb style="margin: 16px 0">
          <a-breadcrumb-item>Home</a-breadcrumb-item>
          <a-breadcrumb-item>List</a-breadcrumb-item>
          <a-breadcrumb-item>App</a-breadcrumb-item>
        </a-breadcrumb>
        <a-layout-content
          :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '280px' }"
        >
          Content
        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-layout>
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

#components-layout-demo-top-side-2 .logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 28px 16px 0;
  float: left;
}
</style>
