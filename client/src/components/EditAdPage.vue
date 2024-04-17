<template>
  <div class="page">
    <h1>Redigera Annons {{ buttonText }}</h1>
    <p>{{ buttonText }}</p>
    <div class="container">
      <form @submit.prevent="submitForm">
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
            <option value="" disabled>Område</option>
            <option value="linkoping">Linköping</option>
            <option value="norrkoping">Norrköping</option>
          </select>
        </div>
        <div class="row">
          <select id="condition" v-model="condition">
            <option value="" disabled>Skick</option>
            <option value="new">Nytt</option>
            <option value="usednew">Använd - nyskick</option>
            <option value="usedok">Använd - gott skick</option>
            <option value="used">Använd - använt skick</option>
          </select>
        </div>
        <div class="row">
          <input type="file" id="image" accept="image/*" multiple @change="handleImageUpload">
        </div>
        <button type="submit" @click.prevent="submitForm">Publicera ändringar</button>
        <button type="button" @click="cancelForm">Avbryt</button>
      </form>
    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      id: null,
      title: '',
      description: '',
      price: null,
      area: '',
      condition: '',
      image: null,
      buttonText: ''
    };
  },

  created() {
    this.id = this.$route.params.id;
    const auth = JSON.parse(sessionStorage.getItem('auth'));
    if (auth) {
      const token = auth.token;

      axios.get(`/items/${this.id}`, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
        .then(response => {
          // Update the form fields with the item data
          this.title = response.data.title;
          this.description = response.data.description;
          this.price = response.data.price;
          this.area = response.data.area || '';
          this.condition = response.data.condition || '';

          // ... handle the image field ...
        })
        .catch(error => {
          console.error(error);
        });
    } else {
      console.error('Auth token not found in sessionStorage');
    }
  },

  watch: {
    '$route.query.newButtonText': function (newButtonText) {
      this.buttonText = newButtonText;
    },
  },
  methods: {
    submitForm() {
      console.log('Submit form method called');

      // Prepare the form data
      // Prepare the form data
      const itemData = {
        title: this.title,
        description: this.description,
        price: this.price,
        area: this.area,
        condition: this.condition,
        image: this.image
      };

      // Get the token from the session storage
      const auth = JSON.parse(sessionStorage.getItem('auth'));
      if (auth) {
        const token = auth.token;

        // Send a PUT request to update the item
        axios.put(`/items/${this.id}`, itemData, {
          headers: {
            "Authorization": "Bearer " + token
          }
        })
          .then(() => {
            console.log('Item updated successfully');
            this.navigateToHistory();
            // Navigate to another page if needed
          })
          .catch(error => {
            console.error('Error updating item:', error);
          });
      } else {
        console.error('Auth token not found in sessionStorage');
      }
    },
    handleImageUpload(event) {
      this.image = Array.from(event.target.files);
    },
    navigateToHistory() {
      this.$router.push('/profile-history')
    },

    cancelForm() {
      this.$router.push('/profile-history')
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
}

.ctrph::placeholder {
  text-align: center;
}
</style>