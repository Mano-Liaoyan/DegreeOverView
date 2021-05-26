<template>
  <div>
    <a-table :columns="columns" :data-source="data" :pagination="false" bordered rowKey="evam">
      <!--    <a slot="name" slot-scope="text">{{ text }}</a>-->
      <!--    <span slot="customTitle"><a-icon type="smile-o"/> Name</span>-->
      <span slot="tags" slot-scope="tags">
        <a-tag :closable="true" v-for="tag in tags" :key="tag" :color="tag === 'loser' ? 'volcano' : tag.length > 5 ? 'geekblue' : 'green'">
          {{ tag.toUpperCase() }}
        </a-tag>
      </span>
      <span slot="action" slot-scope="text, record">
        <a @click="showModal">Modify</a>
        <a-divider type="vertical"/>
        <a @click="clickDelete(record.evam)">Delete</a>
      </span>
    </a-table>
    <div style="text-align: end;margin-top: 20px;">
      <a-button class="editable-add-btn" @click="clickAdd()">
        Add
      </a-button>
    </div>
    <div>
      <ModifyCiloModel :visible="visible" @changeVisibleToFalse="changeVisibleToFalse"/>
    </div>

  </div>
</template>
<script>
import ModifyCiloModel from "./ModifyCiloModel";

const columns = [
  /*  {
      dataIndex: 'name',
      key: 'name',
      slots: {title: 'customTitle'},
      scopedSlots: {customRender: 'name'},
      align: 'center'
    },*/
  {
    title: 'Evaluation Method',
    key: 'evam',
    dataIndex: 'evam',
    align: 'center'
  },
  {
    title: 'Percentage',
    dataIndex: 'percentage',
    key: 'percentage',
    align: 'center'
  },
  {
    title: 'CILOs',
    key: 'tags',
    dataIndex: 'tags',
    scopedSlots: {customRender: 'tags'},
    align: 'center'
  },
  {
    title: 'Action',
    key: 'action',
    scopedSlots: {customRender: 'action'},
    align: 'center'
  },
];

let data = [
  {
    evam: 'Assignments/Quizzes',
    percentage: '15%',
    tags: ['nice', 'developer'],
  },
  {
    evam: 'Labs',
    percentage: '25%',
    tags: ['loser'],
  },
  {
    evam: 'Projects',
    percentage: '10%',
    tags: ['cool', 'teacher'],
  },
  {
    evam: 'Examination',
    percentage: '50%',
    tags: ['cool', 'teacher'],
  },
];

export default {
  name: "AsAndCiloTable",
  components: {
    ModifyCiloModel
  },
  data() {
    return {
      data,
      columns,
      counter: 1,
      visible: false,
    };
  },
  methods: {
    changeVisibleToFalse() {
      this.visible = false;
    },
    showModal() {
      this.visible = true;
    },
    clickAdd() {
      this.data.push({
        percentage: '',
        tags: [],
        evam: 'New Method' + this.counter
      })
      this.counter++;
      console.log(this.data);
    },
    clickDelete(key) {
      const dataSource = [...this.data];
      this.data = dataSource.filter(item => item.evam !== key);
    }
  }
}
</script>

<style scoped>

</style>
