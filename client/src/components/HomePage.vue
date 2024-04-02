<template>
    <div class="page">
      <h1>{{ pageTitle }}</h1>
      <p>This is the Home Page content.</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        pageTitle: 'Home Page',
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
  