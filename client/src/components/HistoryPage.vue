<template>
    <div class="page">
        <router-link to="/profile" v-slot="{ navigate }">
            <button class="ToProfile" @click="navigate">Till din profil</button>
        </router-link>
        <h1>Min köphistorik</h1>
        <h4>Nuvarande annonser</h4>
        <div class="container" ref="container" @scroll="checkScroll">
            <div class="ads-container">
                <div v-for="(ad, index) in availableAds" :key="index" class="ad-box" @mouseover="showButtons(index)" @mouseleave="hideButtons(index)">
                    <!-- Visa annonsens innehåll här -->
                    <p>{{ ad.title }}</p>
                    <img :src="ad.images[0].image_path" alt="Ad Image" class="ad-image" />
                    <div class="buttons" v-show="ad.showButtons">
                      <button class="small-button" @click="editAd(index)">Redigera</button>
                      <button class="small-button" @click="deleteAd(index)">Ta bort</button>
                      <button class="small-button" @click="showModal(index)">Såld</button>
                        <div class="modal" :class="{ 'is-active': isModalActive }">
                          <div class="modal-background" @click="closeModal(index)"></div>
                          <div class="modal-content">
                            <div class="box">
                              <p>Vem har du sålt varan till?</p>
                              <!-- Input för att ange köpare -->
                              <input type="text" v-model="buyer" placeholder="Köparens LiU-id">
                              <!-- Knapp för att bekräfta försäljningen -->
                              <button @click="confirmSale(index)">Bekräfta försäljning</button>
                              <div>
                                <p class="h-button" @click="closeModal(index)">Gå tillbaka</p>
                              </div>
                              
                            </div>
                          </div>
                            
                          </div>
                </div>
            </div>
        </div>
        </div>
        
        <h4>Sålda varor</h4>
        <div class="container" ref="container" @scroll="checkScroll">
            <div class="ads-container">
                <div v-for="(ad, index) in soldAds" :key="index" class="ad-box">
                    <!-- Visa annonsens innehåll här -->
                    <p>{{ ad.title }}</p>
                    <img :src="ad.images[0].image_path" alt="Ad Image" class="ad-image" />
                </div>
            </div>
        </div>
        
        <h4>Köpta varor</h4>
        <div class="container" ref="container" @scroll="checkScroll">
            <div class="ads-container">
                <div v-for="(ad, index) in boughtAds" :key="index" class="ad-box">
                    <!-- Visa annonsens innehåll här -->
                    <p>{{ ad.title }}</p>
                    <img :src="ad.images[0].image_path" alt="Ad Image" class="ad-image" />
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>

    <h4>Sålda varor</h4>
    <div class="container" ref="container" @scroll="checkScroll">
      <div class="ads-container">
        <div v-for="(ad, index) in soldAds" :key="index" class="ad-box">
          <!-- Visa annonsens innehåll här -->
          <p>{{ ad.title }}</p>
          <img :src="ad.images[0].image_path" alt="Ad Image" class="ad-image" />
        </div>
      </div>
    </div>

    <h4>Köpta varor</h4>
    <div class="container" ref="container" @scroll="checkScroll">
      <div class="ads-container">
        <div v-for="(ad, index) in boughtAds" :key="index" class="ad-box">
          <!-- Visa annonsens innehåll här -->
          <p>{{ ad.title }}</p>
          <img :src="ad.images[0].image_path" alt="Ad Image" class="ad-image" />
        </div>
      </div>
    </div>
  </div>


