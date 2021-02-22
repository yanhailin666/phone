<template>
	<view>
		<view>
			<view v-for="(item,index) in address_list":key="index">
				<view class="nr">
					<p>创建时间:{{item.change_time}}</p>
					<p>参考地址:{{item.address}}</p>
				</view>
			</view>
			<view class="jz">
				<p>------------这是一个分割线------------</p>
			</view>
			<view class="text">
				<p>就会开始的发表发吧 电脑； ；就地方浮动空间放大镜看机会 反对 大家都方便地方说的话反馈上课还是客户端就发上来吧四点九八被市场空间不是连不上了对吧上的分布粒子数量很少的了计划</p>
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
		}	
		
	}
</script>

<style>
.nr{
	border-radius: 25px;
	background: #8AC007;
	padding: 10px; 
	width: 95%;
	height: 45px;
	margin-top: 30rpx;
},
.text{
	margin-top: 60rpx;
	text-indent:50px;
},
.jz{
	margin-top: 30rpx;
	text-align: center;
}
</style>
