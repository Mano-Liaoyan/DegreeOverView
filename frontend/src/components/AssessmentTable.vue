<template>
  <div>
    <a-table :columns="columns" :data-source="data" :pagination="false" bordered rowKey="index">
      <!--    <a slot="name" slot-scope="text">{{ text }}</a>-->
      <!--    <span slot="customTitle"><a-icon type="smile-o"/> Name</span>-->
      <span slot="tags" slot-scope="tags">
        <a-tag v-for="tag in tags" :key="tag"
               :color="tag === 'loser' ? 'volcano' : tag.length > 5 ? 'geekblue' : 'green'">
          {{ tag.toUpperCase() }}
        </a-tag>
      </span>
      <span slot="action" slot-scope="text, record">
        <a @click="showModal(record.evam)">Modify</a>
        <a-divider type="vertical"/>
        <a @click="clickDelete(record.evam)">Delete</a>
        <ModifyCiloModel :ev_name="record.evam" @update="updateRowData" :visible="record.visible"
                         @changeVisibleToFalse="changeVisibleToFalse(record.evam)"/>
      </span>
    </a-table>
    <div style="text-align: end;margin-top: 20px;">
      <a-button class="editable-add-btn" @click="clickAdd()">
        Add
      </a-button>
      <a-button class="editable-add-btn" @click="clickPost()">
        Post Assessment
      </a-button>
    </div>
  </div>
</template>
<script>
import ModifyCiloModel from "./ModifyCiloModel";
import axios from "axios";

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
    async clickPost() {
      /*let url = "http://127.0.0.1:8000/api/assessment/";
      let params = {
        evaluation_method: [],
        percentage: [],
        cilos_arr: [],
        cilos: []
      };
      for (let i = 0; i < this.data.length; i++) {
        params.evaluation_method.push(this.data[i].evam)
        params.percentage.push(this.data[i].percentage)
        params.cilos_arr.push(this.data[i].tags)
        for (let j = 0; j < this.data[i].tags.length; j++) {
          params.cilos.push(parseInt(this.data[i].tags[j]))
        }
      }

      let res_data;
      //异步访问cilo search api以获取数据
      await axios.post(url, params).then((res) => {
        if (res.data.assessment_id !== '') { // If success then
          console.log(res.data);
          res_data = res.data;
        } else {// If not then
          // console.log(res.data);
          this.search_data = []
        }
      }).catch((e) => {
        // If some error occurs
        // console.log(this.data)
        if (JSON.stringify(e.response.data.cilos))
          this.$message.error('cilos:' + JSON.stringify(e.response.data.cilos[0]))

      });
      return data;*/
    },
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
