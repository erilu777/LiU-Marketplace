<template>
  <div class="row">
    <div class="profile-container">
      <div class="row">
        <div class="profile-pic-container">
          <img :src="imagePreview || image_path || defaultImage" alt="LMlogo" class="profile-pic">
        </div> 
      </div>
      <div class="row">
        <label for="image" class="file-input-label">Ändra profilbild</label>
        <input type="file" id="image" accept="image/*" @change="handleImageUpload" style="display: none;">
      </div>
      <div class="row">
        <h1 v-if="name">{{ name }}</h1>
        <h1 v-else>Förnamn Efternamn</h1>
      </div>
      <div class="row">
        <h4>{{ email }}</h4>
      </div>
      <form @submit.prevent="editProfile">
        <div class="row">
          <input type="text" id="name" v-model="name" required placeholder="Namn">
        </div>
        <div class="row">
          <input type="text" id="program" v-model="program" required placeholder="Utbildning">
        </div>
        <div class="row">
          <select id="year" required v-model="year">
            <option value="" disabled selected>Årskurs</option>
            <option value=1>1</option>
            <option value=2>2</option>
            <option value=3>3</option>
            <option value=4>4</option>
            <option value=5>5</option>
          </select>
        </div>
        <div class="row">
          <button class="submit-button">Spara</button>
          <button class="cancel-button" @click="navigateToProfile">Avbryt</button>
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
      name: JSON.parse(sessionStorage.getItem('auth')).user.name,
      email: JSON.parse(sessionStorage.getItem('auth')).user.email,
      image_path: JSON.parse(sessionStorage.getItem('auth')).user.image_path,
      previewImage: null,
      defaultImage: require('@/assets/profile.png'),
      user_id: '',
      };
  },
  created() {
    this.fetchProfileData();
  },

  methods: {

    async fetchProfileData() {
      const token = JSON.parse(sessionStorage.getItem('auth')).token;
      const response = await axios.get('/current_user', {
        headers: {
          "Authorization": "Bearer " + token
        }
      });
      this.program = response.data.program;
      this.year = response.data.year;
      this.name = response.data.name;
      this.email = response.data.email;
      this.image_path = response.data.image_path;
      this.user_id = response.data.id;
    },

    editProfile() {

      const formData = new FormData();
      formData.append('program', this.program);
      formData.append('year', this.year);
      formData.append('name', this.name);
      formData.append('image', this.image);

      const token = JSON.parse(sessionStorage.getItem('auth')).token; 
      
      console.log("User ID IN EDIT PROFILE: " + this.user_id);

      axios.put('/users/' + this.user_id, formData, {
        headers: {
          "Authorization": "Bearer " + token,
          'Content-Type': 'multipart/form-data' 
          }
        })
        .then(() => {
          this.$router.push('/profile').then(() => window.location.reload());  //Fullösning för att uppdatera sidan
        })
    },
    handleImageUpload(event) {
      console.log('Image uploaded');
      this.image = event.target.files[0];
      this.imagePreview = URL.createObjectURL(this.image);
      this.$forceUpdate(); // Force update to show the image preview
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

.cancel-button {
  background-color: gainsboro;
  color: black;
}

.submit-button {
  background-color: #0c264d;
  color: white;
  margin-bottom: 10px;
  margin-top: 10px;
}

h1 {
  font-weight: bold;
  color: #0c264d;
}

h4 {
  color: #0c264d;
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
  justify-content: center;
  margin-bottom: 5px;
  align-items: center;
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
.profile-pic {
  width: 200px;
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  border-radius: 50%; /* Makes the image round */
  object-fit: cover; /* Prevents image from stretching */
  border: 2px solid #0c264d;
}

</style>