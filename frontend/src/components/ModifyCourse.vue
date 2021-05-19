<template>
  <a-form-model ref="ruleForm" :model="form" :rules="rules" :label-col="labelCol" :wrapper-col="wrapperCol">
    <a-row>
      <a-form-model-item ref="name" label="Course Name" prop="cname" validate-status="success">
        <a-input v-model="form.cname" @blur="() => {$refs.name.onFieldBlur();}"/>
      </a-form-model-item>
      <a-form-model-item label="Academic Start Year" prop="startDate">
        <YearSelector v-model="form.startDate"></YearSelector>
      </a-form-model-item>
    </a-row>
    <!--    <a-form-model-item ref="name" label="CILOs" prop="cilo">-->
    <!--      <a-input v-model="form.cilo" @blur="() => {$refs.name.onFieldBlur();}"/>-->
    <!--    </a-form-model-item>-->
    <a-form-model-item ref="name" label="Assessments & CILOs" prop="cilo">
      <aaa></aaa>
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
      <a-checkbox-group v-model="form.type">
        <a-checkbox value="1" name="type">
          Online
        </a-checkbox>
        <a-checkbox value="2" name="type">
          Promotion
        </a-checkbox>
        <a-checkbox value="3" name="type">
          Offline
        </a-checkbox>
      </a-checkbox-group>
    </a-form-model-item>
    <a-form-model-item :wrapper-col="{ span: 8, offset: 14 }">
      <a-button type="primary" @click="onSubmit">
        Modify
      </a-button>
      <a-button style="margin-left: 10px;" @click="resetForm">
        Reset
      </a-button>
    </a-form-model-item>
  </a-form-model>
</template>
<script>
import YearSelector from "./YearSelector";
import DynamicForm from "./DynamicForm";
import aaa from "./aaa";


export default {
  name: "ModifyCourse",
  components: {
    YearSelector, DynamicForm, aaa
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
  },
};
</script>

<style scoped>
</style>
