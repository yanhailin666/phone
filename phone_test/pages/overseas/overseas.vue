<template>
	<view>
		<view class="page">
			<view v-for="(item,index) in phone_list":key="index">
				<button type="default" @click="handleClick(item)">{{item.phone}}</button>
			</view>
		</view>
	</view>
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
			handleClick(item) {
				plus.webview.open(item.information_url + item.phone); //定义一个方法直接跳转到url
			},
			getList(){
			uni.request({
				url:'https://yhl.free.qydev.com/phone/overseas',
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

</style>
