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
    <div style="margin-top: 20px;">
  
      <div style="text-align: end;">

        <a-button class="editable-add-btn" @click="clickAdd()">
          Add
        </a-button>
        <a-upload 
            name="file"
            :multiple="false"
            :action='clAction'
            @change="uploadFilecl"
            :file-list="fileListcl"
            :before-upload="beforeUploadcl" 
        >
            <a-button style="margin-right: 10px;"> <a-icon type="upload" 
              /> Import CILOs </a-button>
        </a-upload>
      </div>
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
    title: 'CILO',
    key: 'evam',
    dataIndex: 'evam',
    align: 'center',
    width: '180px'
  },
  {
    title: 'Content',
    dataIndex: 'percentage',
    key: 'percentage',
    align: 'center',
  },
  {
    title: 'Dependenced CILOs',
    key: 'tags',
    dataIndex: 'tags',
    scopedSlots: {customRender: 'tags'},
    align: 'center',
    width: '240px'
  },
  {
    title: 'Action',
    key: 'action',
    scopedSlots: {customRender: 'action'},
    align: 'center',
    width: '180px'
  },
];

export default {
  name: "CiloTable",
  components: {
    ModifyCiloModel
  },
  deactivated() {
    this.data = [];
    this.counter = 1;
    this.visible = false;
  },
  data() {
    return {
      data: [],
      columns,
      counter: 1,
      visible: false,
    };
  },
  mounted() {
    this.clickAdd()
  },
  methods: {
    updateRowData(name, info) {
      let cilo_list = []
      for (let i = 0; i < this.data.length; i++) {
        if (this.data[i].evam === name) {
          this.data[i].evam = info.evam === "" ? this.data[i].evam : info.evam;
          this.$store.commit("pushCilos", this.data[i].evam)
          this.data[i].percentage = info.percentage === "" ? this.data[i].percentage : info.percentage;
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
        evam: 'CILO ' + this.counter,
        visible: false
      })
      this.counter++;
      console.log(this.data);
    },
    clickDelete(key) {
      const dataSource = [...this.data];
      this.counter--;
      this.data = dataSource.filter(item => item.evam !== key);
    },

    beforeUploadcl(file){
      const isXlsx = file.type === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet';
      if (!isXlsx) {
        this.$message.error('Please upload a .xlsx file!');
        this.fileListcl = []
      }
      return isXlsx;
    },
    uploadFilecl(info){
      this.importfile(info.file)  
    },
    importfile (obj) {
     const _this = this
     const reader = new FileReader()
     _this.data = []
     _this.columns = []
     reader.readAsArrayBuffer(obj.originFileObj)
     reader.onload = function () {
       const buffer = reader.result
       const bytes = new Uint8Array(buffer)
       const length = bytes.byteLength
       let binary = ''
       for (let i = 0; i < length; i++) {
         binary += String.fromCharCode(bytes[i])
       }
        const XLSX = require('xlsx')
        const wb = XLSX.read(binary, {
          type: 'binary'
        })
        const outdata = XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]])
        //console.log(outdata)
        let tableheader = outdata[0]
        for(let val in tableheader){
          _this.columns.push({
            title: val,
            dataIndex: val,
            key: val,
          })
          this.counter++;
        }
        outdata.forEach((v,i)=>{
          v={...v,"key":i}
        })
        _this.data = outdata        
      }
    },
  }
}
</script>

<style scoped>

</style>
