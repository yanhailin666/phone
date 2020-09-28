<template>
    <view>
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
    	this.information_url=e.information_url
		// this.phone=e.phone
		this.url=this.information_url//+this.phone
		console.log(this.url);
    }
}
</script>
<style>
</style>












<!-- <template>
    <view>
        <web-view :webview-styles="webviewStyles" src="https://yhl.free.qydev.com/phone/information"></web-view>
    </view>
</template>
onLoad: function (option) { //option为object类型，会序列化上个页面传递的参数
		this.url=option
  //       console.log(option.information_url); //打印出上个页面传递的参数。
		// console.log(option.phone);
		console.log(this.url);
    }
 -->