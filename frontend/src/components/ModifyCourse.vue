<template>
  <a-form-model ref="ruleForm" :model="form" :rules="rules" layout="vertical">
    <!--    :label-col="labelCol" :wrapper-col="wrapperCol"-->
    <a-row type="flex" justify="space-between">
      <a-col class="horizTwo" :span="10">
        <a-form-model-item ref="name" label="Course Name" prop="cname" validate-status="success">
          <a-input v-model="form.cname" @blur="() => {$refs.name.onFieldBlur();}"/>
        </a-form-model-item>
      </a-col>
      <a-col class="horizTwo" :span="10">
        <a-form-model-item ref="name" label="Course Code" prop="code" validate-status="success">
          <a-input v-model="form.code" @blur="() => {$refs.name.onFieldBlur();}"/>
        </a-form-model-item>
      </a-col>
    </a-row>
    <!--    <a-form-model-item ref="name" label="CILOs" prop="cilo">-->
    <!--      <a-input v-model="form.cilo" @blur="() => {$refs.name.onFieldBlur();}"/>-->
    <!--    </a-form-model-item>-->
    <!--    <DynamicForm></DynamicForm>-->
    <a-row type="flex" justify="space-between">
      <a-col class="horizTwo" :span="10">
        <a-form-model-item label="Academic Start Year" prop="startDate">
          <YearSelector v-model="form.startDate"></YearSelector>
        </a-form-model-item>
      </a-col>
      <a-col class="horizTwo" :span="10">
        <a-form-model-item label="Program" prop="program">
          <a-select v-model="form.program" placeholder="please select your programme">
            <a-select-option v-for="(item, index) in program_data" :key="index" :value="item">
              {{ item }}
            </a-select-option>
          </a-select>
        </a-form-model-item>
      </a-col>
    </a-row>
    <a-row type="flex" justify="space-between">
      <a-col class="horizTwo" :span="22">
        <a-form-model-item ref="name" label="Prerequisites" prop="prerequisites">
          <a-input v-model="form.prerequisites" @blur="() => {$refs.name.onFieldBlur();}"/>
        </a-form-model-item>
      </a-col>
    </a-row>
    <a-row type="flex" justify="space-between">
      <a-col class="horizTwo" :span="22">
        <a-form-model-item ref="name" label="Assessments&CILOs" prop="cilo" style="margin-bottom: 0;">
          <AsAndCiloTable/>
        </a-form-model-item>
      </a-col>
    </a-row>
    <a-row type="flex" justify="space-between">
      <a-col class="horizTwo" :span="22">
        <a-form-model-item label="Type" prop="type">
          <a-radio-group v-model="form.type">
            <a-radio value="1">
              Major Required (MR)
            </a-radio>
            <a-radio value="2">
              Major Election (ME)
            </a-radio>
            <a-radio value="3">
              Gradual Election (GE)
            </a-radio>
            <a-radio value="4">
              Free Election (FE)
            </a-radio>
          </a-radio-group>
        </a-form-model-item>
      </a-col>
    </a-row>
    <a-row type="flex" justify="end">
      <a-col :span="12">
        <a-form-model-item :wrapper-col="{ span: 8, offset: 14 }">
          <a-button type="primary" @click="onSubmit">
            Modify
          </a-button>
          <a-button style="margin-left: 10px;" @click="resetForm">
            Reset
          </a-button>
        </a-form-model-item>
      </a-col>
    </a-row>
  </a-form-model>
</template>
<script>
import YearSelector from "./YearSelector";
import DynamicForm from "./DynamicForm";
import aaa from "./aaa";
import AsAndCiloTable from "./AsAndCiloTable";
import axios from "axios";


export default {
  name: "ModifyCourse",
  components: {
    YearSelector, DynamicForm, aaa, AsAndCiloTable
  },
  mounted() {
    this.setProgramData();
  },
  data() {
    return {
      labelCol: {span: 24},
      wrapperCol: {span: 12},
      program_data: undefined,
      form: {
        cname: '',
        code: '',
        cilo: '',
        program: '',
        prerequisites: '',
        relation: '',
        startDate: undefined,
        delivery: false,
        type: '',
      },
      rules: {
        cname: [
          {required: true, message: 'Please input the course name!', trigger: 'blur'},
        ],
        code: [
          {required: true, message: 'Please input the course code!', trigger: 'blur'},
        ],
        cilo: [
          {required: true, message: 'Please input the cilo name!', trigger: 'blur'},
        ],
        program: [
          {required: true, message: 'Please input the programme name!', trigger: 'blur'},
        ],
        type: [
          {required: true, message: 'Please select activity resource', trigger: 'change'},
        ],
      },
    };
  },
  methods: {
    onSubmit() {
      this.$refs.ruleForm.validate(valid => {
        if (valid) {
          alert('submit!');
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm() {
      this.$refs.ruleForm.resetFields();
    },
    async setProgramData() {
      let url = "http://127.0.0.1:8000/api/course/get_all_program/";
      let data;
      //异步访问cilo search api以获取数据
      await axios.get(url).then((res) => {
        // console.log(res.data);
        if (res.data) { // If success then
          // console.log(res.data);
          this.program_data = res.data.programs
        } else {// If not then
          // console.log(res.data);
          data = res.data;
          this.program_data = undefined
        }
      }).catch((e) => {
        // If some error occurs
        console.log(e);
      });
    },
  },
};
</script>

<style scoped>
.horizTwo {
  margin: auto
}
</style>
