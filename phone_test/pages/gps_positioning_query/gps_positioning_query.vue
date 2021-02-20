<template>
	<view>
		<text>1111</text>
		<view>
			<view v-for="(item,index) in address_list":key="index">
				<view class="text">{{item}}</view>
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
	var _self;
	export default {
		data() {
			return{
				address_list:[]
			}
		},
		// created() {
		// 	_self=get_mobile_information
		// },
		onLoad(){
			this.get_mobile_information();
			this.gps_positioning_query();
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
			get_mobile_information(){
				uni.getSystemInfo({
					success:function(res){
						this.brand=res.brand
					//var brand=res.brand
					var model=res.model
					console.log(brand,model);
					}
				});
			},
			gps_positioning_query(){
				uni.request({
					url:'http://192.168.0.106:8088/phone/query_gps_position',
					method:'GET',
					header:{ 'content-type': 'application/x-www-form-urlencoded', },
					data:{
						"brand":this.brand,
						"model":"BKL-AL20",
					},
					success:(res)=>{
						this.address_list=res.data.address_list
						//let address = JSON.parse(JSON.stringify(res))
						//this.address = address
						console.log(this.address_list)
					},
				});
			}
			// gps_positioning_query(){
			// 	uni.request({
			// 		url:'http://192.168.0.106:8088/phone/query_gps_position',
			// 		method:'GET',
			// 		header:{ 'content-type': 'application/x-www-form-urlencoded', },
			// 		uni.getSystemInfo({
			// 			success:function(res){
			// 			let brand=res.brand
			// 			let model=res.model
			// 			console.log(brand,model);
			// 			}
			// 		});
			// 		data:{
			// 			"brand":brand,
			// 			"model":model,
			// 		},
			// 		success: (res) => {
			// 			console.log('request success', res)
			// 			this.address_list1=res.data.address_list
			// 				// this.address_list1=JSON.parse(JSON.stringify(res.data.address_list))
			// 				//var address_list = JSON.parse(JSON.stringify(res.data.address_list))
			// 				// this.address = address
			// 				console.log(this.address_list1)
			// 			// uni.showToast({
			// 			// 	title: '请求成功',a
			// 			// 	icon: 'success',
			// 			// 	mask: true,
			// 				//duration: duration
			// 			// });
			// 			//this.res = '请求结果 : ' + JSON.stringify(res);
			// 		},
			// 		fail: (err) => {
			// 			console.log('request fail', err);
			// 			uni.showModal({
			// 				content: err.errMsg,
			// 				showCancel: false
			// 			});
			// 		},
			// 	})
			// }
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