<template>
    <div class="page">
        <div class="row">
            <div class="profile-container">
                <div class="row">
                    <img src="../assets/profile.png" alt="LMlogo">
                </div>
                <div class="row">
                    <h1>Förnamn Efternam</h1>
                </div>
                <div class="row">
                    <h4>email@email.com</h4>
                </div>
                <div class="row">
                    <h4>Utbildning</h4>
                </div>
                <div class="row">
                    <h4>Årskurs #</h4>
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
  export default {
    data() {
      return {
        pageTitle: 'Profile Page',
      };
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
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 5px;
  }

  .edit-button {
    display: flex;
    align-items: center;
    background-color: #0c264d;
    padding: 10px;
    height: 40px;
    color: white;
    margin-bottom: 10px;
    text-decoration: none;
  }

  .h-button {
    display: flex;
    align-items: center;
    padding: 10px;
    height: 40px;
    border-radius: 20px;
    color: #0c264d;
    margin-bottom: 60px;
    text-decoration: none;
  }
  
  </style>
  