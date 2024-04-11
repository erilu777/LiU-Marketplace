<template>
    <div class="page">
      <h1>Du lämnar nu LiU Marketplace</h1>
      <p>Hoppas vi ses snart igen!</p>
      <button @click="logout">Logga ut</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        pageTitle: 'Logout Page',
      };
    },
    methods: {
      logout() {
        sessionStorage.removeItem('auth');
        this.$router.push('/login');
      }
    }
  };
  </script>
  
  <style scoped>
  .page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    min-height: 100vh;
  }

  button {
    display: flex;
    align-items: center;
    background-color: #0c264d;
    padding: 10px;
    height: 40px;
    border-radius: 20px;
    color: white;
    margin-bottom: 10px;
    text-decoration: none;
  }
  </style>
  