<template>
	<view>
		<view class="page">
			<view v-for="(item,index) in phone":key="index">
				<!--text>{{item}}</text-->
				<button type="default">{{item}}</button>
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
					// //JSON.parse()【从一个字符串中解析出json对象】
					// //JSON.stringify()【从一个对象中解析出字符串】
					// let table = JSON.parse(JSON.stringify(res))
					// this.tableList = table
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
