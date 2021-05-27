<template>
    <div style="height: 100%; width: 100%; text-align: center;">
        <h1> Analysis Result </h1>
        <div id="analysis" style="width: 600px;height:400px; padding-top: 2%;">

        </div>
        <div style="padding-left: 50%; padding-top: 2%;">
            <a-button type="primary" >
                <router-link to="/lecturer/analysislist">
                    Back
                </router-link>
            </a-button>
        </div>
    </div>
</template>

<script>
    import * as echarts from 'echarts';
    
    export default {
    data() {
      return {}
    },
    mounted() {
        let this_ = this;
        let myChart = echarts.init(document.getElementById('analysis'));
        let option = {
        
            title: {
                text: 'line chart'
            },
            toolbox: { // 工具箱
                show: true,
                feature: {
                    dataView: {readOnly: true,
                                },
                    magicType: {type: ['bar', 'line']},
                }
            },

            tooltip: {
                trigger: 'axis',
                axisPointer: { // 坐标轴指示器，坐标轴触发有效
                    type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
                },
                formatter: '{b0}<br/>{a0}: {c0}%<br />{a1}: {c1}%<br />{a2}: {c2}%<br />{a3}: {c3}%'//展示百分比  五条折线
            },
            legend: {
                data: ['CILO1', 'CILO2', 'CILO3', 'CILO4']
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: {
                type: 'category',
                
                data: ['2021', '2020', '2019', '2018']
            },
            yAxis: {
                type: 'value',
                axisLabel: {
                    show: true,
                    interval: 'auto',
                    formatter: '{value} %'//纵坐标百分比
                }
            },
            series: [
                {
                    name: 'CILO1',
                    type: 'bar',
                    barGap: 0,
                    emphasis: {
                        focus: 'series'
                    },
                    data: [20, 40, 25, 10]
                },
                {
                   name: 'CILO2',
                    type: 'bar',
                    barGap: 0,
                    emphasis: {
                        focus: 'series'
                    },
                    data: [30, 20, 35, 20]
                },
                {
                     name: 'CILO3',
                    type: 'bar',
                    barGap: 0,
                    emphasis: {
                        focus: 'series'
                    },
                    
                    data: [10, 10, 15, 30]
                },
                {
                    name: 'CILO4',
                    type: 'bar',
                    barGap: 0,
                    emphasis: {
                        focus: 'series'
                    },
                    
                    data: [15, 30, 25, 40]
                },
            ]
         };
          myChart.setOption(option);
          window.addEventListener('resize',function() {myChart.resize()});
        },
        methods: {},
        watch: {},
        created() {
    
        }
    }
</script>
<style>
#barchart {
    height: 100%;
    width: 100%;
    margin: auto;

}
</style>
