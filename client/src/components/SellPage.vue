<template>
    <div class="page">
      <h1>{{ pageTitle }}</h1>
      <div class="button-containter">
        <div class="row">
            <button @click="navigateToPage(button1Text)">{{ button1Text }}</button>
            <button @click="navigateToPage(button2Text)">{{ button2Text }}</button>
        </div>
        <div class="row">
            <button @click="navigateToPage(button3Text)">{{ button3Text }}</button>
            <button @click="navigateToPage(button4Text)">{{ button4Text }}</button>
        </div>
        <div class="row">
            <button @click="navigateToPage(button5Text)">{{ button5Text }}</button>
            <button @click="navigateToPage(button6Text)">{{ button6Text }}</button>
        </div>
        <div class="row">
            <button class="center-button" @click="navigateToPage(button7Text)">{{ button7Text }}</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        pageTitle: 'Vad vill du sälja?',
        button1Text: "Cykel",
        button2Text: "Bok",
        button3Text: "Biljett",
        button4Text: "Inredning",
        button5Text: "Bostad",
        button6Text: "Verktyg",
        button7Text: "Övrigt",
      };
    },
    methods: {
    navigateToPage(buttonText) {
        console.log(buttonText)
        this.$router.push({ name: 'newad', param: { newButtonText: buttonText } });
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
    margin-bottom: 20px;
  }

  button {
    background-color: #e7f2f7;
    border-color: #bbd5e9;
    padding: 10px;
    width: 47%;
    height: 60px;
    border-radius: 20px;
  }

  .center-button {
    margin: 0 auto;
  }

  </style>
  