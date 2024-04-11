<template>
  <div class="page">
      <h1>Vanliga Frågor</h1>
      <div class="container">
          <h3>Frågor om Köp</h3>
          <div v-for="(faq, index) in faqs1" :key="index" class="faq">
            <div class="question" @click="toggleAnswer1(index)">
              <span>{{ faq.question }}</span>
              <span v-if="!faq.open" class="toggle-icon">></span>
              <span v-else class="toggle-icon">^</span>
            </div>
          <div v-if="faq.open" class="answer">{{ faq.answer }}</div>
          </div>
      </div>
      <div class="container">
          <h3>Frågor om Försäljning</h3>
          <div v-for="(faq, index) in faqs2" :key="index" class="faq">
            <div class="question" @click="toggleAnswer2(index)">
              <span>{{ faq.question }}</span>
              <span v-if="!faq.open" class="toggle-icon">></span>
              <span v-else class="toggle-icon">^</span>
            </div>
          <div v-if="faq.open" class="answer">{{ faq.answer }}</div>
          </div>
      </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      faqs1: [
        { question: "Är det säkert att handla på LIU Marketplace?", answer: "Ja, vår marknadsplats implementerar Single Sign-On (SSO) för att förstärka säkerhetsnivån. SSO möjliggör en säker och bekväm inloggning, vilket innebär att ditt användarkonto skyddas med en stark autentisering." },
        { question: "Hur fungerar betalningen?", answer: "Svar på fråga 2." },
        { question: "Fråga 3?", answer: "Svar på fråga 3." },
      ],
      faqs2: [
        { question: "Hur lägger jag upp en vara för försäljning?", answer: "Klicka på sälj." },
        { question: "Fråga 2?", answer: "Svar på fråga 2." },
        { question: "Fråga 3?", answer: "Svar på fråga 3." },
      ]
    };
  },
  methods: {
    toggleAnswer1(index) {
      this.faqs1[index].open = !this.faqs1[index].open;
    },
    toggleAnswer2(index) {
      this.faqs2[index].open = !this.faqs2[index].open;
    }
  }
};
</script>

<style scoped>
.page {
  padding: 60px;
  min-height: 100vh;
  margin: 0 auto;
}

h1 {
  font-weight: bold;
  font-size: 60px;
  color: #0c264d;
  margin-bottom: 60px;
}

h3 {
  font-weight: bold;
  margin-bottom: 20px;
}

.container {
  overflow-x: hidden;
  background-color: #e7f2f7;
  border: 3px solid #bbd5e9;
  border-radius: 20px;
  width: 100%;
  max-width: 700px;
  margin: 0 auto;
  padding: 30px;
  margin-bottom: 30px;
}

.question {
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  font-weight: bold;
  margin-top: 20px;
}

.toggle-icon {
  font-size: 20px;
}

.answer {
  margin-left: 20px;
  overflow-y: auto;
  padding-bottom: 15px;
}
</style>
