<template>
  <vue-scroll style="height: 100%">
    <div class="createNew">
      <a-form-model ref="ruleForm" :model="form" :rules="rules" layout="vertical">
        <!--    :label-col="labelCol" :wrapper-col="wrapperCol"-->
        <a-row type="flex" justify="space-between">
          <a-col class="horizTwo" :span="10">
            <a-form-model-item ref="name" label="Course Name" prop="cname" validate-status="success">
              <a-input disabled="disabled" v-model="form.cname" @blur="() => {$refs.name.onFieldBlur();}"/>
            </a-form-model-item>
          </a-col>
          <a-col class="horizTwo" :span="10">
            <a-form-model-item ref="name" label="Course Code" prop="code" validate-status="success">
              <a-input v-model="form.code" @blur="() => {$refs.name.onFieldBlur();}"/>
            </a-form-model-item>
          </a-col>
        </a-row>
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
            <a-form-model-item ref="name" label="CILOs" prop="cilo" style="margin-bottom: 0;">
              <CiloTable/>
            </a-form-model-item>
          </a-col>
        </a-row>
        <a-row type="flex" justify="space-between">
          <a-col class="horizTwo" :span="22">
            <a-form-model-item ref="name" label="Assessments" prop="assessments" style="margin-bottom: 0;">
              <AssessmentTable/>
            </a-form-model-item>
          </a-col>
        </a-row>
        <a-row type="flex" justify="space-between">
          <a-col class="horizTwo" :span="22">
            <a-form-model-item label="Type" prop="type">
              <a-radio-group v-model="form.type">
                <a-radio value="MR">
                  Major Required (MR)
                </a-radio>
                <a-radio value="ME">
                  Major Election (ME)
                </a-radio>
                <a-radio value="GE">
                  Gradual Election (GE)
                </a-radio>
                <a-radio value="FE">
                  Free Election (FE)
                </a-radio>
              </a-radio-group>
            </a-form-model-item>
          </a-col>
        </a-row>
        <a-row type="flex" justify="end">
          <a-col :span="12">
            <a-form-model-item :wrapper-col="{ span: 14, offset: 10 }">
              <a-button type="primary" style="margin-right: 15px;" @click="onSubmit">
                Confirm
              </a-button>
              <a-button style="margin-right: 15px;">
                <router-link to="/designer/designerhome"> Cancel</router-link>
              </a-button>
            </a-form-model-item>
          </a-col>
        </a-row>
      </a-form-model>
    </div>
  </vue-scroll>
</template>
<script>
import YearSelector from "./YearSelector";
import DynamicForm from "./DynamicForm";
import AssessmentTable from "./AssessmentTable";
import CiloTable from "./CiloTable";
import axios from "axios";


export default {
  name: "ModifyCourse",
  components: {
    YearSelector, DynamicForm, AssessmentTable, CiloTable
  },
  mounted() {
    this.setProgramData();
  },
  data() {
    return {
      search_data: [],
      value: [],
      labelCol: {span: 24},
      wrapperCol: {span: 12},
      program_data: undefined,
      form: {
        cname: this.$route.params.coursename,
        code: '',
        cilo: '',
        assessments: '',
        program: '',
        startDate: undefined,
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
          {required: false, message: 'Please input the cilo name!', trigger: 'blur'},
        ],
        assessments: [
          {required: false, message: 'Please input the assessments name!', trigger: 'blur'},
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
    handleChange(value) {
      Object.assign(this, {
        value,
        search_data: [],
      });
    },
    async fetchCourse(query) {
      let url = "http://127.0.0.1:8000/course?size=20&search=" + query;
      let data;
      //异步访问cilo search api以获取数据
      await axios.get(url).then((res) => {
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
        // If some error occurs
        console.log(e);
      });
      return data;
    },
    async onSubmit() {
      let url = "http://127.0.0.1:8000/api/course/";
      let url_as = "http://127.0.0.1:8000/api/assessment/";
      this.$refs.ruleForm.validate(async valid => {
        if (valid) {
          let percentage_sum = 0;
          for (let i = 0; i < this.$store.state.as_form.percentage.length; i++) {
            percentage_sum += this.$store.state.as_form.percentage[i]
          }
          if (percentage_sum !== 100 && percentage_sum !== 0) {
            this.$message.error("The sum of the percentage must equals to 100%!")
            return;
          }

          let as_form_param = this.$store.state.as_form
          let as_id = 0;
          /*await axios.post(url_as, as_form_param).then(async (res) => {
            if (res.data) { // If success then
              // console.log(res.data);
              console.log(res.data)
              as_id = res.data.assessment_id
              this.$store.commit("set_course_form", {
                course_name: this.form.cname,
                course_code: this.form.code,
                program: this.form.program,
                type: this.form.type,
                assessment: as_id
              })
              console.log("create course form: ", this.$store.state.create_course_form)
              await axios.post(url, this.$store.state.create_course_form).then((res) => {
                // console.log(res.data);
                if (res.data) { // If success then
                  console.log(res.data);
                } else {// If not then
                  console.log(res.data);
                }
              }).catch(e => {
                console.log(e)
              })
            } else {// If not then
            }
          })*/
          this.$message.success("Create Successfully!")
          await this.$router.push({name: 'designerhome'});
          // console.log("as_form: ", this.$store.state.as_form)
          // alert('submit!');
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

.createNew {
  height: 100%;
  width: 100%;
  position: relative;
}
</style>
