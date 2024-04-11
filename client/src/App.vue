<template>
  <div id="app">
    <LoginPage v-if="!isLoggedIn" @login-success="handleLoginSuccess" />
    <HelloWorld v-else msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import LoginPage from './components/LoginPage.vue';
import { checkLoginStatus } from './components/checkAuth';

export default {
  data() {
    return {
      isLoggedIn: false
    };
  },
  created() {
    this.isLoggedIn = checkLoginStatus();
  },
  methods: {
    handleLoginSuccess() {
      this.isLoggedIn = true;
    }
  },
  components: {
    LoginPage,
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>