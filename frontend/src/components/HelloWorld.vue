<template>
  <div class="hello">
    <div>
      <a-row type="flex" justify="space-around" align="top" />
      <a-row type="flex" justify="space-around" align="middle">
        <a-col :span="9" />
        <a-col :span="6">
          <div class="login">
            <h2>Log In</h2>
            <a-form :form="form" :label-col="{ span: 24 }" :wrapper-col="{ span: 24 }" @submit="handleSubmit">
              <a-form-item label="Username">
                <a-input
                  v-decorator="['Username', { rules: [{ required: true, message: 'Please input your username!' }] }]"
                />
              </a-form-item>
              <a-form-item label="Password">
                <a-input
                  v-decorator="['Password', { rules: [{ required: true, message: 'Please input your Password!' }] }]"
                />
              </a-form-item>
              <!-- <a-form-item label="Gender">
                <a-select
                  v-decorator="[
                    'gender',
                    { rules: [{ required: true, message: 'Please select your gender!' }] },
                  ]"
                  placeholder="Select a option and change input text above"
                  @change="handleSelectChange"
                >
                  <a-select-option value="male">
                    male
                  </a-select-option>
                  <a-select-option value="female">
                    female
                  </a-select-option>
                </a-select>
              </a-form-item> -->
              <a-form-item :wrapper-col="{ span: 24, offset: 0 }">
                <a-button type="primary" html-type="submit">
                  Log In
                </a-button>
              </a-form-item>
            </a-form>
          </div>
        </a-col>
        <a-col :span="9" />
      </a-row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
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
.login {
  border: dotted 1px;
  border-color: black;
  margin-top: 20%;
  padding: 7%;
}
#login {
  border-color: black;
}
</style>
