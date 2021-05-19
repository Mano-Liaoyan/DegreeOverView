<template>
  <div class="add-mem">
    <div class="form-css">
      <div class="form_area" v-for="(item, index) in majorArr" :key="index">
        <!--        <span class="from-index" v-if="majorArr.length>1">{{ index + 1 }}</span>-->
        <a-select show-search :value="item.majorName" placeholder="Evaluation Method"
                  class="sp-width" :default-active-first-option="false" :show-arrow="false"
                  :filter-option="false" :not-found-content="null" label-in-value
                  @search="handleSearch" @focus="handleFocus(index)" @blur="onBlurSelect"
                  @change="handleChange">
          <a-select-option v-for="obj in item.majorNameArr" :key="obj.specialtyCode">
            {{ obj.specialtyName }}
          </a-select-option>
        </a-select>
        <a-input class="m-width" placeholder="CILO" v-model="item.majorCode"/>
        <a-input class="m-width" placeholder="Percent" v-model="item.studentNumber"/>
        <template v-if="!isDisabled">
          <a-icon v-if="index === 0" class="create_fq_icon m-left" @click="addField" type="plus-circle"/>
          <a-icon v-else class="create_fq_icon m-left" @click="deleteField(index)" type="minus-circle"/>
        </template>
      </div>
    </div>
  </div>
</template>

<script>

let timeout;
let currentValue;

function fetch(value, callback) {
  if (timeout) {
    clearTimeout(timeout);
    timeout = null;
  }
  currentValue = value;


}

export default {
  name: 'MajorAddPage',
  data() {
    return {
      isDisabled: false,
      labelCol: {span: 4},
      wrapperCol: {span: 14},
      majorArr: [{majorName: undefined, majorCode: null, education: '', studentNumber: '', majorNameArr: []}],
      majorNameArr: [],
      majorCodeArr: [],
      value: undefined,
      majorCode: undefined,
      selIndex: '',
      form: {
        address: '',
        comment: '',
        departmentName: '',
        education: '',
        grade: '',
        linkMan: '',
        linkPhone: '',
        majorCode: '',
        majorName: undefined,
        schoolCode: '',
        status: false,
        studentNumber: '',
      },
      xueLiOptions: [],
      rules: {
        departmentName: [{required: true, message: '请输入院系名称', trigger: 'blur'},
          {max: 30, message: '最多输入30个字符', trigger: 'blur'},
        ],
        grade: [{required: true, message: '请输入届别', trigger: 'blur'}],
        roles: [{required: true, message: '请输入所属角色', trigger: 'change'}],
      },
    };
  },
  methods: {
    doCancel() {
      this.$router.go(-1);
    },
    addField() {
      if (this.majorArr.length < 20) {
        this.majorArr.push({majorName: undefined, majorCode: null, education: '', studentNumber: '', majorNameArr: []})
      } else {
        this.$message.info('最多添加20个专业！')
      }
    },
    deleteField(index) {
      this.majorArr.splice(index, 1)
    },
    handleSearch(value) {
      if (value) {
        this.majorArr[this.selIndex].inputName = value
        // fetch(value, data => (this.majorNameArr = data));
        // fetch(value, data => (this.majorArr[this.selIndex].majorNameArr = data));
      }
    },
    handleChange(value) {
      // this.value = value;
      // this.form.majorName = value;
      this.majorArr[this.selIndex].majorName = value
      this.majorArr[this.selIndex].majorCode = value.key
      // fetch(value, data => (this.majorNameArr = data));
    },
    onBlurSelect(value) {
      if (this.majorArr[this.selIndex].majorNameArr.length > 0) {
      } else {
        if (this.majorArr[this.selIndex].inputName.length > 0) {
          this.majorArr[this.selIndex].majorName = {key: "", label: this.majorArr[this.selIndex].inputName}
        }
      }
    },
    handleFocus(val) {//传的索引值
      this.selIndex = val
    },
  },

}
</script>

<style scoped lang="less">
.add-mem {
  background-color: #FFFFFF;

  .form-css {

    .form_width {
      width: 468px;

      &.field {
        width: 217px;
      }
    }

    .sp-width {
      width: 160px;
    }

    .m-width {
      width: 88px;
    }

    .form_area {
      //width: 668px;
      /*border: 1px solid red;*/
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;

      .m-left {
        margin-left: 16px;
      }
    }

    .create_fq_icon {
      font-size: 18px;
      vertical-align: middle;
      color: #437FFF;
    }

    .from-index {
      display: inline-block;
      margin-right: 10px;
    }
  }
}

</style>
