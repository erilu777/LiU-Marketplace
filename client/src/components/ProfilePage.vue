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
                    <button @click="navigateToEdit">Ändra Profil</button>
                </div>
            </div>
        <div class="row">
            <div class="ad-containter">
                <div class="row">
                    <h1>Nuvarande Annonser</h1>
                </div>
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
    }
  };
  </script>
  
  <style scoped>
  .page {
    display: flex;
    justify-content: center;
    padding: 20px;
    min-height: 100vh;
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
    margin-top: 50px;
    display: flex;
    flex-direction: column;
  }

  .ad-container {
    margin-top: 50px;
    display: flex;
    flex-direction: column;
  }

  .row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 5px;
  }

  button {
    background-color: #0c264d;
    border-color: #bbd5e9;
    padding: 10px;
    height: 40px;
    width: 30%;
    border-radius: 20px;
    color: white;
    margin: 0 auto;
  }
  
  </style>
  