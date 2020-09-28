<template>
	<view>
		<title>商场</title>
		<web-view :webview-styles="webviewStyles" src="https://cn1.mx5180.com/app/index.php?i=1&c=entry&do=pddindex&m=tuike_pdd"></web-view>
	</view>
</template>

<script>
// 在list2detail-list页面接受参数
export default {
	data(){
		return{
			url:'',
			webviewStyles:{
				progress:{
					color:'#FF3333'
				}
			}
		}
	}
}
</script>
<style>
</style>



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
