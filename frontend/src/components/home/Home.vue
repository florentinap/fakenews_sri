<template>
  <div class="fakenews-app">
    <div class="cover"></div>
    <div class="fake-news-search">
      <search-component @search="onSearch">
      </search-component>
    </div>
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
import SearchComponent from '../search/Search.vue';

export default {
  name: 'Home',
  components: {
    NewsComponent,
    SearchComponent
  },
  data() {
    return {
      news: '',
      searchValue: ''
    }
  },
  methods: {
    getNews() {
      const path = `http://localhost:5000/search?query=${this.searchValue}`;
      axios.get(path)
        .then((res) => {
          this.news = res.data;
        })
        .catch((error) => {
		// eslint-disable-next-line
          console.error(error);
        });
    },
    onSearch(value) {
      this.searchValue = value;
      this.getNews();
    }
  }
}
</script>

<style>
  @import './home.css';
</style>
