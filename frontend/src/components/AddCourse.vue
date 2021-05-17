<template>
  <div class="addcourse">
    <template>
      <a-form :form="form" @submit="handleSubmit">
        <a-form-item>
          <a-input
            style="width: 360px"
            v-decorator="[
              'coursename',
              {
                rules: [
                  {
                    required: true,
                    message: 'Please input course name!',
                  },
                ],
              },
            ]"
            placeholder="input course name here"
          >
          </a-input>
        </a-form-item>
        <a-form-item layout="inline">
          <a-space :size="large">
            <!-- <a-button type="primary" html-type="submit" :disabled="hasErrors(form.getFieldsError())"> -->
            <a-button type="primary" html-type="submit"> Confirm </a-button>
            <a-button> Cancel </a-button>
          </a-space>
        </a-form-item>
      </a-form>
    </template>
  </div>
</template>

<script>
export default {
  name: "AddCourse",
  data() {
    return {
      // msg: 'Welcome to Your Vue.js App'
    };
  },
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
