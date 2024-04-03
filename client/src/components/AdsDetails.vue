<template>
  <div class="ad-details">
    <div class="carousel">
    <img :src="currentImageUrl" :key="currentImageUrl" alt="Product Image" class="ad-image">
      <div class="arrow left" @click="prevImage">&#10094;</div>
      <div class="arrow right" @click="nextImage">&#10095;</div>
   </div>
    <div class="ad-info">
      <h1 class="ad-name"><strong>{{ name }}</strong></h1>
      <p class="ad-price"><strong>Pris: {{ price }}</strong> </p>
      <p class="ad-condition"><strong>Skick: {{ condition }}</strong></p>
      <p class="ad-location"><strong>Plats: {{ location }}</strong></p>
      <p class="ad-category"><strong>Kategori: {{ category }}</strong></p>
      <p class="ad-description"> {{ description }}</p>
      <button @click="contactSeller" class="contact-button" style="color: white">Kontakta säljaren</button>
    </div>
   
    <!-- Seller info -->
  </div>
  <h1 class="seller-about"><strong>Om säljaren</strong></h1>
  <div class="seller-info">
      <img src='/images/profile.png' alt="Profile Image" class="profile-image">
      <div class="seller-id">
        <p class="seller-name"><strong>Anna Andersson</strong></p>
        <p class="seller-liuid"><strong>abc123</strong></p>
      </div>
    </div>
</template>

<script>
export default {
  props: ['id', 'imageUrl', 'name', 'price', 'condition', 'location', 'category', 'description'],
  data () {
    return {
      currentIndex: 0,
      images: ['/images/cykel.png', '/images/apartment.png'],
    }
  },
  computed: {
    currentImageUrl() {
      return this.images[this.currentIndex];
    }
  },
  methods: {
    nextImage() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
    },
    prevImage() {
      this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
    }
  }
};
</script>

<style scoped>

.ad-details {
  display: flex;
  align-items: center;
  text-align: left;
}

.carousel {
  position: relative;
}


.ad-image {
  width: 350px; 
  height: auto;
  margin-left: 50%;
  margin-top: 100px;
}

.arrow {
  position: absolute;
  top: 60%;
  transform: translateY(-50%);
  cursor: pointer;
  font-size: 24px;
  color: rgb(0, 0, 0);
  background-color: rgb(255, 255, 255);
  padding: 10px;
}

.left {
  left: 35%;
}

.right {
  right: -65%;
}

.ad-name {
  font-size: 24px;
  margin-left: 1000 px;
}

.ad-price, .ad-condition, .ad-location, .ad-category, .ad-description {
  font-size: 16px; /* Example: Decrease font size for price */
  margin-bottom: 0;
  margin-right: 300px;
}

.ad-info {
  margin-left: 20%;
  margin-top: 100px;
 }

 .contact-button  {
  margin-top: 50px;
  padding: 10px;
  width: 47%;
  height: 60px;
  border-radius: 20px;
  background-color: #0C254A;
  border-color: #0C254A;
 }

 .seller-about {
  font-size: 20px;
  text-align: left;
  margin-left: 175px;
  margin-top: 20px;
  
 }
 .seller-info {
  display: flex;
  margin-left: 175px;
  text-align: left;
 }


 .profile-image {
  width: 5%;
  height: 5%;
 }

 .seller-name, .seller-liuid {
  margin-bottom: 0;
 }
</style>
