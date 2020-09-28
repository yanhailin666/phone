<script>
import uniNavBar from "@/components/uni-nav-bar/uni-nav-bar.vue"
	export default {
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		},
		components: {uniNavBar},
		
	}
</script>

<style>
	/* #ifndef APP-PLUS-NVUE */
	/* uni.css - 通用组件、模板样式库，可以当作一套ui库应用 */
	@import './common/uni.css';
	
	/* 以下样式用于 hello uni-app 演示所需 */
	/*每个页面公共css */
	.page{
		width: 100%;
		height: 100%;
		background-color: #ffffff;
		position: absolute;
		/*background:url(static/ico/kpy.jpg)背景图片*/
	}
	.uni-header-logo {
	    padding: 30rpx;
	    flex-direction: column;
	    justify-content: center;
	    align-items: center;
	    margin-top: 10rpx;
	}
	
	.uni-header-image {
	    width: 100px;
	    height: 100px;
	}
	
	.uni-hello-text {
	    color: #7A7E83;
	}
	
	.uni-hello-addfile {
	    text-align: center;
	    line-height: 300rpx;
	    background: #FFF;
	    padding: 50rpx;
	    margin-top: 10px;
	    font-size: 38rpx;
	    color: #808080;
	}
	/* #endif*/
</style>
