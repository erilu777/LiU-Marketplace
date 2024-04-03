<template>
        <div class="ads">
          <router-link v-for="ad in ads" :key="ad.id" :to="{ name: 'AdsDetails', params: { id: ad.id }, query: { imageUrl: ad.imageUrl, name: ad.name, price: ad.price, condition: ad.condition, location: ad.location, category: ad.category, description: ad.description }}" class="ad">
            <img :src="ad.imageUrl" alt="Product Image" class="ad-image">
            <div class="ad-details">
            <h3 class="ad-title">{{ ad.name }}</h3>
            <p class="ad-price">{{ ad.price }}</p>
            </div>
          </router-link>
        </div>

  </template>
  
  <script>
  export default {
    data() {
      return {
        ads: [
          { id: 1, imageUrl: '/images/cykel.png', name: 'Damcykel', price: '1200 kr', condition:'', location:'', category:'', description: 'More information about Damcykel'  },
          { id: 2, imageUrl: '/images/apartment.png', name: '2a i Vallastaden', price: '6500 kr', condition: 'Använd - Gott skick', location: 'Linköping', category: 'Lägenhet', description: 'Hyr ut min lägenhet pga utbyte mellan maj - december. 2a på 35 kvm. Belägen i ett lugnt och välskött område.'  },
          { id: 3, imageUrl: '/images/book.png', name: 'Kursbok i TEIM32', price: '300 kr',  details: 'More information about Kursbok i TEIM32'  },
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
    margin-bottom:  50px;
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
  