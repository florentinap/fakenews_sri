<template>
	<div class="search-news">
		<input class="search-input" type="search" v-model="searchValue" @change="onChange">
		<button class="search-icon" @click="onClick"></button>
	</div>
</template>

<script>
	export default {
		name: 'searchNews',
		data() {
			return {
				searchValue: ''
			}
		},
		methods: {
			onClick() {
				this.$emit('search', this.searchValue);
			},
			onChange() {
				this.$emit('search', this.searchValue);
			}
		}
	}
</script>

<style>
	@import './search.css';
</style>