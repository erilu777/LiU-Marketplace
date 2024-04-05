<template>
    <div class="page">
      <h1>Försäljning av {{ category }}</h1>
      <div class="container">
        <form @submit.prevent="submitForm">
            <div class="row">
                <input type="text" id="titel" v-model="titel" placeholder="Titel" class="ctrph">
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
                    <option value="new">Nytt</option>
                    <option value="usednew">Använd - nyskick</option>
                    <option value="usedok">Använd - gott skick</option>
                    <option value="used">Använd - använt skick</option>
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
    handleImageUpload(event) {
      const file = event.target.files[0];
      this.image = file;
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