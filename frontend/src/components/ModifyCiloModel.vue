<template>
  <div>
    <a-modal title="Modify" :visible="isVisible" :confirm-loading="confirmLoading" @ok="handleOk" @cancel="handleCancel" centered>
      <a-row type="flex" justify="space-between" style="margin-top: -19px;">
        <a-col>
          <a-input v-model="evam_name" placeholder="Evaluation Method Name"/>
        </a-col>
        <a-col>
          <!--          <a-input v-model="percentage" placeholder="percentage" suffix="%"/>-->
          Percentage:
          <a-input-number :default-value="20" v-model="percentage" :min="0" :max="100" :formatter="value => `${value}%`"
                          :parser="value => value.replace('%', '')"/>
        </a-col>
      </a-row>
      <h4 style="margin-top: 5px;">New Cilo</h4>
      <a-textarea v-model="text_content" placeholder="Please input the cilo content" allow-clear/>
      <div style="text-align: end;margin-top: 5px;">
        <a-button type="primary" @click="addNewCilo">
          Add new CILO
        </a-button>
      </div>
      <h4 style="margin-top: -19px;">Existing Cilo</h4>
      <a-select mode="multiple" :value="value" placeholder="Select Cilos"
                style="width: 100%" :filter-option="false" :not-found-content="fetching ? undefined : null"
                @search="fetchCilo" @change="handleChange">
        <a-spin v-if="fetching" slot="notFoundContent" size="small"/>
        <a-select-option v-for="data in filteredOptions" :key="data.cilo_id" @click="handleClickOption(data)">
          {{ data.cilo_id }} {{ data.content }}
        </a-select-option>
      </a-select>
      <a-table :columns="columns" :data-source="data" :pagination="false" bordered rowKey="cilo_id" style="margin-top: 10px;"/>
    </a-modal>
  </div>
</template>

<script>
import axios from "axios";

const columns = [
  {
    title: 'CILO_ID',
    key: 'cilo_id',
    dataIndex: 'cilo_id',
    align: 'center'
  },
  {
    title: 'Content',
    dataIndex: 'content',
    key: 'content',
    align: 'center'
  },
];

export default {
  name: "ModifyCiloModel",
  props: {
    visible: undefined,
    ev_name: ''
  },
  mounted() {
    this.value_length = this.valueLength;
  },
  computed: {
    isVisible() {
      return this.visible;
    },
    valueLength() {
      return this.value.length;
    },
    filteredOptions() {
      return this.search_data.filter(o => !this.value.includes(o.cilo_id));
    }
  },
  data() {
    return {
      confirmLoading: false,
      columns,
      data: [],
      search_data: [],
      value: [],
      fetching: false,
      text_content: '',
      evam_name: '',
      percentage: '',
      value_length: 0,
    };
  },
  methods: {
    handleOk(e) {
      this.confirmLoading = true;
      let info = {
        evam: this.evam_name,
        percentage: this.percentage + '%',
        tags: [],
      }
      for (let i = 0; i < this.value.length; i++) {
        info.tags.push(this.value[i].toString());
      }
      setTimeout(() => {
        this.$emit("update", this.ev_name, info)
        this.$emit('changeVisibleToFalse');
        this.confirmLoading = false;
      }, 500);

    },
    handleCancel(e) {
      console.log('Clicked cancel button');
      // this.visible = false;
      this.$emit('changeVisibleToFalse');
    },
    handleChange(value) {
      Object.assign(this, {
        value,
        search_data: [],
        fetching: false,
      });
      if (this.valueLength < this.value_length) {
        console.log("cilo values ", value)
        console.log('before removed: ', this.data)
        for (let i = 0; i < this.data.length; i++) {
          console.log(!value.includes(this.data[i].cilo_id))
          if (!value.includes(this.data[i].cilo_id)) {
            this.data.splice(i, 1);
          }
        }
        console.log('after removed: ', this.data)
      }
      this.value_length = this.valueLength;
    },

    async addNewCilo() {
      let url = "http://127.0.0.1:8000/api/cilo/";
      let params = {
        content: this.text_content
      };
      let res_data;
      //异步访问cilo search api以获取数据
      await axios.post(url, params).then((res) => {
        if (res.data.content === params.content) { // If success then
          console.log(res.data);
          res_data = res.data;
          this.value.push(res_data.cilo_id)
          Object.assign(this, {
            value: this.value,
            search_data: [],
            fetching: false,
          });
          this.value_length = this.valueLength // Update the length cache
          this.data.push({
            cilo_id: res_data.cilo_id,
            content: res_data.content,
          },)
          this.text_content = "";// Empty the text area
        } else {// If not then
          // console.log(res.data);
          this.search_data = []
          data = res.data;
        }
      }).catch((e) => {
        // If some error occurs
        console.log(e);
      });
      return data;
    },

    handleClickOption(data) {
      this.data.push({
        cilo_id: data.cilo_id,
        content: data.content,
      },)
    },

    async fetchCilo(query) {
      this.fetching = true;
      let url = "http://127.0.0.1:8000/cilo?size=20&search=" + query;
      let data;
      //异步访问cilo search api以获取数据
      await axios.get(url).then((res) => {
        this.fetching = false;
        // console.log(res.data);
        console.log(res.data)
        if (res.data.count !== 0) { // If success then
          // console.log(res.data);
          this.search_data = res.data.results
          data = res.data;
        } else {// If not then
          // console.log(res.data);
          this.search_data = []
          data = res.data;
        }
      }).catch((e) => {
        this.fetching = false;
        // If some error occurs
        console.log(e);
      });
      return data;
    }
  }
}
</script>

<style scoped>
.ant-modal-body {
  padding-top: 5px !important;
}
</style>
