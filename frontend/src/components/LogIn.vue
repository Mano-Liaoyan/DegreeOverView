<template>
  <div class="login">
    <div class="loginbox">
      <a-row type="flex" justify="space-around">
        <a-col :span="24">
          <div id="login">
            <h1 style="text-align: center; font-weight: bold;">DegreeOverview</h1>
            <div style="margin-top: 10%;">
              <a-form :rules="loginRules" class="loginform" label-col="{ span: 24 }" :wrapper-col="{ span: 24 }" @submit.native.prevent>
                <a-form-item style="border-radius: 20px; background-color: transparent;">
                  <a-input v-model="infos.username"
                           placeholder="Please input the username">
                    <a-icon slot="prefix" type="user" style="color:rgba(0,0,0,.25)"/>
                  </a-input>
                </a-form-item>
                <a-form-item>
                  <a-input v-model="infos.password" type="password" placeholder="Please input the password">
                    <a-icon slot="prefix" type="lock" style="color:rgba(0,0,0,.25)"/>
                  </a-input>
                </a-form-item>
                <a-form-item label="I'm a:">
                  <a-radio-group name="radioGroup" v-model="infos.role" style="margin: auto;">
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
                <a-form-item style="width: 100%;">
                  <a-button style="width: 100%; font-weight: bold;" type="primary" html-type="submit"
                            :disabled="infos.role === '' || infos.username === '' || infos.password ===''"
                            @click="SendInfo" :data-role="infos.role">
                    Log In
                  </a-button>
                  <br>
                </a-form-item>
              </a-form>
            </div>
          </div>
        </a-col>
      </a-row>
    </div>
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
      },
      loginRules: {
        username: [{required: true, message: '请输入账号', trigger: 'blur'}],
        password: [{required: true, message: '请输入密码', trigger: 'blur'}],
        role: [{required: true, message: '请输入role', trigger: 'blur'}],
      },
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
        console.log(res.data);
        if (res.data.code === 0) { // If success then
          this.$store.commit("setUserName", this.infos.username)
          switch (role) {
            case "student":
              this.$router.push('/Student/studenthome');
              break;
            case "course-designer":
              this.$router.push('/Designer/designerhome');
              break;
            case "lecturer":
              this.$router.push('/Lecturer/lecturerhome');
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

.login {
  height: 100%;
  width: 100%;
  padding: 5%;
  margin: auto;
  background: url("../../static/images/background1.png") no-repeat center center;
  background-size: 100% 100%;
  overflow: hidden;
}

.loginbox {
  height: 455px;
  width: 28%;
  margin: auto;
  position: relative;
  top: 20%;

}

.login-form {
  -webkit-border-radius: 5px;
  border-radius: 5px;
  -moz-border-radius: 5px;
  background-clip: padding-box;
  margin: 10px auto;
  width: 350px;
  padding: 35px 35px 15px 35px;
}

</style>
