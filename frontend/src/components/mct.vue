<template>
  <div class="modify-course">
    <template>
      <a-form :form="form" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }" @submit="handleSubmit">
        <a-form-item label="Course name">
          <a-input v-decorator="[
              'coursename',
              {
                rules: [
                  { required: true, message: 'Please input the course name!', trigger: 'blur' },
                ],
              },
            ]"
          />
        </a-form-item>
        <a-form-item label="CILOs">
          <a-input
            v-decorator="[
              'cilos',
              {
                rules: [{ required: true, message: 'Please input the cilos!', trigger: 'blur' }],
              },
            ]"
          />
        </a-form-item>
        <a-form-item label="Assessments">
          <a-input
            v-decorator="[
              'assessments',
              {
                rules: [
                  { required: true, message: 'Please input the assessments!', trigger: 'blur' },
                ],
              },
            ]"
          />
        </a-form-item>
        <a-form-item label="Relationship">
          <a-input
            v-decorator="[
              'relationship',
              {
                rules: [
                  { required: true, message: 'Please input the relationship!', trigger: 'blur' },
                ],
              },
            ]"
          />
        </a-form-item>
        <a-form-item label="Prerequisites">
          <a-input
            v-decorator="[
              'prerequisites',
              {
                rules: [
                  {
                    required: true,
                    message: 'Please input the prerequisites!',
                    trigger: 'blur'
                  },
                ],
              },
            ]"
          />
        </a-form-item>
        <a-form-item label="Programme">
          <a-input
            v-decorator="[
              'programme',
              {
                rules: [
                  { required: true, message: 'Please input the programme!', trigger: 'blur'  },
                ],
              },
            ]"
          />
        </a-form-item>
        <a-form-item label="Type">
          <a-input
            v-decorator="[
              'type',
              {
                rules: [{ required: true, message: 'Please input the type!', trigger: 'blur'  }],
              },
            ]"
          />
        </a-form-item>
        <a-form-item label="Start Academic Year">
          <a-input
            v-decorator="[
              'startacademicyear',
              {
                rules: [
                  {
                    required: true,
                    message: 'Please input the start academic year!',
                     trigger: 'blur'
                  },
                ],
              },
            ]"
          />
        </a-form-item>
        <a-form-item :wrapper-col="{ span: 12, offset: 5 }">
          <a-space :size="large">
            <a-button type="primary" html-type="submit"> Save</a-button>
            <a-button> Back</a-button>
          </a-space>
        </a-form-item>
      </a-form>
    </template>
  </div>
</template>

<script>
export default {
  name: "ModifyCourse",
  data() {
    return {
      form: this.$form.createForm(this),
    };
  },
  methods: {
    handleSubmit() {

    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
