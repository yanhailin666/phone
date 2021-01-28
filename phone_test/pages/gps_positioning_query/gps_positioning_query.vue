<template>
	<view>
		<text>{{address}}</text>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		onLoad:function () {
			this.gps_positioning_query()
		}
		},
		methods: {
			gps_positioning_query(){
					let data = this.addressData;
						//console.log(JSON.stringify(data))
					if (!bottomImageMenu) {//获取手机信息
									bottomImageMenu = new BottomImageMenu(this.menus, (menus,provider, scene) => {
									let time=new Date().getTime()
									uni.getSystemInfo({
									    success: function (res) {
											let brand=res.brand
											let model=res.model
											uni.request({
												url:'http://192.168.0.183:8088/phone/add_gps_position',
												method:'GET',
												header:{ 'content-type': 'application/x-www-form-urlencoded', },
												data:{
													"brand":brand,
													"model":model,
												},
												success(res) {
													this.address_list=res.data.address_list
													let address = JSON.parse(JSON.stringify(res))
													this.address = address
													console.log(this.address_list)
												}
											})
											
										},
									})
								}
							}
						}
			
		}
	}
</script>

<style>

</style>
