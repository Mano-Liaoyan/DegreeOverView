<template>
  <div>
    <a-table :columns="columns" :data-source="data" :pagination="false" bordered rowKey="index">
      <!--    <a slot="name" slot-scope="text">{{ text }}</a>-->
      <!--    <span slot="customTitle"><a-icon type="smile-o"/> Name</span>-->
      <template v-for="col in ['evam', 'percentage', 'tags']" :slot="col"
                slot-scope="text, record, index">
        <div v-if="col==='evam'" :key="col">
          <a-input style="margin: -5px 0"/>
        </div>
        <div v-if="col==='percentage'" :key="col">
          <a-input-number :default-value="20" :min="0" :max="100" :formatter="value => `${value}%`"
                          :parser="value => value.replace('%', '')" style="text-align: center;"/>
        </div>
        <div v-if="col==='tags'" :key="col">
          <AutoHiddenSelector/>
        </div>
      </template>
      <span slot="action" slot-scope="text, record">
        <a @click="clickDelete(record.evam)">Delete</a>
      </span>
    </a-table>
    <div style="text-align: end;margin-top: 20px;">
      <a-button class="editable-add-btn" @click="clickAdd()">
        Add
      </a-button>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import AutoHiddenSelector from "./AutoHiddenSelector"

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
    align: 'center',
    scopedSlots: {customRender: 'evam'},
    width: "380px",
  },
  {
    title: 'Percentage',
    dataIndex: 'percentage',
    key: 'percentage',
    align: 'center',
    scopedSlots: {customRender: 'percentage'},
    width: "140px",
  },
  {
    title: 'CILOs',
    key: 'tags',
    dataIndex: 'tags',
    scopedSlots: {customRender: 'tags'},
    align: 'center',
    width: "380px",
  },
  {
    title: 'Action',
    key: 'action',
    scopedSlots: {customRender: 'action'},
    align: 'center',
    width: "140px",
  },
];

let data = [
  // {
  //   evam: 'Assignments/Quizzes',
  //   percentage: '15%',
  //   tags: [],
  //   visible: false
  // },
  /*  {
      evam: 'Labs',
      percentage: '25%',
      tags: [],
      visible: false
    },
    {
      evam: 'Projects',
      percentage: '10%',
      tags: [],
      visible: false
    },
    {
      evam: 'Examination',
      percentage: '50%',
      tags: [],
      visible: false
    },*/
];

export default {
  name: "AssessmentTable",
  components: {
    AutoHiddenSelector
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
    updateRowData(name, info) {
      for (let i = 0; i < this.data.length; i++) {
        if (this.data[i].evam === name) {
          this.data[i].evam = info.evam === "" ? this.data[i].evam : info.evam;
          this.data[i].percentage = info.percentage === "%" ? this.data[i].percentage : info.percentage;
          this.data[i].tags = info.tags === [] ? this.data[i].tags : info.tags;
        }
      }
    },
    changeVisibleToFalse(key) {
      // this.visible = false;
      for (let i = 0; i < this.data.length; i++) {
        if (this.data[i].evam === key)
          this.data[i].visible = false;
      }
    },
    showModal(key) {
      for (let i = 0; i < this.data.length; i++) {
        if (this.data[i].evam === key)
          this.data[i].visible = true;
      }
    },
    clickAdd() {
      this.data.push({
        index: this.counter,
        percentage: '',
        tags: [],
        evam: 'New Method' + this.counter,
        visible: false
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
