<template>
    <div class="page">
        <router-link to="/profile" v-slot="{ navigate }">
            <button @click="navigate">Tillbaka till min profil</button>
        </router-link>
        <h1>Min köphistorik</h1>
        <h4>Nuvarande annonser</h4>
        <div class="container" ref="container" @scroll="checkScroll">
            <div class="ads-container">
                <div v-for="(ad, index) in ads" :key="index" class="ad-box">
                    <!-- Visa annonsens innehåll här -->
                    <p>{{ ad.title }}</p>
                    <p>{{ ad.description }}</p>
                </div>
            </div>
        </div>
        <h4>Sålda varor</h4>
        <div class="container" ref="container" @scroll="checkScroll">
            <div class="ads-container">
                <div v-for="(ad, index) in ads" :key="index" class="ad-box">
                    <!-- Visa annonsens innehåll här -->
                    <p>{{ ad.title }}</p>
                    <p>{{ ad.description }}</p>
                </div>
            </div>
        </div>
        <h4>Köpta varor</h4>
        <div class="container" ref="container" @scroll="checkScroll">
            <div class="ads-container">
                <div v-for="(ad, index) in ads" :key="index" class="ad-box">
                    <!-- Visa annonsens innehåll här -->
                    <p>{{ ad.title }}</p>
                    <p>{{ ad.description }}</p>
                </div>
            </div>
        </div>
    </div>
    
  </template>
  
  <script>
  export default {
    data() {
      return {
        ads: [], // Array för att lagra annonser
        isLoading: false // Flagga för att visa om nya annonser laddas
      };
    },
    mounted() {
      // Hämta initiala annonser när komponenten laddas
      this.fetchAds();
    },
    methods: {
      fetchAds() {
        // Här skulle du göra en AJAX-förfrågan för att hämta annonser från din backend
        // Exempelvis:
        // this.isLoading = true;
        // axios.get('/api/ads').then(response => {
        //   this.ads = response.data;
        //   this.isLoading = false;
        // });
        // Då skulle du behöva skapa en backend som svarar med en lista av annonser
        // Jag skapar bara några falska annonser här för exempeländamål:
        for (let i = 0; i < 20; i++) {
          this.ads.push({
            title: `Annons ${i + 1}`,
            description: `Det här är en beskrivning för annons ${i + 1}`
          });
        }
      },
      checkScroll() {
        const container = this.$refs.container;
        // Om användaren har skrollat till botten av container-elementet
        if (
          container.scrollTop + container.clientHeight >= container.scrollHeight &&
          !this.isLoading
        ) {
          // Ladda fler annonser
          this.fetchAds();
        }
      }
    }
  };
  </script>
  
  <style>

  h1,h4 {
    font-weight: bold;
    color: black;
    margin-top: 40px;
  }

  .container {
    width: 100%;
    overflow-x: auto; /* Tillåt horisontell scrollning */
    white-space: nowrap; /* Hindra radbrytning av annonserna */
  }
  
  .ads-container {
    margin-bottom: 20px;
    margin-top: 10px;
    display: inline-block; /* Håll alla annonser i en rad */
  }

  button {
    border-color: #bbd5e9;
    padding: 10px;
    border-radius: 20px;
    color: #0c264d;
    margin-top: 20px;
  }
  
  .ad-box {
    width: 200px; /* Bredden på varje annons */
    height: 150px; /* Höjden på varje annons */
    margin-right: 10px; /* Avstånd mellan annonserna */
    background-color: #f0f0f0;
    display: inline-block; /* Håll annonserna i en rad */
    vertical-align: top; /* Justera vertikalt till toppen av containern */
    padding: 10px;
  }
  </style>
  