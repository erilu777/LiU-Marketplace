<template>
  <div class="button">
    <button @click="goBack" class="back-button" style="color: white">Tillbaka till annonser</button>
  </div>
  <div class="ad-details">
    <div class="image-container">
    <div class="carousel">
      
    <img :src="currentImageUrl" :key="currentImageUrl" alt="Product Image" class="ad-image">
      <div class="arrow left" @click="prevImage">&#10094;</div>
      <div class="arrow right" @click="nextImage">&#10095;</div>
   </div>
   <div class="thumbnails">
        <img v-for="(image, index) in images" :src="image" :key="index" alt="Product Thumbnail" class="thumbnail" @click="currentIndex = index">
      </div>
    </div>

    <div class="ad-info">
      <h1 class="ad-title"><strong>{{ title }}</strong></h1>
      <p class="ad-description"> {{ description }}</p>
      <p class="ad-price"><strong>Pris: {{ price }} kr</strong> </p>
      <p class="ad-condition"><strong>Skick: {{ condition }}</strong></p>
      <p class="ad-area"><strong>Plats: {{ area }}</strong></p>
      <p class="ad-category"><strong>Kategori: {{ category }}</strong></p>
      <p class="ad-date">🕒 {{ new Date(date).toLocaleDateString('sv-SE') + ', ' + new Date(date).toLocaleTimeString('sv-SE', { hour: '2-digit', minute: '2-digit' }) }}</p>      <button @click="contactSeller" class="contact-button" style="color: white">Kontakta säljaren</button>
    </div>
   
    <!-- Seller info -->
  </div>
  <h1 class="seller-about"><strong>Om säljaren</strong></h1>
  <div class="seller-info">
      <img src='/images/profile.png' alt="Profile Image" class="profile-image">
      <div class="seller-id">
        <p class="seller-name"><strong>{{ sellerName }}</strong></p> 
        <p class="seller-liuid"><strong>{{ sellerEmail }}</strong></p>
      </div>
    </div>
</template>

<script>
import { getCondition} from '@/components/getCondition.js';
export default {
  props: ['id'],
  data () {
    return {
      imageUrl: this.$route.query.imageUrl,
      title: this.$route.query.title,
      price: this.$route.query.price,
      condition: getCondition(this.$route.query.condition),
      area: this.$route.query.area,
      category: this.$route.query.category,
      description: this.$route.query.description,
      currentIndex: 0,
      images: ['/images/cykel.png', '/images/apartment.png'],
      date: this.$route.query.date,
      sellerId: this.$route.query.sellerId,
      sellerName: this.$route.query.sellerName,
      sellerEmail: this.$route.query.sellerEmail
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
    },
    goBack() {
      // Navigate back to the all ads page
      this.$router.push({ name: 'buy' });
     },
     contactSeller() {
      // Replace 'seller@example.com' with the actual email address of the seller
      const sellerEmail = 'seller@example.com';
      const subject = 'Angående annons: ' + this.title; // Subject line for the email
      const body = 'Hej,\n\nJag är intresserad av din annons "' + this.title + '".\n\nMed vänliga hälsningar,'; // Body of the email

      // Generate the mailto link with the seller's email, subject, and body
      const mailtoLink = 'mailto:' + encodeURIComponent(sellerEmail) +
                        '?subject=' + encodeURIComponent(subject) +
                        '&body=' + encodeURIComponent(body);

      // Open the email client with the pre-filled email
      window.location.href = mailtoLink;
    }
    }
};
</script>

<style scoped>

.image-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-left: 15%;
}

.ad-details {
  display: flex;
  align-items: top;
  text-align: left;
  margin-top: 80px;
}

.carousel {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.ad-image {
  width: 350px; 
  height: 350px;
  object-fit: cover;
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
  left: -40px;
}

.right {
  right: -40px;
}

.thumbnail {
  margin: 5px 5px;
  border: 1px solid black;
}

.ad-title {
  font-size: 30px;
  margin-top: -20px;
  margin-left: 1000 px;
}


.ad-price, .ad-condition, .ad-area, .ad-category .ad-description {
  font-size: 16px;
  margin-bottom: 0;
  margin-right: 300px;
}

.ad-date {
  font-size: 12px;
  margin-top: 10px;
  margin-right: 300px;
}

.ad-info {
  margin-left: 10%;
  margin-top: 0px;
  width: 600px;
  background-color: #e7f2f7;
  border: 3px solid #bbd5e9;
  border-radius: 20px;
  padding: 50px;
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

 .back-button {
  margin-top: 10px;
  padding: 10px;
  width: auto;
  height: auto;
  border-radius: 20px;
  background-color: #0C254A;
  border-color: #0C254A;
  margin-left: 10px;
 }

 .seller-about {
  font-size: 20px;
  text-align: left;
  margin-left: 175px;
  margin-top: 20px;
  margin-bottom: 0px;
 }

 .seller-info {
  display: flex;
  margin-left: 175px;
  text-align: left;
  margin-bottom: 20px;
  margin-top: 10px;
 }

 .profile-image {
  width: 5%;
  height: 5%;
 }

 .seller-name, .seller-liuid {
  margin-bottom: 0;
 }

 .button {
  margin-top: 20px;
 }

 .back-button {
  display: flex;
 }

 .carousel {
  display: flex;
 } 

  /* Får inte karusellen att funka, blir galen. kollar på det sen. */
 .thumbnails {
    flex-direction: column;
    justify-content: center;
    align-items: flex-start; 
  }

  .thumbnail {
    width: 50px;
    height: auto;
    cursor: pointer;
  }

  .large-image {
  align-self: flex-start; 
  width: 400px;
  height: auto;
}
</style>
