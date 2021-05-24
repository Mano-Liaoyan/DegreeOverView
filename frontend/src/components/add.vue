  	<!--
      	Dialog 对话框
     -->
<template>
    <el-dialog title="创建项目" :visible.sync="dialogFormVisible" width="35%">
		  <el-form ref="tempData" :rules="rules" :model="tempForm" label-position="left" label-width="120px" style="width: 420px; margin-left:50px;">
		    <el-form-item label="项目名称">
		      <el-input v-model="tempForm.projectName" placeholder="请输入项目名称~"/>
		    </el-form-item>
		    <el-form-item label="负责人">
		      <el-input v-model="tempForm.projectManager" placeholder="请输入负责人~"/>
		    </el-form-item>
		    <el-form-item label="项目人员" >
		      <el-input v-model="tempForm.projectMember" placeholder="请输入项目人员~"/>
		    </el-form-item>
		    <el-form-item label="项目描述">
		      <el-input v-model="tempForm.projectDesc" placeholder="请输入项目描述~"/>
		    </el-form-item>
		  </el-form>
		  <div slot="footer" class="dialog-footer">
		    <el-button @click="dialogFormVisible = false">取 消</el-button>
		    <el-button type="primary" @click="createData()">确 定</el-button>
		  </div>
    </el-dialog>
</template>
    
    <script>
    export default {
    
    }
    </script>
    
    <style>
    
    </style>

