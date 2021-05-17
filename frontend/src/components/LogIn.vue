<template>
  <div id="login-framework">
    <a-row type="flex" justify="space-around" style="margin: auto">
      <a-col :span="8">
        <div id="login">
          <h1>Log In</h1>
          <a-form :label-col="{ span: 24 }" :wrapper-col="{ span: 24 }" @submit.native.prevent>
            <a-form-item label="Username">
              <a-input v-model="infos.username">
                <a-icon slot="prefix" type="user" style="color:rgba(0,0,0,.25)"/>
              </a-input>
            </a-form-item>
            <a-form-item label="Password">
              <a-input v-model="infos.password" type="password">
                <a-icon slot="prefix" type="lock" style="color:rgba(0,0,0,.25)"/>
              </a-input>
            </a-form-item>
            <a-form-item label="Identity">
              <a-radio-group name="radioGroup" v-model="infos.role">
                <a-radio value="course-designer">
                  Course Designer
                </a-radio>
                <a-radio value="lecturer">
                  Lecturer
                </a-radio>
                <a-radio value="student">
                  Student
                </a-radio>
              </a-radio-group>
            </a-form-item>
            <a-form-item>
              <a-button type="primary" html-type="submit"
                        :disabled="infos.role === '' || infos.username === '' || infos.password ===''"
                        @click="SendInfo" :data-role="infos.role">
                Log In
              </a-button>
              <br>
            </a-form-item>
          </a-form>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'LogIn',
  data() {
    return {
      infos: {
        username: '',
        password: '',
        role: '',
      }
    };
  },
  methods: {
    SendInfo(e) {
      let data = e.currentTarget.dataset
      let role = data.role;
      console.log(this.infos);
      let url = "http://127.0.0.1:8000/api/" + role + "/login/";
      //异步访问api以获取数据
      axios.post(url, this.infos).then((res) => {
        // console.log(res.data);
        if (res.data.code === 0) { // If success then
          switch (role) {
            case "student":
              this.$router.push('/Student');
              break;
            case "course-designer":
              this.$router.push('/Designer');
              break;
            case "lecturer":
              this.$router.push('/Lecturer');
              break;
          }
          // console.log(res.data);
        } else {// If not then
          console.log(res.data);
        }
      }).catch((e) => {
        // If some error occurs
        console.log(e);
      });
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
  padding: 5%;
  margin: auto;
  text-align: center;
}

#login-framework {
  padding: 5%;
  width: auto;
  margin: auto;
  text-align: center;
}
</style>
