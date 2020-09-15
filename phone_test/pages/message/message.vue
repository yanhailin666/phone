<template>
	<view>
		这是短信页面
		{{res}}
	</view>
</template>

<script>
	export default {
		data:{
			res:''	
			},
		onload:function(){
			uni.request({
				url:'http://127.0.0.1:8088/phone.index',
				method:"GET",
				success:function(res){
					console.log(res)
				}
			})
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
