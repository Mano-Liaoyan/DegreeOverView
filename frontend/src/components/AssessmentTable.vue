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
      <a-upload 
            name="file"
            :multiple="false"
            :action='clAction'
            @change="uploadFilecl"
            :file-list="fileListcl"
            :before-upload="beforeUploadcl" 
          >
            <a-button style="margin-right: 10px;"> <a-icon type="upload" 
              /> Import Assessments </a-button>
        </a-upload>
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
      clAction: '',
      fileListcl: [],
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
      this.$store.commit("setAs", {
        evaluation_method: this.evam.filter(o => o)
      })
    },
    onPercentChange(value, index) {
      this.percentage[index] = value
      this.$store.commit("setAs", {
        percentage: this.percentage.filter(o => o)
      })
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
      this.$store.commit("setAs", {
        cilos_arr: this.selected_cilos.filter(o => o)
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
