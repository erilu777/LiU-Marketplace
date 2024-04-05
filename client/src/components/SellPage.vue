<template>
    <div class="page">
      <h1>{{ pageTitle }}</h1>
      <div class="button-containter">
        <div class="row">
            <button @click="navigateToPage(category1)">{{ category1 }}</button>
            <button @click="navigateToPage(category2)">{{ category2 }}</button>
        </div>
        <div class="row">
            <button @click="navigateToPage(category3)">{{ category3 }}</button>
            <button @click="navigateToPage(category4)">{{ category4 }}</button>
        </div>
        <div class="row">
            <button @click="navigateToPage(category5)">{{ category5 }}</button>
            <button @click="navigateToPage(category6)">{{ category6 }}</button>
        </div>
        <div class="row">
            <button class="center-button" @click="navigateToPage(category7)">{{ category7 }}</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        pageTitle: 'Vad vill du sälja?',
        category1: "Cykel",
        category2: "Bok",
        category3: "Biljett",
        category4: "Inredning",
        category5: "Bostad",
        category6: "Verktyg",
        category7: "Övrigt",
      };
    },
    methods: {
    navigateToPage(category) {
        console.log(category)
        this.$router.push({ name: 'newad', params: { category: category } });
    }
  }
  };
  </script>
  
  <style scoped>
  .page {
    padding: 60px;
    min-height: 100vh;
    width: 45%;
    margin: 0 auto;
  }

  h1 {
    font-weight: bold;
    font-size: 60px;
    color: #0c264d;
    padding-bottom: 40px;
  }
  
  .button-container {
    display: flex;
    flex-direction: column;
  }

  .row {
    display: flex;
    justify-content: space-between;
    
  }

  button {
    background-color: #e7f2f7;
    border-color: #bbd5e9;
    padding: 10px;
    width: 47%;
    height: 60px;
    border-radius: 20px;
    min-width: 180px;
    margin-bottom: 20px;
  }

  .center-button {
    margin: 0 auto;
  }

  </style>
  