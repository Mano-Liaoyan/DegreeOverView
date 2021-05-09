<template>
  <div class="herVerCenter">
    <a-form-model layout="vertical" :model="formInline" @submit="handleSubmit" @submit.native.prevent>
      <a-form-model-item>
        <a-input v-model="formInline.user" placeholder="Username">
          <a-icon slot="prefix" type="user" style="color:rgba(0,0,0,.25)"/>
        </a-input>
      </a-form-model-item>
      <a-form-model-item>
        <a-input v-model="formInline.password" type="password" placeholder="Password">
          <a-icon slot="prefix" type="lock" style="color:rgba(0,0,0,.25)"/>
        </a-input>
      </a-form-model-item>
      <a-form-model-item>
        <a-button type="primary" html-type="submit" :disabled="formInline.user === '' || formInline.password === ''" @click="goToHomePage">
          Log in
        </a-button>
      </a-form-model-item>
    </a-form-model>
    {{ return_info }}
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      formInline: {
        user: '',
        password: '',
      },
      return_info: null
    };
  },
  methods: {
    handleSubmit(e) {
      console.log(this.formInline);
      console.log(e);
      //异步访问api以获取数据
      axios.get('http://127.0.0.1:8000/api/student/2/').then((res) => {
        console.log(res.data);
        this.return_info = res.data;
      }).catch((e) => {
        console.log(e);
      });
    },
    goToHomePage() {
      this.$router.push('/');
    }
  },
}
</script>

<style scoped>

</style>