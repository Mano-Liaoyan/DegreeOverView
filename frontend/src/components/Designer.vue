<template>
  <div class="designer">
    <div>
      <a-row type="flex" justify="space-around" align="top"/>
      <a-row type="flex" justify="space-around" align="middle">
        <a-col :span="6"/>
        <a-col :span="12">
          <div id="designer">
              <h2>designer</h2>
            <a-form layout="inline" :form="form" @submit="handleSubmit">
              <a-form-item>
                <a-input
                  v-decorator="[
                    'keyword',
                    { rules: [{ required: true, message: 'Please input search keywords!' }] },
                  ]"
                  placeholder="Search Keywords"
                >
                  <a-icon slot="prefix" type="search" style="color:rgba(0,0,0,.25)" />
                </a-input>
              </a-form-item>
              <a-form-item>
                <a-select default-value="Choose Search Function..." style="width: 30px" @change="handleChange">
                  <a-select-option value="course">
                    Search by Course
                  </a-select-option>
                  <a-select-option value="cilo">
                    Search by CILOs
                  </a-select-option>
                  <a-select-option value="keyword">
                    Search by Keywords
                  </a-select-option>
                </a-select>
              </a-form-item>
              <a-form-item>
                <!-- <a-button type="primary" html-type="submit" :disabled="hasErrors(form.getFieldsError())"> -->
                <a-button type="primary" html-type="submit">
                  Search
                </a-button>
              </a-form-item>
            </a-form>
            <a-button>View Dependencies</a-button>
            <a-button>View Analysis Result</a-button>
          </div>
        </a-col>
        <a-col :span="6"/>
      </a-row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Designer',
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
