<template>
  <div id="designer">
      <div class="top">
        <a-row type="flex" justify="space-between">
          <a-col :span="12">
            <h2>Designer homepage</h2>
          </a-col>
          <a-col :span="12" justify="end"> 
            <p>welcome xxx!</p>
            <p>Log out</p>
          </a-col>
        </a-row>
      </div>
      <div class="middle">
        <a-row type="flex" justify="flex-start">
              <a-form :label-col="{ span: 24 }" :wrapper-col="{ span: 24 }" @submit.native.prevent>
                <a-form-item>
                  <a-input
                    v-model="infos.keyword" placeholder="Search Keywords">
                   <a-icon slot="prefix" type="search" style="color:rgba(0,0,0,.25)" />
                 </a-input>
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
            </a-row>
            
            <a-button>View Dependencies</a-button>
            <a-button>View Analysis Result</a-button>
          
        </div>

          </div>
    
</template>

<script>
export default {
  name: 'Designer',
  data() {
    return {
      infos: {
        keyword: '',
      }
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
#designer {
  display: flex;
  height: 600px;
  width: 1000px;
  padding: 0 20px;
  background-color: #cccccc;
  justify-content: "center";
  flex-wrap: wrap;
}
.top {
  display: flex;
  height: 100px;
  width: 1000px;
}

</style>
