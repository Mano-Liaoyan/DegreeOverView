<template>
  <div>
    <a-table :columns="columns" :data-source="data" :pagination="false" bordered rowKey="index">
      <template v-for="col in ['evam', 'percentage', 'tags']" :slot="col"
                slot-scope="text, record, index">
        <div v-if="col==='evam'" :key="col">
          <a-input style="margin: -5px 0" @change="e=>onEvamChange(e,record.index)"/>
        </div>
        <div v-if="col==='percentage'" :key="col">
          <a-input-number :min="0" :max="100"
                          :formatter="value => `${value}%`" @change="value=>onPercentChange(value,record.index)"
                          :parser="value => value.replace('%', '')" style="text-align: center;"/>
        </div>
        <div v-if="col==='tags'" :key="col">
          <a-input placeholder="e.g. 1-2" style="margin: -5px 0" @change="e=>onCiloChange(e,record.index)"/>
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


const columns = [
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

export default {
  name: "AssessmentTable",
  data() {
    return {
      data: [],
      columns,
      evam: [],
      percentage: [],
      selected_cilos: [],
      counter: 1,
      visible: false,
    };
  },
  methods: {
    onEvamChange(e, index) {
      this.evam[index] = e.target.value
      console.log('evam: ', this.evam)
    },
    onPercentChange(value, index) {
      this.percentage[index] = value
      console.log('percentage: ', this.percentage)
    },
    /*    onCiloChange(value, index) {
          for (let i = 0; i < value.length; i++) {
            // console.log(value[i].trim().split(/\s+/)[1])
            value[i] = value[i].trim().split(/\s+/)[1] - 1
            console.log('value ', value[i])
          }

          for (let j = 0; j < value.length; j++) {
            value[j] = this.$store.state.create_course_form.cilos[value[j]];
          }

          this.selected_cilos[index] = value
          console.log('selected_cilos: ', this.selected_cilos)
        },*/
    onCiloChange(e, index) {
      this.selected_cilos[index] = e.target.value
      console.log('evam: ', this.selected_cilos)
    },
    updateRowData(name, info) {
      let as_list = [];
      for (let i = 0; i < this.data.length; i++) {
        if (this.data[i].evam === name) {
          this.data[i].evam = info.evam === "" ? this.data[i].evam : info.evam;
          this.data[i].percentage = info.percentage === "%" ? this.data[i].percentage : info.percentage;
          this.data[i].tags = info.tags === [] ? this.data[i].tags : info.tags;
        }
        as_list.push(this.data[i])
      }
      this.$store.commit("set_course_form", {
        assessments: as_list
      })
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
