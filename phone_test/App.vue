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
	/*每个页面公共css */
	.page{
		width: 100%;
		height: 100%;
		background-color: #ffffff;
		position: absolute;
		/*background:url(static/ico/kpy.jpg)背景图片*/
		
	}
</style>
