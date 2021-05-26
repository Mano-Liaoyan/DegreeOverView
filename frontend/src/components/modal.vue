<template>
    <div>
        <!--添加按钮和模态框-->
        <a-button type="primary" @click="showModal">
            添加
        </a-button>
        <a-modal
                :visible="visible"
                :title= "modelTitle"
                okText='确认'
                cancel-text="取消"
                @cancel="handleCancel"
                @ok="handleOk"
        >
            <!--表单 并将表单的值绑定到this.from-->
            <a-form layout='vertical' :form="form">
                <!--每一项元素-->
                <a-form-item label='用户名'>
                    <a-input
                            v-decorator="[
                                      'username',
                                      {
                                        rules: [{ required: true, message: '请填写登录用户名!' }],
                                      }
                                ]"
                    />
                </a-form-item>
                <a-form-item label='密码'>
                    <a-input
                            type='password'
                            v-decorator="[
                                      'password',
                                      {
                                        rules: [{ required: true, message: '请填写登录密码!' }],
                                      }
                                ]"
                    />
                </a-form-item>
                <a-form-item label="状态">
                    <a-radio-group
                            v-decorator="[
                                  'status',
                                      {
                                        initialValue: '1',
                                      }
                                ]"
                    >
                        <a-radio value='1'>启用</a-radio>
                        <a-radio value='0'>禁用</a-radio>
                    </a-radio-group>
                </a-form-item>
            </a-form>
        </a-modal>
    </div>
</template>

<script>
    export default {
        //el 创建前
        beforeCreate() {
            //创建表单
            this.form = this.$form.createForm(this, { name: 'form_in_modal' });
        },
        data() {
            return {
                visible: false,
                //模态对话框标题
                modelTitle: '模态框标题',
            };
        },
        methods: {
            //显示模态框
            showModal() {
                this.visible = true;
            },
            //关闭模态框
            handleCancel() {
                this.visible = false;
            },
            //点击确认
            handleOk() {
                const form = this.form;
                form.validateFields((err, values) => {
                    if (err) {
                        return;
                    }
                    console.log('form 表单内容: ', values);
                    form.resetFields();
                    this.visible = false;
                });
            },
        },
    };
</script>