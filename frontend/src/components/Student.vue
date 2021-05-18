<template>
  <div class="student">
    <div>
      <a-row type="flex" justify="space-around" align="top" />
      <a-row type="flex" justify="space-around" align="middle">
        <a-col :span="6" />
        <a-col :span="12">
          <div id="student">
            <h2>student</h2>
            <div>
              <a-form layout="inline" :form="form" @submit="handleSubmit">
                <a-form-item>
                  <a-input
                    v-decorator="[
                      'keyword',
                      {
                        rules: [
                          {
                            required: true,
                            message: 'Please input search keywords!',
                          },
                        ],
                      },
                    ]"
                    placeholder="Search Keywords"
                  >
                    <a-icon
                      slot="prefix"
                      type="search"
                      style="color: rgba(0, 0, 0, 0.25)"
                    />
                  </a-input>
                </a-form-item>
                <a-form-item>
                  <a-select
                    default-value="Choose Search Function..."
                    style="width: 30px"
                    @change="handleChange"
                  >
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
            </div>
            <div>
              <a-tabs default-active-key="0" :tab-position="left">
                <a-tab-pane key="0" tab="Home">
                  <div>Hello World!</div>
                </a-tab-pane>
                <a-tab-pane key="1" tab="Create a new course">
                  <div>
                    <a-form layout="inline" :form="form" @submit="handleSubmit">
                      <a-form-item>
                        <a-input
                          v-decorator="[
                            'coursename',
                            {
                              rules: [
                                {
                                  required: true,
                                  message: 'Please input course name!',
                                },
                              ],
                            },
                          ]"
                          placeholder="input course name here"
                        >
                        </a-input>
                      </a-form-item>
                      <a-form-item>
                        <!-- <a-button type="primary" html-type="submit" :disabled="hasErrors(form.getFieldsError())"> -->
                        <a-button type="primary" html-type="submit">
                          Confirm
                        </a-button>
                      </a-form-item>
                    </a-form>
                    <a-button>Cancel</a-button>
                  </div>
                </a-tab-pane>
                <a-tab-pane key="2" tab="Modify a course">
                  <div>
                    <a-form :form="form">
                      <a-form-item
                        :label-col="formItemLayout.labelCol"
                        :wrapper-col="formItemLayout.wrapperCol"
                        label="CourseName"
                      >
                        <a-input
                          v-decorator="[
                            'coursename',
                            {
                              rules: [
                                {
                                  required: true,
                                  message: 'Please input course name',
                                },
                              ],
                            },
                          ]"
                          placeholder="Please input your name"
                        />
                      </a-form-item>
                      <a-form-item
                        :label-col="formItemLayout.labelCol"
                        :wrapper-col="formItemLayout.wrapperCol"
                        label="CILOs"
                      >
                        <a-input
                          v-decorator="[
                            'cilos',
                            {
                              rules: [
                                {
                                  required: true,
                                  message: 'Please input cilos',
                                },
                              ],
                            },
                          ]"
                          placeholder="Please input your name"
                        />
                        <a-button> Add CILOs </a-button>
                      </a-form-item>
                      <a-form-item
                        :label-col="formItemLayout.labelCol"
                        :wrapper-col="formItemLayout.wrapperCol"
                        label="Assessments"
                      >
                        <a-input
                          v-decorator="[
                            'assessments',
                            {
                              rules: [
                                {
                                  required: true,
                                  message: 'Please input assessments',
                                },
                              ],
                            },
                          ]"
                          placeholder="Please input your name"
                        />
                        <a-button> Add Assessments </a-button>
                      </a-form-item>
                      <a-form-item
                        :label-col="formItemLayout.labelCol"
                        :wrapper-col="formItemLayout.wrapperCol"
                        label="Relationships"
                      >
                        <a-input
                          v-decorator="[
                            'relationships',
                            {
                              rules: [
                                {
                                  required: true,
                                  message: 'Please input relationships',
                                },
                              ],
                            },
                          ]"
                          placeholder="Please input your name"
                        />
                      </a-form-item>
                      <a-form-item
                        :label-col="formItemLayout.labelCol"
                        :wrapper-col="formItemLayout.wrapperCol"
                        label="Prerequisites"
                      >
                        <a-input
                          v-decorator="[
                            'prerequisites',
                            {
                              rules: [
                                {
                                  required: true,
                                  message: 'Please input prerequisites',
                                },
                              ],
                            },
                          ]"
                          placeholder="Please input your name"
                        />
                      </a-form-item>
                      <a-form-item
                        :label-col="formItemLayout.labelCol"
                        :wrapper-col="formItemLayout.wrapperCol"
                        label="Programme"
                      >
                        <a-input
                          v-decorator="[
                            'programme',
                            {
                              rules: [
                                {
                                  required: true,
                                  message: 'Please input programme',
                                },
                              ],
                            },
                          ]"
                          placeholder="Please input your name"
                        />
                      </a-form-item>
                      <a-form-item
                        :label-col="formItemLayout.labelCol"
                        :wrapper-col="formItemLayout.wrapperCol"
                        label="Type"
                      >
                        <a-input
                          v-decorator="[
                            'type',
                            {
                              rules: [
                                {
                                  required: true,
                                  message: 'Please input type',
                                },
                              ],
                            },
                          ]"
                          placeholder="Please input your name"
                        />
                      </a-form-item>
                      <a-form-item
                        :label-col="formItemLayout.labelCol"
                        :wrapper-col="formItemLayout.wrapperCol"
                        label="StartAcademicYear"
                      >
                        <a-input
                          v-decorator="[
                            'startacademicyear',
                            {
                              rules: [
                                {
                                  required: true,
                                  message: 'Please input start academic year',
                                },
                              ],
                            },
                          ]"
                          placeholder="Please input your name"
                        />
                      </a-form-item>
                      <a-form-item
                        :label-col="formTailLayout.labelCol"
                        :wrapper-col="formTailLayout.wrapperCol"
                      >
                        <a-button> Save </a-button>
                        <a-button> Back </a-button>
                      </a-form-item>
                    </a-form>
                  </div>
                </a-tab-pane>
                <a-tab-pane key="3" tab="Define dependencies">
                  <div></div>
                </a-tab-pane>
                <a-tab-pane key="4" tab="View dependencies">
                  <div></div>
                </a-tab-pane>
                <a-tab-pane key="5" tab="Define relationships">
                  <div></div>
                </a-tab-pane>
              </a-tabs>
            </div>

            <a-button>View Dependencies</a-button>
            <a-button>View Analysis Result</a-button>
          </div>
        </a-col>
        <a-col :span="6" />
      </a-row>
    </div>
  </div>
</template>

<script>
export default {
  name: "Student",
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
</style>
