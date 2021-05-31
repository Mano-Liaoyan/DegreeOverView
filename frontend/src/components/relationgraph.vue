<template>
  <div>
    <div ref="myPage" style="height:calc(100vh - 50px);">
      <SeeksRelationGraph
        ref="seeksRelationGraph"
        :options="graphOptions"
        :on-node-click="onNodeClick"
        :on-line-click="onLineClick">
        <div slot="node" slot-scope="{node}" @mouseover="showNodeTips(node, $event)" @mouseout="hideNodeTips(node, $event)">
          <div style="height:64px;line-height: 60px;border-radius: 32px">
            <p style="font-size: 14px; text-align: center;">
              {{ node.text }}
            </p>
          </div>
          <div style="color: forestgreen;font-size: 16px;position: absolute;width: 160px;height:25px;line-height: 25px;margin-top:5px;margin-left:-48px;text-align: center;background-color: rgba(66,187,66,0.2);">
            {{ node.data.course }}
          </div>
        </div>
      </SeeksRelationGraph>
    </div>
    <div v-if="isShowNodeTipsPanel" :style="{left: nodeMenuPanelPosition.x + 'px', top: nodeMenuPanelPosition.y + 'px' }" style="z-index: 999;padding:10px;background-color: #ffffff;border:#eeeeee solid 1px;box-shadow: 0px 0px 8px #cccccc;position: absolute;">
      <div style="line-height: 25px;padding-left: 10px;color: #888888;font-size: 12px;">{{currentNode.text}}</div>
      <div class="c-node-menu-item">content:{{currentNode.data.content}}</div>
    </div>
    
  </div>
</template>

<script>
import SeeksRelationGraph from 'relation-graph'
export default {
  name: 'Demo',
  components: { SeeksRelationGraph },
  data() {
    return {
      isShowCodePanel: false,
      isShowNodeTipsPanel: false,
      nodeMenuPanelPosition: { x: 0, y: 0 },
      currentNode: {},
      graphOptions: {
        allowSwitchLineShape: true,
        allowSwitchJunctionPoint: true,
        defaultJunctionPoint: 'border'
        // 这里可以参考"Graph 图谱"中的参数进行设置
      }
    }
  },
  mounted() {
    this.showSeeksGraph()
  },
  methods: {
    showSeeksGraph(query) {
      var __graph_json_data = {
        rootId: '2',
        nodes: [
          // 注意：在节点配置信息中，你的自定义属性需要像下面这样放到data标签中，否则数据会丢失
          { id: '1', text: 'CILO-1', data: { course: 'Database Management System', content: 'dfcjsldvsdnv'} },
          { id: '2', text: 'CILO-2', data: { course: 'Structured Programming', content: 'dfcesfcesfesfv'} },
          { id: '3', text: 'CILO-1', data: { course: 'Object-Oriented Programming', content: 'fcrvgdr'} },
          { id: '4', text: 'CILO-1', data: { course: 'Data Structures', content: 'efcefcadcaccdc'} },
          { id: '5', text: 'CILO-2', data: { course: 'Data Algorithms', content: 'asdwcfege'} },
          { id: '6', text: 'CILO-2', data: { course: 'Operation System', content: 'asdwcfege'} },
          { id: '7', text: 'CILO-1', data: { course: 'Computer Organization', content: 'asdwcfege'} },
          { id: '8', text: 'CILO-1', data: { course: 'IT', content: 'asdwcfege'} },
          
        ],
        links: [
          { from: '4', to: '2', text: 'dependence on' },
          { from: '5', to: '4', text: 'dependence on' },
          { from: '4', to: '3', text: 'dependence on' },
          { from: '6', to: '2', text: 'dependence on' },
          { from: '6', to: '7', text: 'dependence on' },
          { from: '1', to: '4', text: 'dependence on' },
          { from: '5', to: '3', text: 'dependence on' },
          { from: '3', to: '2', text: 'dependence on' },
          { from: '2', to: '8', text: 'dependence on' },
        ]
      }
      this.$refs.seeksRelationGraph.setJsonData(__graph_json_data, (seeksRGGraph) => {
        // 这些写上当图谱初始化完成后需要执行的代码
      })
    },
    onNodeClick(nodeObject, $event) {
      console.log('onNodeClick:', nodeObject)
    },
    onLineClick(lineObject, $event) {
      console.log('onLineClick:', lineObject)
    },
    showNodeTips(nodeObject, $event) {
      this.currentNode = nodeObject
      var _base_position = this.$refs.myPage.getBoundingClientRect()
      console.log('showNodeMenus:', $event, _base_position)
      this.isShowNodeTipsPanel = true
      this.nodeMenuPanelPosition.x = $event.clientX - _base_position.x + 10
      this.nodeMenuPanelPosition.y = $event.clientY - _base_position.y + 10
    },
    hideNodeTips(nodeObject, $event) {
      this.isShowNodeTipsPanel = false
    }
  }
}
</script>

