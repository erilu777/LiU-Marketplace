<template>
  <div class="page">
    <h1>{{ pageTitle }}</h1>
    <!-- Search Bar -->
    <div class="search-bar">
      <input type="text" v-model="searchTerm" placeholder="&#128269;" class="search-input">
      <span @click="clearSearch">&#10006;</span>
    </div>
    
    <!-- Categories -->
    <div class="categories">
      <div v-for="category in categories" :key="category.id" 
          :class="{ 'selected': isSelected(category.id), 'selected-text': isSelected(category.id) }" 
          @click="toggleCategory(category.id)" 
          class="category">
        <h2 class="category-name">{{ category.name }}</h2>
      </div>
    </div>
    
    <!--Sort By-->
    <div class="sort-by">
      <span>Sortera efter:</span>
      <select v-model="sortBy">
        <option value="latest">Senast tillagd</option>
        <option value="price">Lägst pris</option>
      </select>
    </div>
    <Ads/>
  </div>
</template>

<script>
import Ads from '@/components/AdsSection.vue';
export default {
  components: {
    Ads
  },
  data() {
    return {
      pageTitle: '',
      searchTerm: '',
      categories: [
        { id: 1, name: 'Cyklar' },
        { id: 2, name: 'Böcker' },
        { id: 3, name: 'Biljetter' },
        { id: 4, name: 'Inredning' },
        { id: 5, name: 'Bostad' },
        { id: 6, name: 'Verktyg' },
        { id: 7, name: 'Övrigt' }
      ],
      selectedCategories: []
    };
},
  methods: {
    toggleCategory(categoryId) {
      const index = this.selectedCategories.indexOf(categoryId);
      if (index === -1) {
        // Category is not selected, add it to selected categories
        this.selectedCategories.push(categoryId);
      } else {
        // Category is already selected, remove it from selected categories
        this.selectedCategories.splice(index, 1);
      }
    },
    isSelected(categoryId) {
      return this.selectedCategories.includes(categoryId);
    },
    clearSearch() {
      this.searchTerm = ''; // Clear the search term
    }
  }
};
</script>

<style scoped>

.categories {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  max-width: (60px);
  margin-top: 20px;
  padding: 0 250px;
}

.category {
  display: flex;
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  margin: 5px;
  padding: 3px 30px; /* Adjust top and bottom padding */
  border: 2px solid #ccc;
  border-radius: 30px;
  width: calc(25% - 20px); 
  max-width: 200px; /* Maximum width of each category */
  background-color: #E7F2F7;
  border-color: #BBD5EA;
}


.category-name {
  font-size: 15px;
  margin-bottom: 5px;
  margin-top: 5px;
}

.search-input {
  margin-top: 20px;
  width: 400px;
}

.selected {
  background-color: #102A50;
  border-color: #000000;
}

.selected-text {
  color: #ffffff; 
}

.sort-by {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
  margin-right: 350px;
}

.sort-by select {
  margin-left: 20px;
  padding: 5px;
}

</style>
