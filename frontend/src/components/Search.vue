<template>
  <div class="global-search-wrapper">
    <a-auto-complete class="global-search" :size="size" style="width: 100%"
                     placeholder="input here" option-label-prop="title" @select="onSelect" @search="handleSearch">
      <template slot="dataSource">
        <a-select-option v-if="item.count!==0" v-for="item in dataSource" :key="item.category" :title="item.category">
          Found <span style="color: red">{{ item.query }}</span> on {{ item.category }}
          <span className="global-search-item-count">{{ item.count }} results</span>
        </a-select-option>
      </template>
      <a-input>
        <a-icon slot="suffix" type="search" class="certain-category-icon"/>
      </a-input>
    </a-auto-complete>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Search",
  props: {
    size: {
      type: String,
      default: "default",
    },
  },
  data() {
    return {
      dataSource: [],
      ciloData: undefined,
      courseData: undefined
    };
  },
  methods: {
    onSelect(value) {
      console.log("onSelect", value);
      if (value === "Course") {
        console.log(this.courseData);

      } else {
        console.log(this.ciloData);
      }
      this.$router.push({name: 'SearchResult'})
    },

    async handleSearch(value) {
      console.log("hs: ", value)
      this.dataSource = value ? await this.searchResult(value) : [];
      console.log('dataSource: ', this.dataSource)
    },

    getRandomInt(max, min = 0) {
      return Math.floor(Math.random() * (max - min + 1)) + min;
    },

    async getCilo(query) {
      let url = "http://127.0.0.1:8000/cilo?search=" + query;
      let data;
      //异步访问cilo search api以获取数据
      await axios.get(url).then((res) => {
        // console.log(res.data);
        if (res.data.count !== 0) { // If success then
          // console.log(res.data);
          data = res.data;
        } else {// If not then
          // console.log(res.data);
          data = res.data;
        }
      }).catch((e) => {
        // If some error occurs
        console.log(e);
      });
      return data;
    },

    async getCourse(query) {
      let url = "http://127.0.0.1:8000/course?search=" + query;
      let data;
      //异步访问course search api以获取数据
      await axios.get(url).then((res) => {
        console.log(res.data);
        if (res.data.count !== 0) { // If success then
          data = res.data;
        } else {// If not then
          // console.log(res.data);
          data = res.data;
        }
      }).catch((e) => {
        // If some error occurs
        console.log(e);
      });
      return data;
    },

    async searchResult(query) {
      let cilo_res, course_res;
      cilo_res = await this.getCilo(query);
      course_res = await this.getCourse(query);
      this.ciloData = cilo_res;
      this.courseData = course_res;
      let a;
      if (cilo_res.count > course_res.count) {
        a = [{'query': query, 'category': 'Cilo', 'count': cilo_res.count},
          {'query': query, 'category': 'Course', 'count': course_res.count},]
      } else {
        a = [{'query': query, 'category': 'Course', 'count': course_res.count},
          {'query': query, 'category': 'Cilo', 'count': cilo_res.count}]
      }
      return a;
    },
  },
};
</script>

<style>
.global-search-wrapper {
  /*padding-right: 50px;*/
  margin: auto;
}

.global-search {
  /*width: 100%;*/
  /*width: 50%;*/
}

.global-search.ant-select-auto-complete .ant-select-selection--single {
  /*margin-right: -46px;*/
}

.global-search.ant-select-auto-complete,
.ant-input-affix-wrapper,
.ant-input:not(:last-child) {
  /*padding-right: 62px;*/
}

.global-search.ant-select-auto-complete,
.ant-input-affix-wrapper,
.ant-input-suffix,
button {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.global-search-item {
  display: flex;
}

.global-search-item-desc {
  flex: auto;
  text-overflow: ellipsis;
  overflow: hidden;
}

.global-search-item-count {
  flex: none;
}
</style>
