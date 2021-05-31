<template>

  <div class="inputcourse"> 
    <div class="inputcoursebox">
      <h1 style="text-align: center; font-weight: bold; font-size: 20px;">Please input the course name</h1>
      <br>
      <a-form :form="form" model="name" ref="name">
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
            v-model="name.input"
          >
          <a-icon slot="prefix" type="bulb" style="color:rgba(0,0,0,.25)"/>
          </a-input>
        </a-form-item>
        <a-form-item>
            <div style="float: left;" >
              <router-link :to="{name:'PerformanceChart',params: {coursename: name.input}}">
              <a-button style="float: left;" type="primary"> 
                 Confirm
                </a-button>
              </router-link>
            </div>
            <div style="float: right;" >
              <a-button> 
                <router-link to="/student/studenthome"> Cancel </router-link>
              </a-button>
            </div>
            
        </a-form-item>
      </a-form>
      </div>
  </div>
</template>

<script>
export default {
  name: "inputCourse",
  data() {
    return {
      name:{
        input: ''
      }
    };
  },
  methods: {
    sendParams(name){
        this.$router.push({
            path: 'coursemain', 
            query: {
                cname: this.name, 
            }
        })
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

.inputcourse{
  height: 100%;
  width: 100%;
  padding: 5%;
  text-align: center;
}

.inputcoursebox{
    border: 1px solid lightskyblue;
    padding: 5%;
    margin: auto;
    position: relative;
    height: 300px;
    width: 460px;

}

</style>
