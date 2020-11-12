<template>
    <view class="content">
        <view class="row b-b">
            <text class="tit">标题</text>
            <input class="input" type="text" v-model="addressData.title" placeholder="请输入标题" placeholder-class="placeholder" />
        </view>
        <view class="row b-b">
            <text class="tit">内容</text>
            <input class="input" type="text" v-model="addressData.content" placeholder="内容" placeholder-class="placeholder" />
        </view>
        <button class="add-btn" @click="showMenu">GPS分享</button>
    </view>
</template>
 
<script>
	import BottomImageMenu from '@/components/zh-bottom-image-menu/zh-bottom-image-menu.js'
	var bottomImageMenu = null
    export default {
        data() {
            return {
                addressData: {
                    title: '',
                    content: '',
                }
            }
        },
		computed: {
				menus() {
				  return [
					{
					  icon: '/static/index/weixin.png',
					  label: '微信',
					  provider: "weixin",
					  scene: "WXSceneSession",
					  type: 0
					 //  onClick() {
						// uni.showToast({ title: '点击了:微信,这是一个写在数据里的回调', icon: 'none' })
					 //  }
					},
					{
					  icon: '/static/index/qq.png',
					  label: 'QQ',
					  provider: "weixin",
					  scene: "WXSceneSession",
					  type: 0
					},
					{
					  icon: '/static/index/pengyouquan.png',
					  label: '朋友圈',
					  provider: "weixin",
					  scene: "WXSceneSession",
					  type: 0
					},
					{
					  icon: '/static/index/weibo.png',
					  label: '微博',
					  provider: "weixin",
					  scene: "WXSceneSession",
					  type: 0
					},
					// {
					//   icon: '/static/index/copy.png',
					//   label: '复制链接'
					// },
				  ]
				}
		},
        onLoad(option) {},
        methods: {
            //提交
            // confirm() {
            //     let data = this.addressData;
            //     console.log(JSON.stringify(data))
            // },
			showMenu() {
				let data = this.addressData;
				//console.log(JSON.stringify(data))
			  if (!bottomImageMenu) {
				bottomImageMenu = new BottomImageMenu(this.menus, (menus,provider, scene) => {
				let time=new Date().getTime()
				uni.getSystemInfo({
				    success: function (res) {
						let brand=res.brand
						let model=res.model
				        // console.log(data3);
						uni.share({
							provider:menus.provider,
							scene:menus.scene,
							type: 0,
							href: "https://cn3.mx5180.com/#/?tima="+time+"&title="+data.title+"&content="+data.content,
							title: data.title,
							summary:data.content,//"我正在使用HBuilderX开发uni-app，赶紧跟我一起来体验！",//当作唯一标识
							imageUrl: "https://img-cdn-qiniu.dcloud.net.cn/uniapp/images/uni@2x.png",
							success: function (res) {
								// let params ={
								// 	"title":data2.title,
								// 	"noncestr": 'yanhailin',
								// 	"content":data2.content,
								// 	"brand1":res.brand
								// },
								console.log("success:" + JSON.stringify(res));
								// let headers={
								//           "Content-Type":"application/x-www-form-urlencoded",
								//           "Token":`this.userToken`   //设置一下token即可
								//     }
								uni.request({
									url:'http://192.168.43.245:8088/phone/add_gps_position',//'https://unidemo.dcloud.net.cn/ajax/echo/text?name=uni-app',//'http://192.168.31.121:8088/phone/add_gps_position',//需要换成本机的IP地址
									method:'GET',
									header:{ 'content-type': 'application/x-www-form-urlencoded', },
									//data:params,
									data: {
										"title":data.title,
										//noncestr: 'yanhailin',
										"content":data.content,
										"brand":brand,
										"model":model,
										"time":time,
									},
									sslVerify: false,
									success: (res) => {
										console.log('request success', res)
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
								});
							},
							fail: function (err) {
								console.log("fail:" + JSON.stringify(err));
							},
					});
				    }
				});
				})
			
			  }
			  bottomImageMenu.show()
			}
        },
		onLoad() {
			bottomImageMenu = new BottomImageMenu(menus,provider, scene)
		}
    }
</script>
 
<style lang="scss">
    page {
        padding-top: 16upx;
    }
 
    .row {
        display: flex;
        align-items: center;
        position: relative;
        padding: 0 30upx;
        height: 110upx;
        background: #fff;
 
        .tit {
            flex-shrink: 0;
            width: 120upx;
            font-size: 30upx;
 
        }
 
        .input {
            flex: 1;
            font-size: 30upx;
 
        }
 
        .icon-shouhuodizhi {
            font-size: 36upx;
 
        }
    }
 
    .add-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 690upx;
        height: 80upx;
        margin: 60upx auto;
        background-color: rgb(28, 42, 134);
        color: #fff;
 
        border-radius: 10upx;
        box-shadow: 1px 2px 5px rgba(28, 42, 134, 0.4);
    }
</style>