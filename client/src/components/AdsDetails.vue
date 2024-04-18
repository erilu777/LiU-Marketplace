<template> 
  <div class="breadcrumbs" v-if="item">
    <a href="/#">LiU Marketplace</a> >
    <a href="/#/buy">Köpa</a> >
    <strong style="color: #0C254A">{{item.title}}</strong>
</div>

  <div class="ad-details" v-if="item">
    <div class="image-container">
      <div class="carousel">    
        <img :src="item.images[currentIndex].image_path" :key="currentImageUrl" alt="Product Image" class="ad-image">
        <div class="arrow left" @click="prevImage">&#10094;</div>
        <div class="arrow right" @click="nextImage">&#10095;</div>
      </div>
      <div class="thumbnails">
            <img v-for="(image, index) in item.images" :src="image.image_path" :key="index" alt="Product Thumbnail" class="thumbnail" :class="{ 'active-thumbnail': currentIndex === index }" @click="currentIndex = index">
      </div>
    </div>

    <div class="ad-info">
      <h1 class="ad-title"><strong>{{ item.title }}</strong></h1>
      <p class="ad-description"> {{ item.description }}</p>
      <p class="ad-price"><strong>Pris: {{ item.price }} kr</strong> </p>
      <p class="ad-condition"><strong>Skick: {{ item.condition }}</strong></p>
      <p class="ad-area"><strong>Plats: {{ item.area }}</strong></p>
      <p class="ad-category"><strong>Kategori: {{ item.category }}</strong></p>
      <p class="ad-date">🕒 {{ formatDate(item.date) }}</p>
      <button @click="contactSeller" class="contact-button" style="color: white">Kontakta säljaren</button>
    </div>
  </div>
      <!-- Seller info -->
  <h1 class="seller-about"><strong>Om säljaren</strong></h1>
  <div class="seller-info" v-if="item">
      <img src='/images/profile.png' alt="Profile Image" class="profile-image">
      <div class="seller-id">
        <p class="seller-name"><strong>{{ item.seller.name }}</strong></p> 
        <p class="seller-liuid"><strong>{{ item.seller.email }}</strong></p>
      </div>
  </div>
</template>

<script>
import { fetchAdData } from '@/components/AdsItems.js';
import { getCondition} from '@/components/getCondition.js';

export default {
  props: ['id'],
  data () {
    return {
      item: null,
      currentIndex: 0,
    }
  },
  async created() {
    console.log('Trying to create ad with ID: ', this.id);
    try {
      this.item = await fetchAdData(this.id);
      console.log('Ad data:', this.id);
      console.log('this.item.title: ', this.item.title);
      this.item.condition = getCondition(this.item.condition);
    } catch (error) {
      console.error('Error fetching ad data:', error);
    }
  },
  computed: {
    currentImageUrl() {
      return this.currentIndex;
    }
  },
  methods: {
    nextImage() {
      this.currentIndex = (this.currentIndex + 1) % this.item.images.length;
    },
    prevImage() {
      this.currentIndex = (this.currentIndex - 1 + this.item.images.length) % this.item.images.length;
    },
    goBack() {
      // Navigate back to the all ads page
      this.$router.push({ name: 'buy' });
     },
     contactSeller() {
      // Replace 'seller@example.com' with the actual email address of the seller
      const sellerEmail = this.item.seller.email;
      const subject = 'Angående annons: ' + this.item.title; // Subject line for the email
      const body = 'Hej,\n\nJag är intresserad av din annons "' + this.item.title + '".\n\nMed vänliga hälsningar,'; // Body of the email

      // Generate the mailto link with the seller's email, subject, and body
      const mailtoLink = 'mailto:' + encodeURIComponent(sellerEmail) +
                        '?subject=' + encodeURIComponent(subject) +
                        '&body=' + encodeURIComponent(body);

      // Open the email client with the pre-filled email
      window.location.href = mailtoLink;
    },
    formatDate(dateString) {
      // Convert the dateString to UTC
      let date = new Date(dateString + 'Z');

      // Format the date and time
      let formattedDate = date.toLocaleDateString('sv-SE', { timeZone: 'Europe/Stockholm' });
      let formattedTime = date.toLocaleTimeString('sv-SE', { hour: '2-digit', minute: '2-digit', timeZone: 'Europe/Stockholm' });

      return formattedDate + ', ' + formattedTime;
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
  width: 550px; 
  height: 550px;
  object-fit: contain;
  background-color: transparent;
}

.arrow {
  cursor: pointer;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  font-size: 24px;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
  color: darkgrey;
  background-color: white;
  padding: 10px;
}

.arrow:hover {
  color: black;
}

.left {
  left: -40px;
  border-radius: 3px 0 0 3px;

}

.right {
  right: -40px;
  border-radius: 0 3px 3px 0;

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
  margin-right: 0;
}

.ad-date {
  font-size: 12px;
  margin-top: 10px;
  margin-right: 0;
}

.ad-info {
  margin-left: 5%;
  margin-top: 0px;
  /*background-color: clear;
  border: 3px solid #bbd5e9;*/
  border-radius: 20px;
  padding: 50px;
  width: 500px;
  height: auto;
 }

 .contact-button  {
  margin-top: 30px;
  margin-bottom: 30px;
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
  margin-left: 15%;
  margin-top: 20px;
  margin-bottom: 0px;
 }

 .seller-info {
  display: flex;
  margin-left: 15%;
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

.breadcrumbs {
    font-size: 14px;
    color: black;
    margin-top: 10px;
}

.breadcrumbs a {
    text-decoration: none;
    color: black;
}

.breadcrumbs a:hover {
    color: #0C254A;
}

.active-thumbnail {
  border: 3px solid #0C254A;
}

</style>
