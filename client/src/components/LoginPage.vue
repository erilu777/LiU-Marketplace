<template>
  <div class="page">
    <h1>LiU Marketplace</h1>
    <div class="container">
      <h3>Logga in</h3>
      <button @click="loginSSO">Logga in med SSO via LiU</button>
    </div>
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

      <!--<h3>Registrera dig</h3>-->

      <div>
        <img class="img_login" src="../assets/LMlogo.png" alt="LMlogo">
      </div>
      <form @submit.prevent="register">
        <div>
          <label>
            <h3>Liu-ID:</h3>
            <input v-model="new_username" type="text" required placeholder="LiU-ID">
          </label>
        </div>
        <div>
          <label>
            <h3>Lösenord:</h3>
            <input v-model="new_password" type="password" required placeholder="Lösenord">
          </label>
        </div>
        <button type="submit">Submit</button>
      </form>
      <button class="close-button" @click="showModal = false">Close</button>
    </div>
    <div v-if="showModal" class="modal">

      <div>
        <img class="img_login" src="../assets/LMlogo.png" alt="LMlogo">
      </div>
      <form @submit.prevent="register">
        <div>
          <label>
            <h3>Liu-ID:</h3>
            <input v-model="new_username" type="text" required placeholder="LiU-ID">
          </label>
        </div>
        <div>
          <label>
            <h3>Lösenord:</h3>
            <input v-model="new_password" type="password" required placeholder="Lösenord">
          </label>
        </div>
        <button type="submit">Submit</button>
      </form>
      <button class="close-button" @click="showModal = false">Close</button>
    </div>

    <div>
      <img class="img_login" src="../assets/LMlogo.png" alt="LMlogo">
    </div>
  </div>

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

</template>

<script>
import axios from 'axios';
import { PublicClientApplication } from "@azure/msal-browser";

export default {
  name: 'LoginPage',
  layout: 'LoginLayout',

  data() {
    return {
      showModal: false,
      liu_id: '',
      password: '',
      msalConfig: {
        auth: {
          clientId: "a43a60fc-0797-469d-b195-722df39d414a",
          authority: "https://login.microsoftonline.com/913f18ec-7f26-4c5f-a816-784fe9a58edd",
          redirectUri: "http://localhost:8080",
          //redirectUri: "http://127.0.0.1:5000"
        },
        cache: {
          cacheLocation: "sessionStorage", // This configures where your cache will be stored
          storeAuthStateInCookie: false, // If you set this to "true", you must also set "cacheLocation" to "sessionStorage"
        }
      },
      loginRequest: {
        scopes: ["openid", "profile", "User.Read"],
      },
      myMSALObj: null,
    };
  },

  created() {
    this.initializeMSAL();
  },

  methods: {
    async initializeMSAL() {
      this.myMSALObj = await new PublicClientApplication(this.msalConfig);
    },

    loginSSO() {
      console.log('loginSSO method called');
      //const myMSALObj = new PublicClientApplication(this.msalConfig);
      this.myMSALObj.loginPopup(this.loginRequest).then((loginResponse) => {
        // login success
        console.log(loginResponse);
      }).catch((error) => {
        console.error(error);
      });
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
  width: 40%;
  height: 47%;
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
  z-index: 1000;
  position: fixed;
  top: 50%;
  left: 50%;
  width: 40%;
  height: 47%;
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

.copyright {
  font-size: 12px;
  margin-top: 100px;
}
</style>