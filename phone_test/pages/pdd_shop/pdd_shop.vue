<template>
    <view>
		<head>
			<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests" />
		</head>
		<web-view :webview-styles="webviewStyles" :src="url"></web-view>
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
	},
    onLoad(e) {
    	this.pdd_url=e.pdd_url
		this.url=this.pdd_url
		console.log(this.url);
    }
}
</script>
<style>
</style>