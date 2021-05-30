<template>

  <div class="viewdependency"> 
    <div class="dependencybox">
      <h1 style="text-align: center; font-weight: bold; font-size: 20px;">Input the Programme to view dependency</h1>
      <br>
      <a-form :form="form" @submit="handleSubmit">
        <a-form-item>
          <a-input
            style="width: 400px"
            v-decorator="[
              'coursename',
              {
                rules: [
                  {
                    required: true,
                    message: 'Please input programme!',
                    trigger: 'blur',
                  },
                ],
              },
            ]"
            placeholder="Please input programme"
          >
          <a-icon slot="prefix" type="bulb" style="color:rgba(0,0,0,.25)"/>
          </a-input>
        </a-form-item>
        <a-form-item>
            <div style="float: left;" >
              <a-button style="float: left;" type="primary" html-type="submit"> 
                <router-link to="dependencyDesigner"> Confirm </router-link>
                </a-button>
            </div>
            <div style="float: right;" >
              <a-button> 
                <router-link to="/designer"> Cancel </router-link>
              </a-button>
            </div>
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
  methods: {
    handleSubmit(){

    },
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

.viewdependency{
  height: 100%;
  width: 100%;
  padding: 5%;
  text-align: center;
}

.dependencybox{
    border: 1px solid lightskyblue;
    padding: 5%;
    margin: auto;
    position: relative;
    height: 300px;
    width: 500px;

}

</style>
