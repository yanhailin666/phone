<template>
	<view>
		<text>1111</text>
		<view>
			<view v-for="(item,index) in address_list":key="index">
				<view class="text">{{item.address}}</view>
			</view>
		</view>
	</view>
</template>

<script>
	var _self;
	export default {
		data() {
			return{
				address_list:[],
			}
		},
		onLoad(){
			//执行顺序
			this.get_mobile_information();
			this.brand=getApp().globalData.brand
			this.model=getApp().globalData.model
			this.gps_positioning_query();
		},
		methods:{
			get_mobile_information(){
				uni.getSystemInfo({
					success:function(res){
					//this.brand=res.brand
					// let brand=res.brand
					// var model=res.model
					getApp().globalData.brand=res.brand//修改全局变量数据，在onLoad中注意顺序
					getApp().globalData.model=res.model
					//console.log(brand,model);
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
						"model":this.model,
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