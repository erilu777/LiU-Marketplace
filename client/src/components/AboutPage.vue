<template>
  <div class="page">
    <h1>THE TEAM</h1>
    <p>Det här är ett kandidatarbete på Linköpings Universitet. Vi är 7 studenter på I-sektionen med teknisk inriktning
      Datateknik.</p>
    <div class="team">
      <div class="team-member" v-for="member in teamMembers" :key="member.name">
        <img :src="member.image" :alt="member.name" class="team-member-image">
        <h2 class="team-member-title">{{ member.name }}: {{ member.title }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pageTitle: 'Om Oss',
      teamMembers: [
        { name: 'Ella', title: 'Front-End Developer', image: require('../assets/ella.png') },
        { name: 'Olivia', title: 'Front-End Developer', image: require('../assets/olivia.png') },
        { name: 'Fredrik', title: 'Git Master', image: require('../assets/fredrik.png') },
        { name: 'Erik A', title: 'Scrum Master', image: require('../assets/erikA.png') },
        { name: 'Erik L', title: 'Back-End Developer', image: require('../assets/erikL.png') },
        { name: 'Axel', title: 'Back-End Developer', image: require('../assets/axel.png') },
        { name: 'Adrian', title: 'Writing Angel', image: require('../assets/adrian.png') },
      ],
    };
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
  padding-bottom: 40px;
}

.team {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.team-member {
  flex: 1 0 21%; /* Adjust this value as needed */
  margin: 10px;
  text-align: center;
}

.team-member-image {
  width: 100%;
  height: auto;
}
</style>