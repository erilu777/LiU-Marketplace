<template>
  <div class="page">
    <div class="row">
      <div class="profile-container">
        <div class="row">
          <div class="profile-pic-container">
            <img :src="user.image_path || defaultImage" alt="LMlogo" class="profile-pic">
          </div>
        </div>
        <div class="row">
          <h1 v-if="user.name">{{ user.name }}</h1>
        </div>
        <div class="row">
          <h4>{{ user.email }}</h4>
        </div>
        <div class="row">
          <h4>{{ user.program }}</h4>
        </div>
        <div class="row">
          <h4>Årskurs {{ user.year }}</h4>
        </div>
        <div class="row">
          <button class="edit-button" @click="navigateToEdit">Redigera profil</button>
        </div>
        <div class="row">
          <button class="h-button" @click="navigateToHistory">Visa nuvarande annonser och historik</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {
        //real_name: JSON.parse(sessionStorage.getItem('auth')).user.name,
        firstName: '',
        lastName: '',
        email: '',
        program: '',
        year: '',
      },
      defaultImage: require('@/assets/profile.png'),
    };
  },

  async created() {
    const token = JSON.parse(sessionStorage.getItem('auth')).token;
    const response = await axios.get('/current_user', {
      headers: {
        "Authorization": "Bearer " + token
      },
    });
    this.user = response.data;
  },

  methods: {
    navigateToEdit() {
      this.$router.push('/edit-profile');
    },
    navigateToHistory() {
      this.$router.push('/profile-history');
    }
  }
};
</script>

<style scoped>
.page {
  min-height: 80vh;
  margin: 0 auto;
}

h2 {
  font-weight: bold;
  color: #0c264d;
}

h4 {
  color: #0c264d;
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

.profile-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.row {
  display: flex;
  justify-content: center;
  margin-bottom: 5px;
}

.edit-button {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #0c264d;
  padding: 10px;
  height: 40px;
  color: white;
  margin-bottom: 7px;
  margin-top: 7px;
  text-decoration: none;
}

.h-button {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
  height: 40px;
  color: #0c264d;
  text-decoration: none;
}
</style>