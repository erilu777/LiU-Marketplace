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
        { question: "Hur fungerar betalningen?", answer: "Du kontaktar säljaren och kommer överens om hur köpet ska ske. Betalningsmetoden kan variera beroende på överenskommelsen mellan köpare och säljare. Vanliga betalningsalternativ inkluderar kontant betalning vid mötet för att överlämna varan, eller användning av betalningsplattformar som Swish eller PayPal för att överföra pengar elektroniskt. När köpet är gjort går säljaren in på varan och markerar som såld och fyller i köparens LiU-ID som sedan hittar annonsen under Mina Köp." },
        { question: "Kan jag kontakta säljaren för att ställa frågor om produkten innan jag köper den?", answer: "Ja, du kan  kontakta säljaren genom att trycka på 'Kontakta säljaren' på den annons du är intresserad av för att ställa frågor eller begära mer information om produkten innan du genomför köpet via e-post. Det är en bra idé att klargöra eventuella tvivel eller frågor innan du fattar ett köpbeslut." },
      ],
      faqs2: [
        { question: "Hur lägger jag upp en vara för försäljning?", answer: "För att lägga upp en annons, välj alternativet 'Sälja' för att skapa en ny annons. Välj först kategori och fyll sedan i information om produkten, inklusive titel, beskrivning, pris, område, skick och bilder. När du är nöjd klickar du på 'Gå till betalning'. Efter betalningen är gjord görs annonsen synlig för andra användare." },
        { question: "Kan jag ändra eller ta bort min annons efter att den har publicerats?", answer: "Ja, du kan redigera eller ta bort din annons när som helst genom att gå till ditt användarkonto och välja alternativet för att hantera dina annonser. Här kan du uppdatera informationen, ändra priset eller helt enkelt ta bort annonsen om produkten har sålts eller om du inte längre vill sälja den." },
        { question: "Finns det några avgifter för att sälja på plattformen?", answer: "Det finns en uppsättningsavgift på 10kr för att lägga upp en annons. Denna avgift tas ut för att täcka administrativa avgifter samt säkerställa seriösa annonser." },
        { question: "Finns det några riktlinjer för att skapa en effektiv annons?", answer: "Ja, det finns några tips som kan hjälpa till att göra din annons mer lockande och informativ. Inkludera tydliga och detaljerade beskrivningar av produkten, använd högkvalitativa bilder, ange priset tydligt och var ärlig om produktskick och eventuella defekter. Ju mer information du kan ge, desto större chans är det att locka intresserade köpare."}
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
  white-space: normal;
  text-align: left;
}
</style>
