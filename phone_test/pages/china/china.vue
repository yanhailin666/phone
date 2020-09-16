<template>
	<view>
		<view class="page">
			<view v-for="(item,index) in phone":key="index">
				<text>{{item}}</text>
			</view>
		</view>
	</view>
</template>

<script>	
	export default {
		data() {
			return{
				country:[],
				phone:[],
				information:[]
			}
		},
		onLoad:function(){
			uni.request({
				url:'http://127.0.0.1:8088/phone/china',
				success:(res)=>{
					this.country = res.data.country_list;
					this.phone = res.data.phone_list;
					this.information = res.data.information_list;
					console.log(this.phone)
				}
			})
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
