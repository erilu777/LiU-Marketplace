<template>
    <div class="page">
        <h1>LiU Marketplace</h1>
        <div class="container">
            <h3>Logga in</h3>
            <button>Logga in med SSO via LiU</button>
        </div>
          <input type="text" v-model="username" placeholder="Användarnamn">
          <input type="password" v-model="password" placeholder="Lösenord">
          <button @click="login">Logga in</button>
          <div>
            <img src="../assets/LMlogo.png" alt="LMlogo">
          </div>
        
    </div>
</template>
  
  <script>
  export default{
    name: 'LoginPage',
    layout: 'LoginLayout'
  }
  </script>
  
  <style scoped>
  .page {
    padding: 20px;
    min-height: 100vh;
    background-color: #0c264d; 
  }

  h1 {
    font-size:70px;
    margin-top: 60px;
    color: white;
    font-weight: bold;
  }

  h3 {
    font-weight: bold;
    color: #0c264d;
  }

  .container {
    background-color: #e7f2f7;
    border: 3px solid #bbd5e9;
    border-radius: 20px;
    width: 350px;
    margin: 0 auto;
    padding: 50px;
    margin-top: 60px;
    height: 250px;
  }

  button {
    margin-top: 40px;
  }

  img {
    max-width: 100px;
    margin-top: 40px;
  }

  </style>
  