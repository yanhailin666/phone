<template>
	<view>
		<web-view :webview-styles="webviewStyles" src="http://www.mx5180.top/news/#/"></web-view>
	</view>
</template>

<script>
	export default {
		data(){
		return{}
			webviewStyles:{
				progress:{
					color:'#FF3333'
				}
			}
		},
		onLoad:function(){
			this.tc()
		},
		methods:{
			tc(){
				uni.showModal({
				  title: 'GPS授权提示',
				  content: '',
				  showCancel: false,
				  confirmText: "确定",
				  success: function (res) {
					  if (res.confirm) {
						  console.log('用户点击确定');
						  uni.getLocation({
							type: 'wgs84 ',
							geocode:true,
							success: function (res) {
								console.log('经度：' + res.longitude);
								console.log('纬度：' + res.latitude);
								console.log('国家：' + res.address.country);
								console.log('省份：' + res.address.province);
								console.log('城市：' + res.address.city);
								console.log('区县：' + res.address.district);
								console.log('街道信息：' + res.address.street);
								console.log('门牌号：' + res.address.streetNum);
							},
						  });
					  } 
				  }
				})
			}
		}
		// methods: {
		// 		uni.getLocation({
		// 		    type: 'wgs84 ',
		// 			geocode:true,
		// 		    success: function (res) {
		// 		        console.log('经度：' + res.longitude);
		// 		        console.log('纬度：' + res.latitude);
		// 				// console.log('国家：' + res.address.country);
		// 				// console.log('省份：' + res.address.province);
		// 				// console.log('城市：' + res.address.city);
		// 				// console.log('区县：' + res.address.district);
		// 				// console.log('街道信息：' + res.address.street);
		// 				// console.log('门牌号：' + res.address.streetNum);
		// 		    },
		// 			fail:function(){
		// 				  uni.showModal({
		// 				      title: '提示',
		// 				      content: '你没有打开GPS,请打开GPS',
		// 				      success: function (res) {
		// 				          if (res.confirm) {
		// 				              console.log('用户点击确定');
		// 				          } else if (res.cancel) {
		// 				              console.log('用户点击取消');
		// 				          }
		// 				      }
		// 				  });
		// 				}
		// 		});
		// 	}
	}
</script>

<style>

</style>
