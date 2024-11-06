<template>
  <div class="page">
    <h1>Försäljning av {{ category }}</h1>
    <div class="container">
      <form @submit.prevent="addItem">
        <div class="row">
          <input type="text" id="title" v-model="title" required placeholder="Titel" class="ctrph">
        </div>
        <div class="row">
          <textarea id="description" v-model="description" required placeholder="Beskrivning" class="ctrph"></textarea>
        </div>
        <div class="row">
          <input type="number" id="price" v-model="price" required placeholder="Pris" class="ctrph">
        </div>
        <div class="row">
          <select id="area" required v-model="area">
            <option value="" disabled selected>Område</option>
            <option value="Linköping">Linköping</option>
            <option value="Norrköping">Norrköping</option>
          </select>
        </div>
        <div class="row">
          <select id="condition" required v-model="condition">
            <option value="" disabled selected>Skick</option>
            <option value="Nytt">Nytt</option>
            <option value="Använd_Nyskick">Använd - nyskick</option>
            <option value="Använd_Gott_skick">Använd - gott skick</option>
            <option value="Använd_Slitet_skick">Använd - använt skick</option>
          </select>
        </div>
        <div class="row">
          <div class="row drop-zone" 
            @dragover.prevent="dragOver"
            @dragleave.prevent.stop="dragLeave"
            @drop.prevent="handleImageUpload"
            @click="openFileExplorer"
            :class="{ 'isDragging': isDragging }">
            <input type="file" id="image" accept="image/*" multiple @change="handleImageUpload" style="display: none;" ref="fileInput">
            <div :class="{ dragging: isDragging }">
              <i class="fa fa-cloud-upload"></i> 
              <div class="add-photos-text">
                <p class="header"><strong>Lägg till foton</strong></p> 
                <p class="subheader">eller dra och släpp</p> 
              </div>
            </div>
          </div>
          <div class="image-preview-row">
            <div v-for="(imagePreview, index) in imagePreviews" :key="index" class="image-container">
              <img :src="imagePreview" alt="Image preview">
              <button @click="removeImage(index)">✖</button>
            </div>
          </div>
        </div>
        <button type="submit">Publicera annons</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      category: '',
      area: '',
      condition: '',
      images: [],
      imagePreviews: [],
      isDragging: false,
    };
  },
  created() {
    this.category = this.$route.params.category;
  },
  methods: {
    addItem() {
      const token = JSON.parse(sessionStorage.getItem('auth')).token; // Hämta token från sessionStorage
      console.log('Token:', token); // Log the value of the token
      
      if (!this.category || !this.title || !this.description || !this.price || !this.condition || !this.area) {
        alert('Fyll i alla fält.');
        return;
      }

      if (!this.images || this.images.length === 0) {
        alert('Glöm inte att lägga till en bild.');
        return;
      }

      const formData = new FormData();
      formData.append('category', this.category);
      formData.append('title', this.title);
      formData.append('description', this.description);
      formData.append('price', this.price);
      formData.append('condition', this.condition);
      formData.append('area', this.area);
      formData.append('date', new Date().toISOString());
      
      for (let i = 0; i < this.images.length; i++) {
        formData.append('images', this.images[i]);
      }

      axios.post('/items', formData, {
        headers: {
          "Authorization": "Bearer " + token,
          'Content-Type': 'multipart/form-data' 
        }
      })
        .then(response => {
          console.log('Response:', response);
        })
        .catch(error => {
          console.log('Error:', error);
        });
      this.$router.push('/home');
    },
    handleImageUpload(event) {

      this.isDragging = false;
      let newImages;

      if (event.type === 'drop') {
        event.preventDefault();
        newImages = Array.from(event.dataTransfer.files);
      }else{
        newImages = Array.from(event.target.files);
      }
      for (let i = 0; i < newImages.length; i++) {
        if (!newImages[i].type.startsWith('image/')) {
          alert('Alla filer måste vara bilder.');
          return;
        }
      }
      const newImagePreviews = newImages.map(image => URL.createObjectURL(image));
      this.images = [...this.images, ...newImages];
      this.imagePreviews = [...this.imagePreviews, ...newImagePreviews];
    },
    removeImage(index) {
      event.preventDefault();
      this.images.splice(index, 1);
      this.imagePreviews.splice(index, 1);
    },
    openFileExplorer() {
      this.$refs.fileInput.click();
    },
    dragOver() {
    this.isDragging = true;
    },
    dragLeave() {
    this.isDragging = false;
    }
  }
};
</script>

<style scoped>
.page {
  padding: 60px;
  min-height: 80vh;
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
  width: 700px;
  margin: 0 auto;
  padding: 50px;
}

.row {
  padding: 10px;
  width: 70%;
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
  margin-top: 15px;
}

.ctrph::placeholder {
  text-align: center;
}
.image-preview-row {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}
.image-container {
  position: relative;
  display: inline-block;
  width: 170px;
  height: 170px;
  margin-top: 20px;
  margin-right: 10px;
}
.image-container img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  background-color: transparent;
}
.image-container button {
  position: absolute;
  top: 0;
  right: 0;
  background-color: transparent;
  color: red;
  border: none;
  font-weight: bold;
  cursor: pointer;
  font-size: 20px;
}
.drop-zone {
  background-color: #e7f2f7;
  border: 3px dashed #bbd5e9; /* Use dashed border for drop zone indication */
  border-radius: 20px;
  width: 95%;
  height: 200px;
  margin: 20px auto;
  padding: 20px;
  text-align: center;
  cursor: pointer;
}

.drop-zone.isDragging { 
  border-color: #8b8c95; /* Update border color when dragging */
  background-color: #a6c2d7;  /* Add a subtle background color change */
  width: 100%;
  height: 220px;
}
.drop-zone .add-photos-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #3d4056;
}
.drop-zone .add-photos-text .header {
  font-size: 20px;
  font-weight: bold;
}
.drop-zone .add-photos-text .subheader {
  font-size: 16px;
}
</style>b