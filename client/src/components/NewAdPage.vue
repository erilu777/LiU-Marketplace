<template>
  <div class="page">
    <h1>Försäljning av {{ category }}</h1>
    <div class="container">
      <form @submit.prevent="addItem">
        <div class="row">
          <input type="text" id="title" v-model="title" placeholder="Titel" class="ctrph">
        </div>
        <div class="row">
          <textarea id="description" v-model="description" placeholder="Beskrivning" class="ctrph"></textarea>
        </div>
        <div class="row">
          <input type="number" id="price" v-model="price" placeholder="Pris" class="ctrph">
        </div>
        <div class="row">
          <select id="area" v-model="area">
            <option value="" disabled selected>Område</option>
            <option value="Linköping">Linköping</option>
            <option value="Norrköping">Norrköping</option>
          </select>
        </div>
        <div class="row">
          <select id="condition" v-model="condition">
            <option value="" disabled selected>Skick</option>
            <option value="Nytt">Nytt</option>
            <option value="Använd_Nyskick">Använd - nyskick</option>
            <option value="Använd_Gott_skick">Använd - gott skick</option>
            <option value="Använd_Slitet_skick">Använd - använt skick</option>
          </select>
        </div>
        <div class="row">
          <input type="file" id="image" accept="image/*" multiple @change="handleImageUpload">
        </div>
        <button type="submit">Gå till betalning</button>
        <!--<button type="submit" @click="navigateToPay">Gå till betalning</button>-->
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      category: '',
      area: '',
      condition: ''
    };
  },
  created() {
    this.category = this.$route.params.category;
  },
  methods: {

    addItem() {
      const token = JSON.parse(sessionStorage.getItem('auth')).token; // Hämta token från sessionStorage
      console.log('Token:', token); // Log the value of the token

      const formData = new FormData();
      formData.append('category', this.category);
      formData.append('title', this.title);
      formData.append('description', this.description);
      formData.append('price', this.price);
      formData.append('condition', this.condition);
      formData.append('area', this.area);
      formData.append('date', new Date().toISOString());
      if(this.image){
        for(let i = 0; i < this.image.length; i++){
          formData.append('image', this.image[i]);
        }
      }

  axios.post('/items', formData, {
    headers: {
      "Authorization": "Bearer " + token,
      'Content-Type': 'multipart/form-data' // Set the content type to multipart/form-data
    }
  })
        .then(response => {
          console.log('Response:', response);
        })
        .catch(error => {
          console.log('Error:', error);
        });
        this.$router.push('/payment');
    },
    handleImageUpload(event) {
      this.image = Array.from(event.target.files);
    },
    navigateToHome() {
      this.$router.push('/');
    },
    navigateToPay() {
      this.addItem();
      this.$router.push('/payment');
    }

  }
};
</script>

<style scoped>
.page {
  padding: 60px;
  min-height: 80vh;
  margin: 0 auto;
}

h1 {
  font-weight: bold;
  font-size: 60px;
  color: #0c264d;
  padding-bottom: 40px;
}

.container {
  background-color: #e7f2f7;
  border: 3px solid #bbd5e9;
  border-radius: 20px;
  width: 700px;
  margin: 0 auto;
  padding: 50px;
}

.row {
  padding: 10px;
  width: 70%;
  margin: 0 auto;
}

button {
  background-color: #0c264d;
  border-color: #bbd5e9;
  padding: 10px;
  width: 40%;
  border-radius: 20px;
  color: white;
  font-weight: bold;
  margin-top: 15px;
}

.ctrph::placeholder {
  text-align: center;
}
</style>