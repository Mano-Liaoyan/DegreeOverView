<template>
  <div class="courseListforAnalysis">
    <template>
      <a-table :columns="columns" :data-source="data">
        <a slot="name" slot-scope="text">{{ text }}</a>
        <span slot="customTitle"><a-icon type="smile-o" /> Name</span>
        <span slot="tags" slot-scope="tags">
          <a-tag
            v-for="tag in tags"
            :key="tag"
            :color="
              tag === 'loser'
                ? 'volcano'
                : tag.length > 5
                ? 'geekblue'
                : 'green'
            "
          >
            {{ tag.toUpperCase() }}
          </a-tag>
        </span>
        <span slot="type"> 
          <a-dropdown>
            <a-menu slot="overlay" @click="handleMenuClick">
                <a-menu-item key="1"> <a-icon type="user" />1st menu item </a-menu-item>
                <a-menu-item key="2"> <a-icon type="user" />2nd menu item </a-menu-item>
                <a-menu-item key="3"> <a-icon type="user" />3rd item </a-menu-item>
            </a-menu>
            <a-button style="margin-left: 8px"> Select the analysis type <a-icon type="down" /> </a-button>
           </a-dropdown>
        </span>
         <span slot="action">
          <a-button> 
            <router-link to="/lecturer/chart"> Show Analysis </router-link>
           </a-button>
        </span>
      </a-table>
    </template>
  </div>
</template>

<script>
const columns = [
  {
    title: "Course Name",
    dataIndex: "name",
    key: "name",
  },
  {
    title: "Major",
    key: "tags",
    dataIndex: "tags",
    scopedSlots: { customRender: "tags" },
  },
  
  {
    title: "Type",
    key: "type",
    scopedSlots: { customRender: "type" },
  },
  {
    title: "Action",
    key: "action",
    scopedSlots: { customRender: "action" },
  },
];

const data = [
  {
    key: "1",
    name: "Discrete Math",
    tags: ["CST"],
  },
  {
    key: "2",
    name: "Computer Organization",
    tags: ["CST"],
  },
  {
    key: "3",
    name: "Orienter-Object Programming",
    tags: ["CST"],
  },
   {
    key: "4",
    name: "Structured Programming",
    tags: ["CST"],
  },
];

export default {
  name: "CLFD",
  data() {
    return {
      data,
      columns
    };
  },
  methods:{
    handleMenuClick(e) {
      console.log('click', e);
    },
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
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

.courseList{
  height: 100%;
  width: 100%;
  text-align: center;
}
</style>
