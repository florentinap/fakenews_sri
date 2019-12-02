<template>
	<div class="predict">
		<textarea class="predict-text-area" v-model="predictText"></textarea>
		<button class="predict-button" @click="onClick">
			PREDICT
		</button>
		<div class="fake-news-list">
			<news-component  :key="newsItem.name" v-for="newsItem in news"
				:news="newsItem" :fake="newsItem.fake">
			</news-component>
    </div>
	</div>
</template>

<script>
import axios from 'axios';
import NewsComponent from '../news/News.vue';

	export default {
		name: 'PredictTab',
		components: {
			NewsComponent
		},
		data() {
			return {
				predictText: '',
				news: []
			}
		},
		methods: {
			onClick() {
				const path = `http://localhost:5000/predict?query=${this.predictText}`;
				axios.get(path)
					.then((res) => {
						this.news.push({statement: this.predictText, label: res.data})
						this.predictText = '';
					})
					.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
				});
			}
		}
	}
</script>

<style>
	@import './predictTab.css'
</style>