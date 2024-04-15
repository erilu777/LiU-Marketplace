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
      filteredItems: [],
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

.search-input {
  margin-top: 20px;
  width: 400px;
}

.selected-text {
  color: #ffffff;
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
