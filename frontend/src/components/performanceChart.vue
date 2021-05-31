<template>
  <div id="chart" style="width: 600px;height:400px;">
      
  </div>
</template>

<script>
  import * as echarts from 'echarts'
  export default {
    data() {
      return {}
    },
    mounted() {
      let this_ = this;
      let myChart = echarts.init(document.getElementById('chart'));
      let option = {
        color: [ '#FF917C'],
    title: {
        text: this.$route.params.coursename,
    },
    legend: {
        data: ['CILOs']
    },
    radar: 
        {
            indicator: [
            { name: 'CILO 1', max: 100},
            { name: 'CILO2', max: 100},
            { name: 'CILO3', max: 100},
           
            ],
        },
    series: [{
        name: '',
        type: 'radar',
        data: [
            {
                value: [98.5, 99.6, 97.0],
                name: 'CILOs',
                 label: {
                        show: true,
                        formatter: function (params) {
                            return params.value;
                        }
                    },
            },
          
        ]
    }]
      };
      myChart.setOption(option);
 
      //建议加上以下这一行代码，不加的效果图如下（当浏览器窗口缩小的时候）。超过了div的界限（红色边框）
      window.addEventListener('resize',function() {myChart.resize()});
    },
    methods: {},
    watch: {},
    created() {
 
    }
  }
</script>

<style>
#chart {
    height: 100%;
    width: 100%;
    margin: auto;

}
</style>
