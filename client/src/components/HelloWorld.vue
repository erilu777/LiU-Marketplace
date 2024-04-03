<template>
  <div class="app">
    <div class="menu-bar">
      <!-- Update the menu items to use router-link -->
      <div class="menu-bar-left">
        <img src="../assets/LMlogo.png" alt="LMlogo">
        <router-link to="/">LiU Marketplace</router-link>
        <router-link to="/buy">Köpa</router-link>
        <router-link to="/sell">Sälja</router-link>
      </div>
      <div class="menu-bar-right">
        <router-link to="/profile">Min Profil</router-link>
        <router-link to="/logout">Logga Ut</router-link>
      </div>
    </div>
    <!-- Add router-view to display the current page content -->
    <router-view></router-view>
  </div>
  <footer class="footer">
    <div class="column">
      <h3>Mer info</h3>
      <ul>
        <li><router-link to="/om-oss">Om oss</router-link></li>
        <li><router-link to="/vanliga-fragor">Vanliga Frågor</router-link></li>
        <li><router-link to="/kontakta-oss">Kontakta oss</router-link></li>
      </ul>
    </div>
    <div class="column">
      <h3>LiU Marketplace</h3>
      <p>For Students - By Students</p>
    </div>
    <div class="column">
      <img src="../assets/LMlogo.png" alt="LMlogo">
    </div>
  </footer>
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
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #0c264d; 
  color: white;
  padding: 10px 20px; 
  height: 80px;
}

.menu-bar-left {
  display: flex;
  align-items: center;

}

.menu-bar-right {
  display: flex;
}

.menu-bar a {
  color: white; /* White text color for menu items */
  text-decoration: none; /* Remove underline */
  margin-right: 20px; /* Add margin between menu items */
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-size: 25px;
}

.menu-bar a:hover {
  text-decoration: underline; /* Add underline on hover */
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

h3 {
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
