<template>
    <div class="page">
        <h1>Klart!</h1>
        <h3>Nu är din annons publicerad.</h3>
        <button @click="navigateToHistory">Gå till dina annonser</button>
        <button @click="navigateToSell">Skapa en ny annons</button>
    </div>
</template>

<script>
export default{
    methods: {
        navigateToHistory() {
            this.$router.push('/profile-history')
        },
        navigateToSell() {
            this.$router.push('/sell')
        }
    }
}
</script>

<style>
.page {
    padding: 60px;
    min-height: 80vh;
    margin: 0 auto;
  }

h1 {
    font-weight: bold;
    font-size: 60px;
    color: #0c264d;
    padding-bottom: 20px;
  }

button {
    margin-top: 100px;
}
</style>