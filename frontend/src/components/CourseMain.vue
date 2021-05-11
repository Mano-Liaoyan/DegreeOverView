<template>
  <div class="coursemain">
    <div>
      <a-row type="flex" justify="space-around" align="top"/>
      <a-row type="flex" justify="space-around" align="middle">
        <a-col :span="6"/>
        <a-col :span="12">
          <div id="coursemain">
            <h2>Course</h2>
            <a-row>
                <a-button>Edit CILOs</a-button>
                <a-button>Import CILOs</a-button>
            </a-row>
            <a-row>
                <a-button>Edit Assessments</a-button>
                <a-button>Import Assessments</a-button>
            </a-row>
            <a-row>
                <a-button>Cancel</a-button>
            </a-row>
          </div>
        </a-col>
        <a-col :span="6"/>
      </a-row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CourseMain',
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
