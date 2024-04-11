<template>
  <div class="page">
    <h1>LiU Marketplace</h1>
    <div class="container">
      <h3>Logga in</h3>
      <button>Logga in med SSO via LiU</button>
    </div>
    <input type="text" v-model="username" placeholder="LiU-ID">
    <input type="password" v-model="password" placeholder="Lösenord">
    <button @click="login">Logga in</button>
    <div>
      <h3>Registrera dig!</h3>
      <input type="text" v-model="new_username" placeholder="LiU-ID">
      <input type="password" v-model="new_password" placeholder="Lösenord">
      <button @click="register">Registrera dig här</button>
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
        <li><router-link to="/om-oss">Om oss</router-link></li>
        <li><router-link to="/vanliga-fragor">Vanliga Frågor</router-link></li>
        <li><router-link to="/kontakta-oss">Kontakta oss</router-link></li>
      </ul>
    </div>
    <div class="column">
      <h3 class="h3_footer"><strong>LiU Marketplace</strong></h3>
      <p>For Students - By Students</p>
    </div>
    <div class="column">
      <img src="../assets/LMlogo.png" alt="LMlogo">
    </div>
  </footer>

</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',
  layout: 'LoginLayout',

  data() {
    return {
      liu_id: '',
      password: '',
    };
  },

  methods: {
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
        } 
      } catch (error) {
        if (error.response.status == 401 || error.response.status == 400) {
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
        if (signupResponse.data) {
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
        } else {
          alert("Användarnamnet är upptaget.");
          console.log(signupResponse.data);
        }
      } catch (error) {
        console.error(error);
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
  color: white
}

.footer a {
  color: white; /* White text color for menu items */
  text-decoration: none; /* Remove underline */
}

.column img {
  max-width: 150px;
}

.menu-bar img {
  max-width: 50px;
  margin-right: 10px;
}

</style>