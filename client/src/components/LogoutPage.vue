<template>
    <div class="page">
      <h1>{{ pageTitle }}</h1>
      <p>This is the Logout Page content. (behövs väl egentligen inte)</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        pageTitle: 'Logout Page',
      };
    }
  };
  </script>
  
  <style scoped>
  .page {
    padding: 20px;
    min-height: 100vh;
  }
  </style>
  