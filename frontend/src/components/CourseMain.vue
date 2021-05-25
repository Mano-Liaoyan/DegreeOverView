<template>
  <div class="coursemain">
    <h1 style="text-align: center; font-weight: bold;">Please fill in the following information</h1>
    <br>
    <a-form-model ref="ruleForm" :model="form" :rules="rules" :label-col="labelCol" :wrapper-col="wrapperCol">
      <a-row>
        <a-form-model-item label="Course Name">
          <a-input model="form.cname" placeholder="course name" disabled=true></a-input>
        </a-form-model-item>
        <a-form-model-item label="Academic Start Year" prop="startDate">
          <YearSelector v-model="form.startDate"></YearSelector>
        </a-form-model-item>
      </a-row>
       <!--    <a-form-model-item ref="name" label="CILOs" prop="cilo">-->
    <!--      <a-input v-model="form.cilo" @blur="() => {$refs.name.onFieldBlur();}"/>-->
    <!--    </a-form-model-item>-->
      <a-form-model-item ref="name" label="CILOs" prop="cilo">
        <a-button type="primary">
          Edit CILOs
        </a-button>
        <a-upload 
          :multiple="false"         
         @change="handleChange"
         accept="application/vnd.ms-excel, 
            application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" 
        >
          <a-button style="margin-left: 10px;"> <a-icon type="upload" 
          /> Import CILOs </a-button>
        </a-upload>
      </a-form-model-item>
       <a-form-model-item ref="name" label="Assessments" prop="cilo">
        <a-button type="primary">
          Edit Assessment
        </a-button>
        <a-upload
          action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
          :default-file-list="defaultFileList"
          accept="application/vnd.ms-excel, 
            application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" 
        >
          <a-button style="margin-left: 10px;"> <a-icon type="upload" /> Import Assessment methods </a-button>
        </a-upload>
      </a-form-model-item>
      <!--    <DynamicForm></DynamicForm>-->
      <a-form-model-item ref="name" label="Programme" prop="programme" style="margin-top: -10px">
        <a-input v-model="form.programme" @blur="() => {$refs.name.onFieldBlur();}"/>
      </a-form-model-item>
      <a-form-model-item ref="name" label="Prerequisites" prop="prerequisites">
        <a-input v-model="form.prerequisites" @blur="() => {$refs.name.onFieldBlur();}"/>
      </a-form-model-item>
      <a-form-model-item ref="name" label="Relation" prop="relation">
        <a-input v-model="form.relation" @blur="() => {$refs.name.onFieldBlur();}"/>
      </a-form-model-item>
      <a-form-model-item label="Type" prop="type">
      <a-radio-group v-model="form.type">
        <a-radio value="1" name="type">
          Major Required (MR)
        </a-radio>
        <a-radio value="2" name="type">
          Major Election (ME)
        </a-radio>
        <br>
        <a-radio value="3" name="type">
          Gradual Election (GE)
        </a-radio>
        <a-radio value="4" name="type">
          Free Election (FE)
        </a-radio>
      </a-radio-group>
      </a-form-model-item>
      <a-form-model-item>
        <div style="float: left; padding-left: 100px;" >
          <a-button type="primary" @click="() => openNotificationWithIcon('success')">
            Confirm
          </a-button>
        </div>
        <div style="float: right;" >
          <a-button @click="resetForm">
            <router-link to="/designer"> Cancel </router-link>
          </a-button>
        </div>
      </a-form-model-item>
    </a-form-model>
  </div>
</template>

<script>
import YearSelector from "./YearSelector";
import DynamicForm from "./DynamicForm";


export default {
  name: "ModifyCourse",
  components: {
    YearSelector, DynamicForm
  },
  data() {
    return {
      labelCol: {span: 4},
      wrapperCol: {span: 14},
      form: {
        cname: '',
        cilo: '',
        programme: '',
        prerequisites: '',
        relation: '',
        startDate: undefined,
        delivery: false,
        type: [],
      },
      fileList: [
        // files
      ],
      rules: {
        cname: [
          {required: true, message: 'Please input the course name!', trigger: 'blur'},
        ],
        cilo: [
          {required: true, message: 'Please input the cilo name!', trigger: 'blur'},
        ],
        programme: [
          {required: true, message: 'Please input the programme name!', trigger: 'blur'},
        ],
        type: [
          {
            type: 'array',
            required: true,
            message: 'Please select at least one course type',
            trigger: 'change',
          },
        ]
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
    openNotificationWithIcon(type) {
      this.$notification[type]({
        message: 'Successful!',
        description:
          'Added the course xxx successfully!',
      });
    },
    handleChange(info) {
      let fileList = [...info.fileList];

      // 1. Limit the number of uploaded files
      //    Only to show two recent uploaded files, and old ones will be replaced by the new
      fileList = fileList.slice(-2);

      // 2. read from response and show file link
      fileList = fileList.map(file => {
        if (file.response) {
          // Component will show file.url as link
          file.url = file.response.url;
        }
        return file;
      });

      this.fileList = fileList;
    },
    beforeUpload(file) {
      const isXlsxOrXls = file.type === 'xlsx' || file.type === 'xls';
      if (!isJpgOrPng) {
        this.$message.error('You can only upload JPG file!');
      }
      const isLt2M = file.size / 1024 / 1024 < 2;
      if (!isLt2M) {
        this.$message.error('Image must smaller than 2MB!');
      }
      return isJpgOrPng && isLt2M;
    },
  },
};
</script>

<style scoped>
.coursemain{
  height: 100%;
  width: 100%;
  position: relative;
}

</style>
