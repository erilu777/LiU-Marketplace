<template>
  <div class="page">
    <!-- Search Bar -->
    <div class="search-bar">
      <input type="search" v-model="searchTerm" placeholder="&#128269;" class="search-input">
    </div>

    <!-- Categories -->
    <div class="categories">
      <div v-for="category in categories" :key="category.id"
        :class="{ 'selected': isSelected(category.name), 'selected-text': isSelected(category.name) }"
        @click="toggleCategory(category.name)" class="category">
        <h2 class="category-name">{{ category.name }}</h2>
      </div>
    </div>

    <!--Sort By-->
    <div class="sort-by">
      <span>Välj område:</span>
      <select v-model="choose" @change="sortByArea">
        <option value="alla">Alla områden</option>
        <option value="linkoping">Linköping</option>
        <option value="norrkoping">Norrköping</option>
      </select>
      <span>Sortera efter:</span>
      <select v-model="sortBy" @change="handleSort">
        <option disabled value="">Sortera efter</option>
        <option value="price">Lägst pris</option>
        <option value="latest">Senaste</option>
      </select>
    </div>

    <div class="ads">
      <router-link v-for="ad in filteredItems" :key="ad.id"
        :to="{ name: 'AdsDetails', params: { id: ad.id }, query: { imageUrl: ad.imageUrl, title: ad.title, price: ad.price, condition: ad.condition, area: ad.area, category: ad.category, description: ad.description, date: ad.date, sellerId: ad.seller.id, sellerName: ad.seller.name, sellerEmail: ad.seller.email} }"
        class="ad">
        <img :src="ad.imageUrl" alt="Product Image" class="ad-image">
        <div class="ad-details">
          <h3 class="ad-title">{{ ad.title }}</h3>
          <p class="ad-price">{{ ad.price }} kr</p>
          <p class="ad-area">{{ ad.area }}</p>
          <p class="ad-date">{{ new Date(ad.date).toLocaleDateString('sv-SE')  }}</p>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import { fetchAdsData } from '@/components/AdsItems.js';

export default {
  components: {

  },
  data() {
    return {
      searchTerm: '',
      sortBy: '',
      choose: 'alla',
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
      items: [],
    };
  },
  async mounted() {
    this.items = await fetchAdsData();
    this.filteredItems = this.items;
    this.items.forEach(item => {
      console.log('Item area:', item.area);
    });
  },
  watch: {
    searchTerm: function () {
      this.filteredItems = this.items.filter((item) =>
        (item.category && item.category.toLowerCase().includes(this.searchTerm.toLowerCase())) ||
        (item.title && item.title.toLowerCase().includes(this.searchTerm.toLowerCase()))
      );
    },
  },
  methods: {
    toggleCategory(categoryName) {
      if (!this.selectedCategories.includes(categoryName)) {
        // Category is not selected, add it to selected categories
        this.selectedCategories.push(categoryName);
      } else {
        // Category is already selected, remove it from selected categories
        const index = this.selectedCategories.indexOf(categoryName);
        this.selectedCategories.splice(index, 1);
      }
      this.filterByCategory();
    },

    filterByCategory() {
      if (this.selectedCategories.length === 0) {
        // No category selected, show all items
        this.filteredItems = this.items;
      } else {
        // Filter items based on selected categories
        this.filteredItems = this.items.filter(item => this.selectedCategories.includes(item.category));
      }
    },
    isSelected(categoryName) {
      return this.selectedCategories.includes(categoryName);
    },
    clearSearch() {
      this.searchTerm = ''; // Clear the search term
    },
    sortByPrice() {
      this.filteredItems.sort((a, b) => a.price - b.price);
    },
    sortByDate() {
      this.filteredItems.sort((a, b) => b.id - a.id);
    },
    sortByArea() {
      if (this.choose === 'linkoping' || this.choose === 'norrkoping') {
        const chosenArea = this.choose === 'linkoping' ? 'Linköping' : 'Norrköping';
        this.filteredItems = this.items.filter(item => {
          console.log('Item area:', item.area);
          return item.area === chosenArea;
        });
      } else if (this.choose === 'alla') {
        this.filteredItems = this.items;
        this.sortBy = ''; // Reset sortBy when selecting "Alla Områden"
      }
      console.log('Filtered items:', this.filteredItems);
      this.handleSort();
    },

    handleSort() {
      if (this.sortBy === 'price') {
        this.sortByPrice();
      } else if (this.sortBy === 'latest') {
        this.sortByDate();
      }
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
  min-width: 100px;
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
  margin-right: 20%;
}

.sort-by select:first-of-type {
  margin-right: 20px;
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
  font-size: 25px;
  color: #102A50;
  font-weight: bold;
  text-align: left;
}


.ad-area, .ad-date, .ad-price {
  margin: 0;
  text-align: left;
}
</style>
