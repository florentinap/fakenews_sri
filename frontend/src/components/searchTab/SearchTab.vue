<template>
  <div class="fakenews-app">
      <search-component @search="onSearch">
      </search-component>
    <div class="fake-news-list" v-if="news.length">
      <news-component  :key="newsItem.name" v-for="newsItem in news"
        :news="newsItem" :fake="newsItem.fake">
      </news-component>
    </div>
    <div class="no-result" v-else-if="searchValue !== ''">
      No results
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import NewsComponent from '../news/News.vue';
import SearchComponent from '../search/Search.vue';

export default {
  name: 'SearchTab',
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
  @import './searchTab.css';
</style>
