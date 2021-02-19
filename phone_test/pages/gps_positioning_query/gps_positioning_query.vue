<template>
	<view>
		<text>1111</text>
		<view>
			<view v-for="(item,index) in address_list":key="index">
				<view class="uni-padding-wrap uni-common-mt">
					<view class="uni-flex uni-row">
						<view class="text">{{item.address}}</view>
					</view>
				</view>	
			</view>
<!-- 			<view v-for="address in address_list" :key="address.id">
				<label class="checkbox">
					<checkbox :value="address.address" /> {{ address.address}}
				</label>
			</view> -->
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return{
				index:0,
				address_list:[]
			}
		},
		onLoad(){
			this.gps_positioning_query();
			this.showImg=true;
		},
		// data() {
		// 	return{
		// 		address_list:[
		// 			{
		// 				"id": 1,
		// 				"address": "2434535",
		// 				"lat": "",
		// 				"lng": ""
		// 			}, {
		// 				"id": 2,
		// 				"address": "",
		// 				"lat": "",
		// 				"lng": ""
		// 			}, {
		// 				"id": 3,
		// 				"address": "",
		// 				"lat": "",
		// 				"lng": ""
		// 			}, {
		// 				"id": 4,
		// 				"address": "",
		// 				"lat": "",
		// 				"lng": ""
		// 			}, {
		// 				"id": 5,
		// 				"address": "湖南省永州市宁远县061县道",
		// 				"lat": "25.452189",
		// 				"lng": "111.901027"
		// 			}
					
		// 		]
		// 	}
		// },
		// onLoad:function(){
		// 	this.gps_positioning_query()},
		methods:{
			gps_positioning_query(){
				uni.getSystemInfo({
					success:function(res){
						let brand=res.brand
						let model=res.model
						console.log(brand,model);
						uni.request({
							url:'http://192.168.43.151:8088/phone/query_gps_position',
							method:'GET',
							header:{ 'content-type': 'application/x-www-form-urlencoded', },
							data:{
								"brand":brand,
								"model":model,
							},
							sslVerify: false,
							success: (res) => {
								console.log('request success', res)
									this.address_list=res.data.address_list
									//var address_list = JSON.parse(JSON.stringify(res.data.address_list))
									// this.address = address
									//console.log(address_list)
								uni.showToast({
									title: '请求成功',
									icon: 'success',
									mask: true,
									//duration: duration
								});
								this.res = '请求结果 : ' + JSON.stringify(res);
							},
							fail: (err) => {
								console.log('request fail', err);
								uni.showModal({
									content: err.errMsg,
									showCancel: false
								});
							},
							complete: () => {
								this.loading = false;
							}
							// success(res) {
							// 	this.address_list=res.data.address_list
							// 	let address = JSON.parse(JSON.stringify(res))
							// 	this.address = address
							// 	console.log(this.address_list)
							// },
						});
					}
				});
			}
		}	
		
	}
</script>

<style>

</style>
<!-- methods: {
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
									url:'http://192.168.43.151:8088/phone/add_gps_position',
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
									},
								});
								
							}
						});
					}
				}
			}
		
		} -->