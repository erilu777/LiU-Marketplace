<template>
  <div class="app">
    <div class="menu-bar">
      <!-- Update the menu items to use router-link -->
      <router-link to="/">LiU Marketplace</router-link>
      <router-link to="/buy">Köpa</router-link>
      <router-link to="/sell">Sälja</router-link>
      <router-link to="/profile">Min Profil</router-link>
      <router-link to="/logout">Logga Ut</router-link>
    </div>
    <!-- Add router-view to display the current page content -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<style scoped>
.app {
  font-family: Arial, sans-serif;
}

.menu-bar {
  background-color: #0c264d; 
  color: white;
  padding: 10px 20px; 
  height: 60px;
}

.menu-bar a {
  color: white; /* White text color for menu items */
  text-decoration: none; /* Remove underline */
  margin-right: 20px; /* Add margin between menu items */
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-size:larger;
}

.menu-bar a:hover {
  text-decoration: underline; /* Add underline on hover */
}

.content {
  padding: 20px; /* Add padding for content */
}

</style>
