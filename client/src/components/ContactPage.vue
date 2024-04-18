<template>
    <div class="page">
      <h1>Kontakta Oss</h1>
      <div class="container">
        <form @submit.prevent="submitForm">
            <div class="row">
                <input type="text" id="name" v-model="name" placeholder="Namn" class="ctrph" required>
            </div>
            <div class="row">
                <input type="email" id="email" v-model="email" placeholder="Email" class="ctrph" required>
            </div>
            <div class="row">
                <input type="subject" v-model="subject" placeholder="Ämnesrad" class="ctrph" required>
            </div>
            <div class="row">
                <textarea id="description" v-model="description" placeholder="Din Fråga" class="ctrph" required></textarea>
            </div>
            <button @click="submit" class="contact-button" style="color: white">Skicka</button>
        </form>
      </div>
    </div>
</template>

<script>
  export default {
  data() {
    return {
      buttonText: '',
      area: '',
      condition: '',
      name: '',
      email: '',
    };
  },
  watch: {
    '$route.params.buttonText': function(newButtonText) {
    this.buttonText = newButtonText;
    }
  },
  methods: {
    submitForm() {
      console.log('Formulärdata:', this.name, this.image);
    },
    handleImageUpload(event) {
      const file = event.target.files[0];
      this.image = file;
    },
    submit() {
      const contactEmail = 'liu@marketplace.com'
      const subject = this.subject; // Subject line for the email
      const body = this.description + '\n\nMed vänliga hälsningar,\n' + this.name + '\n' + this.email; // Body of the email

      // Generate the mailto link with the seller's email, subject, and body
      const mailtoLink = 'mailto:' + encodeURIComponent(contactEmail) +
                        '?subject=' + encodeURIComponent(subject) +
                        '&body=' + encodeURIComponent(body);

      // Open the email client with the pre-filled email
      window.location.href = mailtoLink;
      }
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

  .container {
    background-color: #e7f2f7;
    border: 3px solid #bbd5e9;
    border-radius: 20px;
    width: 500px;
    margin: 0 auto;
    padding: 30px;
  }

  .row {
    padding: 10px;
    margin: 0 auto;
  }

  button {
    background-color: #0c264d;
    border-color: #bbd5e9;
    padding: 10px;
    width: 40%;
    border-radius: 20px;
    color: white;
    font-weight: bold;
    margin-top: 20px;
  }

  .ctrph::placeholder {
    text-align: center; 
  }
</style>








