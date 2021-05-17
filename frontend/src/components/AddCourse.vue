<template>
  <div class="addcourse">
    <div>
      <a-row type="flex" justify="space-around" align="top"/>
      <a-row type="flex" justify="space-around" align="middle">
        <a-col :span="6"/>
        <a-col :span="12">
          <div id="addcourse">
            <h2>Add Course</h2>
            <a-form layout="inline" :form="form" @submit="handleSubmit">
              <a-form-item>
                <a-input
                  v-decorator="[
                    'coursename',
                    { rules: [{ required: true, message: 'Please input course name!' }] },
                  ]"
                  placeholder="input course name here"
                >
                </a-input>
              </a-form-item>
              <a-form-item>
                <!-- <a-button type="primary" html-type="submit" :disabled="hasErrors(form.getFieldsError())"> -->
                <a-button type="primary" html-type="submit">
                  Confirm
                </a-button>
              </a-form-item>
            </a-form>
            <a-button>Cancel</a-button>
          </div>
        </a-col>
        <a-col :span="6"/>
      </a-row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AddCourse',
  data() {
    return {
      // msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
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
