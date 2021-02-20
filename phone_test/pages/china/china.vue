<template>
	<view>
		<page-head title="view"></page-head>
		<view v-for="(item,index) in phone_list":key="index">
			<view class="uni-padding-wrap uni-common-mt">
				<view class="uni-flex uni-row">
					<view class="text" style="width: 100rpx;">{{item.country}}</view>
					<view class="text" style="-webkit-flex: 1;flex: 1;"  @click="copy(item.phone,item.information_url)">{{item.phone}}</view>
				</view>
			</view>	
		</view>
	</view>
	<!-- <view>
		<view class="uni-flex uni-row">
			<view v-for="(item,index) in phone_list":key="index">
				<view class="text" style="width: 200rpx;">{{item.country}}</view>
				<button class="text" style="-webkit-flex: 1;flex: 1;" type="default" @click="comment(item.information_url)">{{item.phone}}</button>
			</view>
		</view>
	</view> -->
</template>

<script>	
	export default {
		data() {
			return{
				showImg:false,
				phone_list:[]
			}
		},
		onLoad(){
			this.getList();
			this.showImg=true;
		},
		methods: {
			copy(value,information_url){
				uni.showModal({
					title:"复制内容",
					content:value,//模板中提示的内容
					confirmText:"复制并跳转",
					showCancel:false,
				  success:()=>{//点击复制内容的后调函数
				    //uni.setClipboardData方法就是讲内容复制到粘贴板
				    uni.setClipboardData({
				      data:value,//要被复制的内容
				      success:()=>{//复制成功的回调函数
						uni.navigateTo({
							url:'../message/message?information_url='+information_url,
								})
							}	
						});
					}	
				});
			},
			comment:function(information_url){
					uni.navigateTo({
						url:'../message/message?information_url='+information_url,
						//url:'../message/message?information_url='+information_url+'&phone='+phone
					});
				},
			handleClick(item) {
				plus.webview.open(item.information_url + item.phone); //定义一个方法直接跳转到url
			},
			getList(){
			uni.request({
				url:'http://192.168.0.106:8088/phone/china',
				success:(res)=>{
					this.phone_list=res.data.json_list
					// this.country = res.data.country_list;
					// this.phone = res.data.phone_list;
					// this.information = res.data.information_list;
					// //JSON.parse()【从一个字符串中解析出json对象】
					// //JSON.stringify()【从一个对象中解析出字符串】
					let table = JSON.parse(JSON.stringify(res))
					this.tableList = table
					console.log(this.phone_list)
				}
			})
			},
		}
	}
</script>

<style>
	.flex-item {
		width: 33.3%;
		height: 200rpx;
		text-align: center;
		line-height: 200rpx;
	}

	.flex-item-V {
		width: 100%;
		height: 150rpx;
		text-align: center;
		line-height: 150rpx;
	}

	.text {
		margin: 15rpx 10rpx;
		padding: 0 20rpx;
		background-color: #ebebeb;
		height: 70rpx;
		line-height: 70rpx;
		text-align: center;
		color: #777;
		font-size: 26rpx;
	}
	
	.desc {
		/* text-indent: 40rpx; */
	}
</style>
