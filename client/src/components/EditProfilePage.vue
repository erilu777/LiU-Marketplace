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
        <h4>email@email.com</h4>
      </div>
      <form @submit.prevent="editProfile">
        <div class="row">
          <input type="text" id="education" v-model="education" placeholder="Utbildning">
        </div>
        <div class="row">
          <input type="text" id="grade" v-model="grade" placeholder="Årskurs">
        </div>
        <div class="row">
          <button class="submit">Spara</button>
        </div>
      </form>
    </div>
  </div>

</template>

<script>
import  axios  from 'axios';

export default {
  data() {
    return {
      pageTitle: 'Profile Page',
      category: '',
      area: '',
      condition: ''
    };
  },
  methods: {

    editProfile() {
      const token = JSON.parse(sessionStorage.getItem('auth')).token; // Hämta token från sessionStorage
      console.log('Token:', token);
      const userId = JSON.parse(sessionStorage.getItem('auth')).user.id;
      const data = {
        "category": this.category,
        "area": this.area,
        "condition": this.condition
      };
      axios.put('/users/' + userId, data, {
        headers: {
          "Authorization": "Bearer " + token
        }
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