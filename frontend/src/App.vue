<template>
  <div id="fakenews-app">
    <div class="cover"></div>
    <div class="fake-news-search">
      <search-component>
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
import NewsComponent from './components/news/News.vue';
import SearchComponent from './components/search/Search.vue';

export default {
  name: 'app',
  components: {
    NewsComponent,
    SearchComponent
  },
  data() {
    return {
      news: [
      {
        name: "fake news 1",
        content: "this is a fake news bla bla bla bla",
        fake: true
      },
      {
        name: "fake news 2",
        content: "this is NOT a fake news",
        fake: false
      }]
    }
  }
}
</script>

<style>
  @import './app.css';
</style>
