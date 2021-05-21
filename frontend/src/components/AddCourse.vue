<template>
  <div class="addcourse">
    <div class="addcoursebox">
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
                    trigger: 'blur',
                  },
                ],
              },
            ]"
            placeholder="Please input course name"
          >
          </a-input>
        </a-form-item>
        <a-form-item>
          <a-space :size="large">
            <div style="float: left;" >
              <a-button style="float: left;" type="primary" html-type="submit"> 
                <router-link to="coursemain"> Confirm </router-link>
                </a-button>
            </div>
            <div style="float: right;" >
              <a-button> 
                <router-link to="/designer"> Cancel </router-link>
              </a-button>
            </div>
          </a-space>
        </a-form-item>
      </a-form>
  </div>
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

.addcourse{
  height: 100%;
  width: 100%;
  margin: auto;
}

.addcoursebox{
   height: 455px;
    width: 28%;
    margin: auto;
    position: relative;
    top: 20%;
    text-align: center;
}
</style>
