<template>
        <div class="ads">
        <div v-for="ad in ads" :key="ad.id" class="ad">
            <img :src="ad.imageUrl" alt="Product Image" class="ad-image">
            <div class="ad-details">
            <h3 class="ad-title">{{ ad.name }}</h3>
            <p class="ad-price">{{ ad.price }}</p>
            </div>
        </div>
        </div>

  </template>
  
  <script>
  export default {
    data() {
      return {
        ads: [
          { id: 1, imageUrl: '/images/cykel.png', name: 'Damcykel', price: '1200 kr' },
          { id: 2, imageUrl: '/images/apartment.png', name: '2a i Vallastaden', price: '6500 kr' },
          { id: 3, imageUrl: '/images/book.png', name: 'Kursbok i TEIM32', price: '300 kr' },
        ]
      };
    }
  };
  </script>
  
  <style scoped>


  .ads {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    max-width: 100%;
    margin-left: 300px;
    margin-right: 300px;
    margin-top: 20px;
  }
  
  .ad {
    width: calc(33.33% - 20px); /* Three ads per row */
    margin-bottom: 20px;
    border: 2px solid #ccc;
    border-radius: 15px;
    overflow: hidden;
    background-color: #E7F2F7;
    border-color: #BBD5EA;
  }
  
  .ad-image {
    width: 250px;
    height: auto;
    padding: 10px;
    align-items: center;
    max-width: 100%;
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
  