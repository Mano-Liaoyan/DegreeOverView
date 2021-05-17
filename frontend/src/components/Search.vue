<template>
  <div class="global-search-wrapper" style="width: 450px">
    <a-auto-complete
      class="global-search"
      :size="size"
      style="width: 100%"
      placeholder="input here"
      option-label-prop="title"
      @select="onSelect"
      @search="handleSearch"
    >
      <template slot="dataSource">
        <a-select-option
          v-for="item in dataSource"
          :key="item.category"
          :title="item.category"
        >
          Found {{ item.query }} on {{ item.category }}
          <span className="global-search-item-count"
            >{{ item.count }} results</span
          >
        </a-select-option>
      </template>
      <a-input>
        <a-button
          slot="suffix"
          style="margin-right: -12px"
          class="search-btn"
          :size="size"
          type="primary"
        >
          <a-icon type="search" />
        </a-button>
      </a-input>
      <a-input>
        <template>
          <a-radio-group name="radioGroup" :default-value="1">
            <a-radio :value="1"> A </a-radio>
            <a-radio :value="2"> B </a-radio>
            <a-radio :value="3"> C </a-radio>
            <a-radio :value="4"> D </a-radio>
          </a-radio-group>
        </template>
      </a-input>
    </a-auto-complete>
  </div>
</template>
<script>
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
    };
  },
  methods: {
    onSelect(value) {
      console.log("onSelect", value);
    },

    handleSearch(value) {
      this.dataSource = value ? this.searchResult(value) : [];
    },

    getRandomInt(max, min = 0) {
      return Math.floor(Math.random() * (max - min + 1)) + min;
    },

    searchResult(query) {
      return new Array(this.getRandomInt(5))
        .join(".")
        .split(".")
        .map((item, idx) => ({
          query,
          category: `${query}${idx}`,
          count: this.getRandomInt(200, 100),
        }));
    },
  },
};
</script>

<style>
.global-search-wrapper {
  padding-right: 50px;
}

.global-search {
  width: 100%;
}

.global-search.ant-select-auto-complete .ant-select-selection--single {
  margin-right: -46px;
}

.global-search.ant-select-auto-complete
  .ant-input-affix-wrapper
  .ant-input:not(:last-child) {
  padding-right: 62px;
}

.global-search.ant-select-auto-complete
  .ant-input-affix-wrapper
  .ant-input-suffix
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
