<template>
	<view>
		<text>sfjeref[oeruf[]]</text>
		<swiper-item v-for="(item,phone) in phone" :key="phone">
			<view>
				<text :a="item.phone"></text>
			</view>
			
		</swiper-item>
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
				url:'http://127.0.0.1:8088/phone/home',
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
