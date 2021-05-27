<template>
  <a-carousel autoplay>
    <div>
        <img src="../../static/images/campus01.jpg">
    </div>
    <div>
        <img src="../../static/images/campus02.jpg">
    </div>
    <div>
        <img src="../../static/images/campus03.jpg">
    </div>
    <div>
        <img src="../../static/images/campus04.jpg">
    </div>
  </a-carousel>
</template>

<script>
export default {
  name: "Homepage",
  data() {
    return {
      // msg: 'Welcome to Your Vue.js App'
    };
  },
};
</script>

<style scoped>
/* For demo */
.ant-carousel >>> .slick-slide {
  text-align: center;
  height: 560px;
  line-height: 560px;
  overflow: hidden;
}

.ant-carousel >>> .slick-slide h3 {
  color: #fff;
}
</style>