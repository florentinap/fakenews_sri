<template>
	<div class="news-item">
		<div class="news-header">
			<div class="news-name">
				{{ news.name }}
			</div>
			<div class="fake" v-if="fake">
				FAKE
			</div>
		</div>
		<div class="news-content">
			{{ news.content }}
		</div>
	</div>
</template>

<script type="text/javascript">
	export default {
		name: 'NewsItem',
		props: {
			news: {
				type: String,
				required: true
			},
			fake: {
				type: Boolean
			}
		}
	}
</script>

<style>
	@import './news.css'
</style>