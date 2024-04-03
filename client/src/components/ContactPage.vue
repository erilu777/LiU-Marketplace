<template>
    <div class="page">
      <h1>Kontakta Oss</h1>
      <div class="container">
        <form @submit.prevent="submitForm">
            <div class="row">
                <input type="text" id="name" v-model="name" placeholder="Namn" class="ctrph">
            </div>
            <div class="row">
                <input type="email" id="email" v-model="email" placeholder="Email" class="ctrph">
            </div>
            <div class="row">
                <textarea id="description" v-model="description" placeholder="Din Fråga" class="ctrph"></textarea>
            </div>
            <button type="submit">Skicka</button>
        </form>
      </div>
    </div>
</template>

<script>
  export default {
  data() {
    return {
      buttonText: '',
      area: '',
      condition: ''
    };
  },
  watch: {
    '$route.params.buttonText': function(newButtonText) {
    this.buttonText = newButtonText;
    }
  },
  methods: {
    submitForm() {
      console.log('Formulärdata:', this.name, this.image);
    },
    handleImageUpload(event) {
      const file = event.target.files[0];
      this.image = file;
    }
  }
};

  </script>

<style scoped>
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
    width: 500px;
    margin: 0 auto;
    padding: 30px;
  }

  .row {
    padding: 10px;
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
    margin-top: 20px;
  }

  .ctrph::placeholder {
    text-align: center; 
  }
</style>