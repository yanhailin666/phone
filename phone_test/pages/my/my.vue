<template>
  <div class="test-component">
	<hm-head-portrait-card :options="options"></hm-head-portrait-card>
	<!-- <button @click="points_query">积分查询</button>-->
	<button class="click" @click="gps_positioning_query">GPS定位查询</button>
	<!--button @click="IP_location_query">ip定位查询</button> -->
  </div>
	
</template>
<script>
	import HmHeadPortraitCard from '@/components/hm-head-portrait-card/index.vue'

export default {
  components: { HmHeadPortraitCard },
  data() {
    return {
      options: {
          actionBg:
            '/static/hm-head-portrait-card/images/img_25814_0_0.png',
          avator:
            '/static/hm-head-portrait-card/images/img_25814_0_1.png',
          name: '严海林',
          info: '旅行社代理人',
          num: '1570',
          // num2: '2570',
          // num3: '230',
          // fans: '积分',
          // article: '文章',
          attention: '积分'
        }
    };
  },
  methods: {
    onClick: function(e) {
      console.log('onClick');
    },
	gps_positioning_query(){
		uni.navigateTo({
			url:'../gps_positioning_query/gps_positioning_query'
		})
	}
  }
};
</script>
<style>
	.click{
		border-radius: 25px;
		background: #e3e3e3;
	}
</style>