<template>
	<view>
		<view class="page">
			<button type="default" @click="china">中国</button>
			<button type="default" @click="overseas">海外</button>
		</view>
	</view>
</template>

<script>	
	export default {
		data() {
			return {
				
			}
		},
		methods:{
			china(){
				uni.navigateTo({
					   url:"/pages/china/china"    //这边的url前面多个斜杠哦！！！！！！
				 })
				},
			overseas(){
				uni.navigateTo({
					   url:"/pages/overseas/overseas"//这里不能接导航栏的url
				 })
			}
		}
	}
</script>

<style>

</style>
