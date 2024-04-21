<template>
  <div class="page">
    <h1>LiU Marketplace</h1>
    <div class="container">
      <h3>Logga in</h3>
      <button @click="SSOlogin">Logga in med SSO via LiU</button>
    </div>
    <!--
    <form @submit.prevent="login">
      <input type="text" v-model="username" required placeholder="LiU-ID">
      <input type="password" v-model="password" required placeholder="Lösenord">
      <button type="submit">Logga in</button>
    </form>

    <div>
      <h3>Registrera dig!</h3>
      <button @click="showModal = true">Registrera dig här</button>
    </div>
    
    <div v-if="showModal" class="modal">
      
    <button class="close-buttonX" @click="showModal = false">X</button>
  
      <div>
        <img class="img_login" src="../assets/LMlogo.png" alt="LMlogo">
      </div>
      <form @submit.prevent="register">
        <div>
          <label>
            <h3>LiU-ID:</h3>
            <input v-model="new_username" type="text" required placeholder="LiU-ID">
          </label>
        </div>
        <div>
          <label>
            <h3>Lösenord:</h3>
            <input v-model="new_password" type="password" required placeholder="Lösenord">
          </label>
        </div>
        
        <div class="terms">
          <input type="checkbox" id="terms" v-model="acceptedTerms">
          <label for="terms">I accept the <a href="#" @click.prevent="showTerms">terms and conditions</a></label>
        </div>

        <button type="submit">Submit</button>
      </form>

      <div v-if="showTermsModal" class="TermModal">
        <h2>Användarvillkor</h2>
        <div class="terms-container">

          <pre>
    Villkor för LiU Marketplace<br/><br/>

    Genom att registrera dig på LiU Marketplace godkänner 
    du följande villkor:<br/><br/>

    §1.<br/> LiU Marketplace är inte säljare av annonserade produkter
     utan agerar endast som förmedlare av annonser. 
    LiU Marketplace ansvarar därmed inte för eventuella 
    problem med produkter som köps via plattformen.<br/><br/>

    §2.<br/> All data hanteras inom EU i enlighet med GDPR. 
    LiU Marketplace åtar sig att skydda dina personuppgifter och
     behandla dem konfidentiellt.<br/><br/>

    §3.<br/> Ditt LiU-ID och namn är redan offentliga handlingar inom 
    Linköpings universitet och kommer därmed att vara synliga för
     andra användare på LiU Marketplace.<br/><br/>

    §4.<br/> Som användare är du ansvarig för att följa svensk lag och
     LiU Marketplaces användarvillkor när du lägger upp annonser
      och interagerar med andra användare.<br/><br/>

    §5.<br/> LiU Marketplace förbehåller sig rätten att ta bort annonser
     och stänga av användare som godtyckligt bedöms handla i icke 
     god tro, eller svensk lag.<br/><br/>

    §6.<br/> Tvister mellan köpare och säljare ska i första hand lösas mellan 
    parterna. LiU Marketplace ansvarar inte för att medla i sådana 
    tvister.<br/><br/>

    §7.<br/> LiU Marketplace ansvarar inte för eventuella förluster eller skador
     som uppstår till följd av användning av plattformen.<br/><br/>

    §8.<br/> Genom att använda LiU Marketplace samtycker du till att 
    LiU Marketplace skickar dig nödvändig information via e-post.<br/><br/>

    §9.<br/> LiU Marketplace förbehåller sig rätten att ändra dessa villkor. 
    Vid väsentliga ändringar kommer du att meddelas via e-post.<br/><br/>
</pre>

        </div>
        <button @click="showTermsModal = false">Close</button>
      </div>
    </div>
-->
    <!-- Footer -->
    <div class="footer-line"></div>
    <footer class="footer">
      <div class="column">
        <h3 class="h3_footer"><strong>Mer info</strong></h3>
        <ul>
          <p><a href="mailto:liu@marketplace.com" target="_blank">liu@marketplace.com</a></p>
          <p><a href="tel:+46123456789" target="_blank">+46 123 45 67 89</a></p>
        </ul>
      </div>
      <div class="column">
        <h3 class="h3_footer"><strong>LiU Marketplace</strong></h3>
        <p>For Students - By Students</p>
        <p class="copyright">© LiU Marketplace 2024</p>
      </div>
      <div class="column">
        <img src="../assets/LMlogo.png" alt="LMlogo">
      </div>
    </footer>
  </div>
</template>

<script>
import axios from 'axios';
import termsText from 'raw-loader!../assets/Villkor.txt';

