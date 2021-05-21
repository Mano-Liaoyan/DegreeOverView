<template>
    <div class="loginContain">
        <div class="loginBox">
            <h2 class="loginH2"><strong>Vue</strong> 后台管理系统</h2>
            <el-form :model="loginForm" :rules="loginFormRules" ref="loginForm" label-position="left" label-width="0px" class="login-form">
                <el-form-item prop="username">
                    <el-input type="text" v-model="loginForm.username" auto-complete="off" placeholder="请输入账号">
                        <i slot="prefix" class="el-input__icon el-icon-user-solid"></i>
                    </el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" v-model="loginForm.password" auto-complete="off" placeholder="密码">
                        <i slot="prefix" class="el-input__icon el-icon-lock"></i>
                    </el-input>
                </el-form-item>
                <el-form-item style="width:100%;">
                    <el-button type="primary" style="  width: 100%; background: #19b9e7;">登 录</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            logining: false,
            loginForm: {
                username: 'admin',
                password: '123456',
            },
            notifyObj: null,
            loginFormRules: {
                username: [{ required: true, message: '请输入账号', trigger: 'blur' }],
                password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
            },
        }
    },
}
</script>

<style lang="scss" scoped>
$inputHeight: 48px;

.loginContain {
    height: 100%;
    width: 100%;
    background: url(../../assets/img/loginbg.jpg) no-repeat center center;
    background-size: 100% 100%;
    overflow: hidden;
}
.loginBox {
    height: 455px;
    width: 550px;
    margin: 0 auto;
    position: relative;
    top: 20%;
}
.loginH2 {
    font-size: 28px;
    color: #fff;
    text-align: center;
}

.el-input {
    background-color: transparent;
    border-radius: 20px;
    height: $inputHeight;
    color: #ffffff !important;
    border: rgba(255, 255, 255, 0.2) 2px solid !important;
}
::v-deep .el-input__inner {
    padding-left: 30px;
    background-color: transparent !important;
    border: none !important;
    height: $inputHeight !important;
    color: #ffffff !important;
}
.login-form {
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    margin: 10px auto;
    width: 380px;
    padding: 35px 35px 15px 35px;
}
</style>
