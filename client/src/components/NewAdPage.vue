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
                    <option value="linkoping">Linköping</option>
                    <option value="norrkoping">Norrköping</option>
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
                <input type="file" id="image" accept="image/*" @change="handleImageUpload">
            </div>
            <button type="submit" @click="navigateToPay">Gå till betalning</button>
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
    submitForm() {
      console.log('Formulärdata:', this.name, this.image);
    },
    addItem() {
      const data = {
      "category": this.category,
      "title": this.title,
      "description": this.description,
      "price": this.price,
      "condition": this.condition,
      "seller_id": 1
    };
      axios.post('http://localhost:5000/items', data)
        .then(response => {
          console.log('Svar från server:', response);
          this.navigateToHome();
        })
        .catch(error => {
          console.error('Fel vid kommunikation med server:', error);
        });
    },
    handleImageUpload(event) {
      const file = event.target.files[0];
      this.image = file;
    },
    navigateToHome() {
      this.$router.push('/');
    },
    navigateToPay() {
      this.$router.push('/payment');
    }

  }
  };
  </script>

<style scoped>
.page {
    padding: 60px;
    min-height: 100vh;
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