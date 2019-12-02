<template>
	<div>
			<button
				v-for="tab in tabs"      
				:key="tab"
				@click="selected = tab;"
				:class="['tab-btn', { active: selected === tab }]" >
				{{ tab }}
			</button>

		<div class="cover"></div>

		<component :is="selected" class="tab"></component>
	</div>
</template>

<script>
import SearchTab from '../searchTab/SearchTab.vue';
import PredictTab from '../predictTab/PredictTab.vue';

export default {
  data: function() {
    return {
      tabs: ['SearchTab', 'PredictTab'],
      selected: 'SearchTab'
    };
  },
  components: {
    SearchTab,
    PredictTab
  }
};
</script>

<style>
	@import './home.css'
</style>