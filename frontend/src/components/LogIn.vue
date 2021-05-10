<template>
  <div class="login">
    <div>
      <a-row type="flex" justify="space-around" align="top"/>
      <a-row type="flex" justify="space-around" align="middle">
        <a-col :span="7"/>
        <a-col :span="10">
          <div id="login">
            <h1>Log In</h1>
            <a-form :form="form" :label-col="{ span: 24 }" :wrapper-col="{ span: 24 }" @submit="handleSubmit" @submit.native.prevent>
              <a-form-item label="Username">
                <a-input v-model="Username">
                <a-icon slot="prefix" type="user" style="color:rgba(0,0,0,.25)"/></a-input>
              </a-form-item>
              <a-form-item label="Password">
                <!--<a-input
                  v-decorator="['Password', { rules: [{ required: true, message: 'Please input your Password!' }] }]"
                />-->
                <a-input v-model="Password" type="password" >
                    <a-icon slot="prefix" type="lock" style="color:rgba(0,0,0,.25)"/>
                </a-input>
              </a-form-item>
              <a-form-item label="Identity">
                    <a-radio-group name="radioGroup" v-model ="checked" @change="onChange">
                      <a-radio :value="1">
                        Course Designer
                      </a-radio>
                      <a-radio :value="2">
                        Lecturer
                      </a-radio>
                      <a-radio :value="3">
                        Student
                      </a-radio>
                    </a-radio-group>
              </a-form-item>
              <a-form-item >
                <!--<span>value: {{checked}}</span><br>
                <span>name: {{Username}}</span><br>
                <span>psw: {{Password}}</span><br>-->
                <a-button type="primary" html-type="submit" :disabled="checked === '' || Username === '' || Password ===''">
                  <router-link v-if="checked === 1" to="/designer">
                    Log In
                  </router-link>
                  <router-link v-else-if="checked === 2" to="/lecturer">
                    Log In
                  </router-link>
                  <router-link v-else-if="checked === 3" to="/student">
                    Log In
                  </router-link>
                   <router-link v-else to="/">
                    Log In
                  </router-link>
                </a-button> <br>
                
              </a-form-item>
            </a-form>
          </div>
        </a-col>
        <a-col :span="7"/>
      </a-row>
    </div>
  </div>
</template>

<script>
export default {
  el: '#login',
  name: 'LogIn',
  data() {
    return {
        Username : '',
        Password : '',
        checked : '',
    };
  },
  methods: {
    getRadioValue (event) {
      checked = event.target.value;
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

#login {
  border: 1px dotted black;
  margin-top: 30%;
  padding: 7%;
}
</style>
