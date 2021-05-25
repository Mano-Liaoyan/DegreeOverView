<template>
  <div class="definedependency">
    <div class="definedependencybox">
      <a-form :form="form" @submit="handleSubmit" :label-col="labelCol" :wrapper-col="wrapperCol">
        <a-form-item label="CILO1">
          <a-select
            style="width: 360px"
            v-decorator="[
              'cilo1',
              {
                rules: [{ required: true, message: 'Please select cilo1!' }],
              },
            ]"
            placeholder="cilo1"
            @change="handleSelectChange"
          >
            <a-select-option value="1"> 1 </a-select-option>
            <a-select-option value="2"> 2 </a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="CILO2">
          <a-select
            style="width: 360px"
            v-decorator="[
              'cilo2',
              {
                rules: [{ required: true, message: 'Please select cilo2!' }],
              },
            ]"
            placeholder="cilo2"
            @change="handleSelectChange"
          >
            <a-select-option value="1"> 1 </a-select-option>
            <a-select-option value="2"> 2 </a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="CILO3">
          <a-select
            style="width: 360px"
            v-decorator="[
              'cilo3',
              {
                rules: [{ required: true, message: 'Please select cilo3!' }],
              },
            ]"
            placeholder="cilo3"
            @change="handleSelectChange"
          >
            <a-select-option value="1"> 1 </a-select-option>
            <a-select-option value="2"> 2 </a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item layout="inline">
          <a-space :size="large">
            <!-- <a-button type="primary" html-type="submit" :disabled="hasErrors(form.getFieldsError())"> -->
            <a-button type="primary" html-type="submit"> Save </a-button>
            <a-button> Cancel </a-button>
          </a-space>
        </a-form-item>
      </a-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "DefineDependency",
  data() {
    return {
      
    };
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

.definedependency{
    height: 100%;
    width: 100%;
    margin: auto;
    position: relative;
    text-align: center;
}

.definedependencybox{
  height: 100%;
   width: 100%;
}


</style>
