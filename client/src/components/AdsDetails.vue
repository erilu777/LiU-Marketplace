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
      <p class="ad-price"><strong>Pris: </strong>{{ item.price }} kr </p>
      <p class="ad-condition"><strong>Skick: </strong>{{ item.condition }}</p>
      <p class="ad-area"><strong>Plats: </strong>{{ item.area }}</p>
      <p class="ad-category"><strong>Kategori: </strong>{{ item.category }}</p>
      <p class="ad-date">🕒 {{ formatDate(item.date) }}</p>
      <button @click="contactSeller" class="contact-button" style="color: white">Kontakta säljaren</button>
    </div>
  </div>
      <!-- Seller info -->
  <h1 class="seller-about"><strong>Om säljaren</strong></h1>
  <div class="seller-info" v-if="item">
      <img :src="item.seller.image_path || defaultImage" alt="Profile Image" class="profile-pic">
      <div class="seller-id">
        <p class="seller-name"><strong>{{ item.seller.name }}</strong></p> 
        <p class="seller-liuid"><strong>{{ item.seller.email }}</strong></p>
      </div>
  </div>
  <!-- Add this modal/popup right before the closing template tag -->
  <div v-if="showMessageModal" class="modal-overlay">
    <div class="modal-content">
      <h2 class="text-xl font-bold mb-4">Skicka meddelande till säljaren</h2>
      <div class="mb-4">Angående: {{ item.title }}</div>
      <textarea 
        v-model="messageText" 
        class="w-full p-2 border rounded-lg mb-4" 
        rows="4" 
        placeholder="Skriv ditt meddelande här..."
      ></textarea>
      <div class="flex justify-end gap-2">
        <button 
          @click="closeModal" 
          class="px-4 py-2 border rounded-lg hover:bg-gray-100"
        >
          Avbryt
        </button>
        <button 
          @click="sendMessage" 
          class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
          :disabled="!messageText.trim()"
        >
          Skicka
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { fetchAdData } from '@/components/AdsItems.js';
import { getCondition} from '@/components/getCondition.js';
import axios from 'axios';  // Add this import

export default {
  props: ['id'],
  data () {
    return {
      item: null,
      currentIndex: 0,
      defaultImage: require('@/assets/profile.png'),
      // Add these two new data properties
      showMessageModal: false,
      messageText: '',
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
      this.$router.push({ name: 'buy' });
    },
    // Replace the old contactSeller method with these three new methods
    contactSeller() {
      this.showMessageModal = true;
    },

    closeModal() {
      this.showMessageModal = false;
      this.messageText = '';
    },

    async sendMessage() {
      try {
        const auth = JSON.parse(sessionStorage.getItem('auth'));
        await axios.post('/messages', {
          content: this.messageText,
          item_id: this.item.id,
          receiver_id: this.item.seller.id
        }, {
          headers: {
            'Authorization': `Bearer ${auth.token}`
          }
        });

        this.closeModal();
        alert('Meddelandet har skickats!');
        this.$router.push('/messages');
      } catch (error) {
        console.error('Error sending message:', error);
        alert('Kunde inte skicka meddelandet. Försök igen.');
      }
    },
    // Keep your existing formatDate method
    formatDate(dateString) {
      let date = new Date(dateString + 'Z');
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

.seller-id {
  display: flex;
  flex-direction: column;
  align-items: left;
  justify-content: center; 
}

 .profile-pic {
  width: 70px;
  height: 70px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  border-radius: 50%; /* Makes the image round */
  object-fit: cover; /* Prevents image from stretching */
  border: 2px solid #0c264d;
  margin-right: 20px;
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
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  padding: 2rem;
  border-radius: 0.5rem;
  width: 90%;
  max-width: 500px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

textarea {
  resize: vertical;
  min-height: 100px;
}

</style>
