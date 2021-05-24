<template>
  <div class="viewperformance">
    <template>
      <a-form-model
        ref="ruleForm"
        :model="form"
        :rules="rules"
        :label-col="labelCol"
        :wrapper-col="wrapperCol"
      >
        <a-row>
          <a-form-model-item label="Course Name">
            <a-input />
          </a-form-model-item>
          <a-form-model-item label="Academic Start Year" prop="startDate">
            <YearSelector></YearSelector>
          </a-form-model-item>
        </a-row>
        <a-form-model-item :wrapper-col="{ span: 8, offset: 14 }">
          <a-button type="primary" @click="onSubmit"> Confirm </a-button>
          <a-button style="margin-left: 10px"> Cancel </a-button>
        </a-form-model-item>
      </a-form-model>
    </template>
  </div>
</template>

<script>
import YearSelector from "./YearSelector";

export default {
  name: "ViewPerformance",
  components: {
    YearSelector
  },
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
