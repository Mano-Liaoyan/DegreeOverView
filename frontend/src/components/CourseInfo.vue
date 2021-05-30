<template>
<vue-scroll style="height: 100%">
  <a-descriptions title="Course Info" bordered>
    <a-descriptions-item label="Course Name">
      Discrete Math
    </a-descriptions-item>
    <a-descriptions-item label="Course Code">
      123456
    </a-descriptions-item>
    <a-descriptions-item label="Programme">
      CST/DS
    </a-descriptions-item>
    <a-descriptions-item label="Academic Start Year" :span="3">
      2020/Summer semester
    </a-descriptions-item>
    <a-descriptions-item label="Pre-requisite" :span="3">
      Calculus I, Statistic
    </a-descriptions-item>
    
    <a-descriptions-item label="Assessment Methods:" :span="3">
      <a-table :columns="columns" :data-source="data" :pagination="false">
        <a slot="name" slot-scope="text">{{ text }}</a>
        <span slot="method">Name</span>
        <span slot="CILOs" slot-scope="tags">
          <a-tag
            v-for="tag in tags"
            :key="tag"
            :color="
              tag === 'loser'
                ? 'volcano'
                : tag.length > 5
                ? 'geekblue'
                : 'green'
            "
          >
            {{ tag.toUpperCase() }}
          </a-tag>
        </span>
         <span slot="percentage">
             Percentage
        </span>
      </a-table>
      <br />
    </a-descriptions-item>
    <a-descriptions-item label="CILOs:">
      <a-table :columns="cilocolumns" :data-source="cilodata" :pagination="false">
        <a slot="name" slot-scope="text">{{ text }}</a>
        <span slot="CILO">Name</span>
         <span slot="Details">
             Percentage
        </span>
      </a-table>
      <br />
    </a-descriptions-item>
  </a-descriptions>
</vue-scroll>
  
</template>

<script>
const columns = [
  {
    title: "Evaluation Method",
    dataIndex: "name",
    key: "name",
  },
  {
    title: "CILOs",
    key: "tags",
    dataIndex: "tags",
    scopedSlots: { customRender: "tags" },
  },
  {
    title: "Percentage",
    key: "percentage",
    dataIndex: "percentage",
  },
];

const data = [
  {
    key: "1",
    name: "Assignments/Quizes",
    tags: ["CILO1"],
    percentage: "15%"
  },
  {
    key: "2",
    name: "Labs",
    tags: ["CILO2"],
    percentage: "25%"
  },
  {
    key: "3",
    name: "Projects",
    tags: ["CILO1", "CILO2"],
    percentage: "10%"
  },
  {
    key: "4",
    name: "Examination",
    tags: ["CILO1", "CILO2"],
    percentage: "50%"
  },
];

const cilocolumns = [
 {
    title: "CILO ID",
    dataIndex: "id",
    key: "id",
  },
  {
    title: "Detais",
    key: "detail",
    dataIndex: "detail",
  },
];

const cilodata = [
 {
    key: "1",
    id: "1",
    detail: "xxxxxx",
  },
  {
    key: "2",
    id: "2",
    detail: "xxxxxx",
  },
];

export default {
  name: "CourseInfo",
  data() {
    return {
      data,
      columns,
      cilodata,
      cilocolumns,
    };
  },
  methods:{
    handleMenuClick(e) {
      console.log("click", e);
    },
  },
};

</script>