export default {
  name: 'LoginPage',
  layout: 'LoginLayout',

  data() {
    return {
      acceptedTerms: false,
      showTermsModal: false,
      termsText: '',
      showModal: false,
      liu_id: '',
      password: '',
      loginRequest: {
        scopes: ["openid", "profile", "User.Read"],
      },
    };
  },

  created() {
  },
  mounted() {
    console.log("mounted");
    const urlParams = new URLSearchParams(window.location.search);
    const accessToken = urlParams.get('access_token');
    const user = urlParams.get('user');
    if (accessToken) { 
        console.log("access token: " + accessToken);  
        console.log("user: " + user);
        sessionStorage.setItem('auth' , JSON.stringify({access_token: accessToken, user: user}));
        this.$emit('login-success');
        alert("Inloggad.");
        this.$router.push('/home').then(() => window.location.reload());  //Fullösning för att uppdatera sidan
    }
  },
  methods: {
    showTerms() {
      this.showTermsModal = true;
      this.termsText = termsText;
    },
    SSOlogin() {
      console.log("inshallah SSO");
      window.location.href = "http://localhost:8080/ssologin";   

      const accessToken = this.$cookies.get('access_token');
      console.log(accessToken);
    },
    async login() {
      try {
        const response = await axios.post("/login", {
          liu_id: this.username,
          password: this.password
        }, {
          withCredentials: true
        });
        if (response.status >= 200 && response.status < 300) {
          sessionStorage.setItem('auth', JSON.stringify(response.data));
          sessionStorage.setItem('is_admin', response.data.is_admin);
          this.$emit('login-success');
          alert("Inloggad.");
          console.log(response.data);
          this.$router.push('/').then(() => window.location.reload());  //Fullösning för att uppdatera sidan    
        }
      } catch (error) {
        if (error.response.status == 401) {
          alert("Fel LiU-ID eller lösenord.");
        } else {
          console.error(error);
        }
      }
    },

    async register() {
      try {
        if (!this.acceptedTerms) {
          alert('You must accept the terms and conditions to register.');
          return;
        }
        const signupResponse = await axios.post("/sign-up", {
          liu_id: this.new_username,
          password: this.new_password
        }, {
          withCredentials: true
        });
        if (signupResponse.status >= 200 && signupResponse.status < 300) {
          const loginResponse = await axios.post("/login", {
            liu_id: this.new_username,
            password: this.new_password
          }, {
            withCredentials: true
          });
          if (loginResponse.data) {
            sessionStorage.setItem('auth', JSON.stringify(loginResponse.data));
            sessionStorage.setItem('is_admin', loginResponse.data.is_admin);
            this.$emit('login-success');
            this.$router.push('/edit-profile');
            alert("Registrerad och inloggad.");
            console.log(loginResponse.data);
          }
        }
      } catch (error) {
        if (error.response.status == 400) {
          alert("LiU_ID upptaget.");
        } else {
          console.error(error);
        }
      }
    },
  },
};
</script>

<style scoped>
.page {
  padding: 20px;
  min-height: 100vh;
  background-color: #0c264d;
  font-family: Arial, sans-serif;
}

h1 {
  font-size: 70px;
  margin-top: 60px;
  color: white;
  font-weight: bold;
}
.terms-container pre {
  font-family: inherit; /* This will make the font the same as the parent element */
}
h3 {
  font-weight: bold;
  color: #0c264d;
}

.container {
  background-color: #e7f2f7;
  border: 3px solid #bbd5e9;
  border-radius: 20px;
  width: 350px;
  margin: 0 auto;
  padding: 50px;
  margin-top: 60px;
  height: 250px;
}

button {
  margin-top: 40px;
}

.img_login {
  max-width: 100px;
  margin-top: 40px;
}

.modal {
  z-index: 1000;
  position: fixed;
  top: 50%;
  left: 50%;
  width: 50%;
  height: 55%;
  padding: 20px;
  transform: translate(-50%, -50%);
  display: flex;
  justify-content: center;
  border: 1px solid black;
  align-items: flex-start;
  background-color: white;
  border-radius: 10px;
}

.close-button {
  margin-top: 60px;
}

.img_login {
  width: 100%;
  height: auto;
  margin: 20px;
  margin-top: 40px;
}

/* Footer styles */
.footer-line {
  height: 2px;
  background-color: white;
  width: 100%;
}

.footer {
  display: flex;
  justify-content: center;
  background-color: #0c264d;
  height: 300px;
  padding: 60px;
  text-align: center;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-weight: normal;
}

.column {
  width: 30%;
}

.column ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

p {
  color: white;
}

.h3_footer {
  color: white;
  font-weight: normal;
}

.footer a {
  color: white;
  /* White text color for menu items */
  text-decoration: none;
  /* Remove underline */
}

.column img {
  max-width: 150px;
}

.menu-bar img {
  max-width: 50px;
  margin-right: 10px;
}

.modal {
  z-index: 900;
  position: fixed;
  top: 50%;
  left: 50%;
  width: 50%;
  height: 55%;
  padding: 20px;
  transform: translate(-50%, -50%);
  display: flex;
  justify-content: center;
  border: 1px solid black;
  align-items: flex-start;
  background-color: white;
  border-radius: 10px;
}

.TermModal {
  z-index: 1000;
  position: fixed;
  top: 50%;
  left: 50%;
  width: 110%;
  height: 100%;
  padding: 20px;
  transform: translate(-50%, -50%);
  border: 1px solid black;
  background-color: white;
  border-radius: 10px;
  overflow: auto;
}



.img_login {
  width: 100%;
  height: auto;
  margin: 20px;
  margin-top: 40px;
}

.terms-container {
  max-width: 100%;
  /* Adjust as needed */
  margin: 0 auto;
  word-wrap: break-word;
  /* Add this line */
}

.copyright {
  font-size: 12px;
  margin-top: 100px;
}

.close-container {
  position: relative;
}

.modal {
  position: relative;
  /* other styles */
}

.close-buttonX {
  position: absolute;
  top: -50px; /* adjust as needed */
  right: 0px; /* adjust as needed */
  background: none;
  border: none;
  font-size: 1.5em;
}
</style>