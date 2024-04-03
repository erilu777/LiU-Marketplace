<template>
    <div class="page">
      <h1>{{ pageTitle }}</h1>
      <p>Det här är ett kandidatarbete på Linköpings Universitet. Vi är 7 studenter på I-sektionen med teknisk inriktning Datateknik.</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        pageTitle: 'Om Oss',
      };
    }
  };
  </script>
  
  <style scoped>

  h1 {
    font-weight: bold;
    font-size: 60px;
    color: #0c264d;
    padding-bottom: 40px;
  }
  </style>
  