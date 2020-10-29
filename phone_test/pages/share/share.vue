<template>
	<view>
		<page-head title="form"></page-head>
		<view class="uni-padding-wrap uni-common-mt">
			<form @submit="formSubmit">
				<view class="uni-form-item uni-column">
					<view class="title">标题</view>
					<textarea class="uni-textarea" name="title" placeholder="请输入标题"/>
				</view>
				<view class="uni-form-item uni-column">
					<view class="title">内容</view>
					<textarea class="uni-textarea" name="content" placeholder="请输入内容" />
				</view>
				<view>
					<sunui-textarea ref="textarea" indent="0em"></sunui-textarea> <!-- @input="getInput" -->
				</view>
				<view class="index-page">
					<button form-type="submit">GPS分享</button>
					<!-- <uni-popup ref="sharepopup" type="bottom">
						<share-btn :sharedataTemp="sharedata"></share-btn>
					</uni-popup> -->
				</view>
			</form>
		</view>
	</view>
</template>

<script>
	import uniPopup from '../../components/uni-popup/uni-popup.vue';
	import shareBtn from '../../components/share-btn/share-btn.vue';
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			formSubmit: function(e){
				this.data1=(JSON.stringify(e.detail.value))//获取输入的内容
				let data2=((e.detail.value))//获取输入的内容
				// let title=(String(e.detail.value))
				// console.log(JSON.stringify(e.detail.value))
				// console.log(JSON.stringify(this.data))
				//console.log(data1.title)
				// console.log(data2)
				// console.log(data2.title)
				uni.getSystemInfo({
				    success: function (res) {
						let brand=res.brand
						let model=res.model
				        // console.log(data3);
						uni.share({
							provider: "weixin",
							scene: "WXSceneSession",
							type: 0,
							href: "http://127.0.0.1:8080/#/pages/location/location",
							title: data2.title,
							summary:data2.content,//"我正在使用HBuilderX开发uni-app，赶紧跟我一起来体验！",//当作唯一标识
							imageUrl: "https://img-cdn-qiniu.dcloud.net.cn/uniapp/images/uni@2x.png",
							complete: function (res) {
								// let params ={
								// 	"title":data2.title,
								// 	"noncestr": 'yanhailin',
								// 	"content":data2.content,
								// 	"brand1":res.brand
								// },
								//console.log("success:" + JSON.stringify(res));
								// let headers={
								//           "Content-Type":"application/x-www-form-urlencoded",
								//           "Token":`this.userToken`   //设置一下token即可
								//     }
								uni.request({
									url:'http://192.168.31.121:8088/phone/add_gps_position',//需要换成本机的IP地址
									method:'GET',
									header:{ 'content-type': 'application/x-www-form-urlencoded', },
									//data:params,
									data: {
										"title":data2.title,
										noncestr: 'yanhailin',
										"content":data2.content,
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
							// fail: function (err) {
							// 	console.log("fail:" + JSON.stringify(err));
							// },
					});
				    }
				});
			},
			// components: {
			// 	uniPopup,
			// 	shareBtn
			// }
		}
	}
</script>

<style scoped>
	.uni-form-item__title{
		font-size:18px;
		line-height: 18px;
		font-style: inherit;
	}
	.uni-input {
	    height: 40px;
	    line-height: 60px;
	    font-size: 15px;
	    padding: 0px;
	    flex: 1;
	    background-color: #FFFFFF;
	}
	<style>
		.content {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
		}
	
		.logo {
			height: 200rpx;
			width: 200rpx;
			margin-top: 200rpx;
			margin-left: auto;
			margin-right: auto;
			margin-bottom: 50rpx;
		}
	
		.text-area {
			display: flex;
			justify-content: center;
		}
	
		.title {
			font-size: 36rpx;
			color: #8f8f94;
		}
	</style>

	
</style>