</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      availableAds: [], // Array för att lagra tillgängliga annonser
      soldAds: [], // Array för att lagra sålda annonser
      boughtAds: [], // Array för att lagra köpta annonser
      isLoading: false, // Flagga för att visa om nya annonser laddas
      buyer: this.buyer, // Köparens LiU-id
    };
  },

  methods: {
    async fetchAds() {
      this.isLoading = true;
      try {
        const auth = JSON.parse(sessionStorage.getItem('auth'));
        if (auth) {
          const token = auth.token;

          const availableResponse = await axios.get('/available_items', {
            headers: {
              "Authorization": "Bearer " + token
            },
          });
          this.availableAds = availableResponse.data.map(ad => ({
            ...ad,
            showButtons: false,
          }));

          const soldResponse = await axios.get('/sold_items', {
            headers: {
              "Authorization": "Bearer " + token
            },
          });
          this.soldAds = soldResponse.data;

          const boughtResponse = await axios.get('/bought_items', {
            headers: {
              "Authorization": "Bearer " + token
            },
          });
          this.boughtAds = boughtResponse.data;
        } else {
          console.error('Auth token not found in sessionStorage');
        }
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
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
    },
    showButtons(index) {
      console.log(this.availableAds[index]);  // Add this line
      this.availableAds[index].showButtons = true;
    },
    hideButtons(index) {
      this.availableAds[index].showButtons = false;
    },
    editAd(index) {
      const ad = this.availableAds[index];
      console.log(ad); // Log the ad to the console
      this.$router.push(`/edit-ad/${ad.id}`);
    },
    showModal(index) {
      this.isModalActive = true;
      this.availableAds[index].showButtons = false;
      this.availableAds[index].showButtons = true;
    },
    closeModal(index) {
      this.isModalActive = false;
      this.availableAds[index].showButtons = false;
      this.availableAds[index].showButtons = true;
    },
    deleteAd(index) {
      if (confirm('Är du säker på att du vill ta bort annonsen?')) {
        const ad = this.availableAds[index];
        if (ad && ad.id) {
          // Get the token from the session storage
          const auth = JSON.parse(sessionStorage.getItem('auth'));
          if (auth) {
            const token = auth.token;

            // Send a DELETE request to delete the ad
            axios.delete(`/items/${ad.id}`, {
              headers: {
                "Authorization": "Bearer " + token
              }
            })
              .then(() => {
                console.log('Ad deleted successfully');
                // Remove the ad from the availableAds array
                this.availableAds.splice(index, 1);
              })
              .catch(error => {
                console.error('Error deleting ad:', error);
              });
          } else {
            console.error('Auth token not found in sessionStorage');
          }
        } else {
          console.error('Ad ID not found');
        }
      }

    },
    confirmSale(index) {
      const ad = this.availableAds[index];
      if (ad && ad.id) {
        // Get the token from the session storage
        const auth = JSON.parse(sessionStorage.getItem('auth'));
        if (auth) {
          const token = auth.token;

          console.log('buyer_id:', this.buyer);
          // Send a PUT request to mark the ad as sold
          axios.put(`/items/${ad.id}/sell`, {
            buyer_id: this.buyer,
          }, {
            headers: {
              "Authorization": "Bearer " + token
            }
          })
            .then(() => {
              console.log('Ad marked as sold successfully');
              // Remove the ad from the availableAds array
              this.availableAds.splice(index, 1);
              window.location.reload();
            })
            .catch(error => {
              console.error('Error marking ad as sold:', error);
            });
        } else {
          console.error('Auth token not found in sessionStorage');
        }
      } else {
        console.error('Ad ID not found');
      }
    },
  },


  mounted() {
    // Hämta initiala annonser när komponenten laddas
    this.fetchAds();
  },

};
</script>

<style>
.page {
  padding: 60px;
  margin: 0 auto;
}

h1,
h4 {
  font-weight: bold;
  color: black;
  margin-top: 40px;
}

.h-button:hover {
  cursor: pointer;
}

  .small-button {
    font-size: small;
    padding: 3px;
    margin-left: 2px;
    margin-right: 2px;
    margin-top: 10px;
  }
  
  .ad-box {
    width: 200px; /* Bredden på varje annons */
    min-height: 150px; /* Höjden på varje annons */
    margin-right: 10px; /* Avstånd mellan annonserna */
    background-color: #f0f0f0;
    display: inline-block; /* Håll annonserna i en rad */
    vertical-align: top; /* Justera vertikalt till toppen av containern */
    padding: 10px;
    overflow: hidden;
  }

  .ad-box p {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

.container {
  width: 100%;
  overflow-x: auto;
  /* Tillåt horisontell scrollning */
  white-space: nowrap;
  /* Hindra radbrytning av annonserna */
}

.ads-container {
  margin-bottom: 20px;
  margin-top: 10px;
  display: inline-block;
  /* Håll alla annonser i en rad */
}

button {
  border-color: #bbd5e9;
  padding: 10px;
  border-radius: 20px;
  color: #0c264d;
  margin-left: 10px;
}

.small-button {
  font-size: small;
  padding: 3px;
  margin-left: 2px;
  margin-right: 2px;
  margin-top: 10px;
}

.ad-box {
  width: 200px;
  /* Bredden på varje annons */
  min-height: 150px;
  /* Höjden på varje annons */
  margin-right: 10px;
  /* Avstånd mellan annonserna */
  background-color: #f0f0f0;
  display: inline-block;
  /* Håll annonserna i en rad */
  vertical-align: top;
  /* Justera vertikalt till toppen av containern */
  padding: 10px;
}

.ad-box:hover .buttons {
  display: block;
  /* Visa knapparna när annonsen är hovrad */
}

.ToProfile {
  margin-top: 0;
}

.ad-image {
  width: 200px;
  height: 200px;
  padding: 10px;
  align-items: center;
  max-width: 100%;
  margin-top: 10px;
  object-fit: cover;
}

.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal.is-active {
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
}

.profile-button {
  margin-top: 10px; 
}
</style>