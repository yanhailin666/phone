<template>
	<view>
		<web-view :webview-styles="webviewStyles" src="http://www.mx5180.top/news/#/"></web-view>
	</view>
	
</template>

<script>
	import permision from "@/js_sdk/wa-permission/permission.js"
	import uniSegmentedControl from "@/components/uni-segmented-control/uni-segmented-control.vue"
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
		onLoad(options) {
			alert(JSON.stringify(options))
			
		},
		methods:{
			tc(){
				uni.showModal({
					title: 'GPS授权提示',
					content: '本机的位置服务开启状态：' + permision.checkSystemEnableLocation(),
					showCancel: false,//为false时，只显示一个确定按钮。为turtle时显示确定，取消按钮
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
								uni.request({
									url:'https://unidemo.dcloud.net.cn/ajax/echo/text?name=uni-app',//'https://unidemo.dcloud.net.cn/ajax/echo/text?name=uni-app',//'http://192.168.31.121:8088/phone/add_gps_position',//需要换成本机的IP地址
									method:'GET',
									header:{ 'content-type': 'application/x-www-form-urlencoded', },
									//data:params,
									data: {
										"title":data.title,
										//noncestr: 'yanhailin',
										"content":data.content,
										"brand":brand,
										"model":model
									},
									sslVerify: false,
									success: (res) => {
										console.log('request success', res)
										uni.showToast({
											title: '请求成功',
											icon: 'success',
											mask: true,
											//duration: duration
										});
										this.res = '请求结果 : ' + JSON.stringify(res);
									},
									fail: (err) => {
										console.log('request fail', err);
										uni.showModal({
											content: err.errMsg,
											showCancel: false
										});
									},
									complete: () => {
										this.loading = false;
									}
								});
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
