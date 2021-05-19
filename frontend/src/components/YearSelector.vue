<template>
  <a-cascader :options="options" change-on-select @change="onChange" :default-value="[thisYear, '03']">
    <a-icon slot="suffixIcon" type="calendar"/>
  </a-cascader>
</template>
<script>
export default {
  name: "YearSelector",
  data() {
    return {
      options: [],
      thisYear: undefined
    };
  },
  created() {
    let d = new Date();
    this.thisYear = d.getFullYear();
  },
  mounted() {
    this.createTimeOptions();
  },
  methods: {
    onChange(value) {
      console.log(value);
    },
    createTimeOptions() {
      let times = [{
        value: '03',
        label: 'Summer Semester',
      }, {
        value: '09',
        label: 'Winter Semester',
      },]

      for (let i = 1980; i < 2100; i++) {
        this.options.push({
          value: i,
          label: i,
          children: times
        })
      }
    }
  },
};
</script>
