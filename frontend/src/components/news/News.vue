<template>
	<div class="news-item">
		<div class="news-header">
			<div class="news-name">
				{{ news.name }}
			</div>
			<div class="news-subject">
				{{ news.subject }}
			</div>
			<div class="fake">
				{{ news.label }}
			</div>
		</div>
		<div class="news-content">
			{{ news.statement }}
		</div>
	</div>
</template>

<script>
	export default {
		name: 'NewsItem',
		props: {
			news: {
				type: Object,
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