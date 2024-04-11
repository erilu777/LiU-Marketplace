<template>
  <div class="home-page">
    <div class="banner">
      <img src="../assets/home.jpg" alt="Home" class="banner-image">
      <div class="banner-content">
        <h1>making your life easy. and cheap.</h1>
        <img src="../assets/LMlogo.png" alt="Liu Marketplace Logo" class="logo">
      </div>
    </div>
    
    
    <!-- Rest of your page content -->

    <div class="page">
      <!-- Search Bar -->
      <div class="search-bar">
        <input type="search" v-model="searchTerm" placeholder="&#128269;" class="search-input">
      </div>

      <div class="ads">
        <router-link v-for="ad in filteredItems" :key="ad.id"
          :to="{ name: 'AdsDetails', params: { id: ad.id }, query: { imageUrl: ad.imageUrl, title: ad.title, price: ad.price, condition: ad.condition, area: ad.area, category: ad.category, description: ad.description } }"
          class="ad">
          <img :src="ad.imageUrl" alt="Product Image" class="ad-image">
          <div class="ad-details">
            <h3 class="ad-title">{{ ad.title }}</h3>
            <p class="ad-price">{{ ad.price }}</p>
          </div>
        </router-link>
      </div>
    </div>

  </div>


</template>

<script>
import * as ads from '@/components/AdsItems.js';

export default {
  components: {

  },
  data() {
    return {
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
      selectedCategories: [],
      filteredItems: [],
    };
  },
  watch: {
    searchTerm: function () {
      this.filteredItems = ads.adsData.filter((ad) =>
        ad.category && ad.category.toLowerCase().includes(this.searchTerm.toLowerCase())
      );
    },
  },
  created() {
    this.filteredItems = ads.adsData
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
.home-page {
  position: relative;
}

.banner {
  position: relative;
  width: 100%;
}

.banner-image {
  width: 100%;
  height: auto;
}

.banner-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}

h1 {
  color: white;
  margin-top: 30px;
}

.logo {
  margin-top: 100px;
  max-width: 150px;
}


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
  justify-content: center;
  /* Center horizontally */
  align-items: center;
  /* Center vertically */
  margin: 5px;
  padding: 3px 30px;
  /* Adjust top and bottom padding */
  border: 2px solid #ccc;
  border-radius: 30px;
  width: calc(25% - 20px);
  max-width: 200px;
  /* Maximum width of each category */
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

.ads {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  gap: 30px;
  max-width: 70%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  margin-bottom: 20px
}

.ad {
  min-width: 200px;
  width: calc(33.33% - 20px);
  /* Three ads per row */
  border: 2px solid #ccc;
  border-radius: 15px;
  overflow: hidden;
  background-color: #E7F2F7;
  border-color: #BBD5EA;
  text-decoration: none;
}

p {
  color: #102A50;
}

.ad-image {
  width: 250px;
  height: auto;
  padding: 10px;
  align-items: center;
  max-width: 100%;
  margin-top: 10px;
}

.ad-details {
  padding: 10px;
}

.ad-title {
  margin-top: 0;
  margin-bottom: 5px;
  font-size: 15px;
  color: #102A50;
  font-weight: bold;
  text-align: left;
}

.ad-price {
  margin: 0;
  text-align: left;
}
</style>
