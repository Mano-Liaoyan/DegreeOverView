<template>
<div>
  <div id="chart" style="width: 600px; height: 400px">

  </div>
  </div>
</template>

<script>
import * as echarts from "echarts";
export default {
  data() {
    return {
     
    };
  },
  mounted() {
    let this_ = this;
    let chartDom = document.getElementById("chart");
    let myChart = echarts.init(chartDom);
    let option = {
      title: {
        text: this.$route.params.programme,
      },
      tooltip: {},
      animationDurationUpdate: 1500,
      animationEasingUpdate: "quinticInOut",
      series: [
        {
          type: "graph",
          layout: "none",
          symbolSize: 50,
          roam: true,
          label: {
            show: true,
          },
          edgeSymbol: ["circle", "arrow"],
          edgeSymbolSize: [4, 10],
          edgeLabel: {
            fontSize: 20,
          },
          data: [
            {
              name: "Data Structure",
              x: 300,
              y: 300,
            },
            {
              name: "Data Algorithms",
              x: 800,
              y: 300,
            },
            {
              name: "Structured Programming",
              x: 550,
              y: 100,
            },
            {
              name: "CILO4",
              x: 550,
              y: 500,
            },
          ],
          links: [
            {
              source: 0,
              target: 1,
              symbolSize: [5, 20],
              label: {
                show: true,
              },
              lineStyle: {
                width: 5,
                curveness: 0.2,
              },
            },
            
            {
              source: "Structured Programming",
              target: "Data Structure",
            },
            {
              source: "Data Structure",
              target: "Data Algorithms",
            },
            // {
            //   source: "CILO2",
            //   target: "CILO4",
            // },
            // {
            //   source: "CILO1",
            //   target: "CILO4",
            // },
          ],
          lineStyle: {
            opacity: 0.9,
            width: 2,
            curveness: 0,
          },
        },
      ],
    };

    option && myChart.setOption(option);
  },
  methods: {},
  watch: {},
  created() {},
};
</script>

<style>
#chart {
  height: 100%;
  width: 100%;
  margin: auto;
}
</style>
