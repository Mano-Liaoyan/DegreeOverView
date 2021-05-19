<template>
  <div class="analysisresult">
    <template>
      <a-form :form="form" @submit="handleSubmit">
        <a-form-item label="Type of analysis">
          <a-select
            style="width: 360px"
            v-decorator="[
              'type',
              {
                rules: [{ required: true, message: 'Please select a type of analysis!' }],
              },
            ]"
            placeholder="Choose a type of analysis"
            @change="handleSelectChange"
          >
            <a-select-option value="1"> type 1 </a-select-option>
            <a-select-option value="2"> type 2 </a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item layout="inline">
          <a-space :size="large">
            <!-- <a-button type="primary" html-type="submit" :disabled="hasErrors(form.getFieldsError())"> -->
            <a-button type="primary" html-type="submit"> 
              <router-link to=""> Analysis </router-link>
              </a-button>
            <a-button> Back </a-button>
          </a-space>
        </a-form-item>
      </a-form>
    </template>
  </div>
</template>

<script>
export default {
  name: "AnalysisResult",
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
