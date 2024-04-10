<template>
  <div class="row">
    <div class="profile-container">
      <div class="row">
        <img src="../assets/profile.png" alt="LMlogo">
      </div>
      <div class="row">
        <label for="image" class="file-input-label">Ändra profilbild</label>
        <input type="file" id="image" accept="image/*" @change="handleImageUpload" style="display: none;">
      </div>
      <div class="row">
        <h1>Förnamn Efternam</h1>
      </div>
      <div class="row">
        <h4>{{ Liu_ID }}@email.com</h4>
      </div>
      <form @submit.prevent="editProfile">
        <div class="row">
          <input type="text" id="education" v-model="education" placeholder="Utbildning">
        </div>
        <div class="row">
          <select id="year" v-model="year">
            <option value="" disabled selected>Årskurs</option>
            <option value= 1 >1</option>
            <option value= 2 >2</option>
            <option value= 3 >3</option>
            <option value= 4 >4</option>
            <option value= 5 >5</option>
          </select>        </div>
        <div class="row">
          <button class="submit">Spara</button>
        </div>
      </form>
    </div>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      pageTitle: 'Profile Page',
      program: '',
      year: '',
      Liu_ID: JSON.parse(sessionStorage.getItem('auth')).user.liu_id
    };
  },
  methods: {

    editProfile() {
      const auth = JSON.parse(sessionStorage.getItem('auth'));
      const token = JSON.parse(sessionStorage.getItem('auth')).token; // Hämta token från sessionStorage
      console.log('Token:', token);
      const userId = JSON.parse(sessionStorage.getItem('auth')).user.id;
      const data = {
        "program": this.education,
         "year": this.year,
      };
      axios.put('/users/' + userId, data, {
        headers: {
          "Authorization": "Bearer " + token
        }
      })
        .then(response => {
          // Update sessionStorage with the new data
          auth.user = response.data;
          sessionStorage.setItem('auth', JSON.stringify(auth));
          this.$router.push('/profile');
        })
      this.$router.push('/profile');
    },

    navigateToProfile() {
      this.$router.push('/profile');
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
  color: black;
}

h4 {
  color: black;
}

img {
  max-width: 300px;
  margin: 0 auto;
}

.profile-container {
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

.save-button {
  display: flex;
  align-items: center;
  background-color: #0c264d;
  padding: 10px;
  height: 40px;
  border-radius: 20px;
  color: white;
  margin-bottom: 60px;
  text-decoration: none;
}

.file-input-label {
  color: #0c264d;
  border-color: #0c264d;
  padding: 10px;
  border-radius: 20px;
  cursor: pointer;
  border: 2px solid;
}
</style>