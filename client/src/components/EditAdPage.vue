<template>
  <div class="page">
    <h1>Redigera Annons {{ buttonText }}</h1>
    <p>{{ buttonText }}</p>
    <div class="container">
      <form @submit.prevent="submitForm">
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
            <option value="" disabled>Område</option>
            <option value="Linköping">Linköping</option>
            <option value="Norrköping">Norrköping</option>
          </select>
        </div>
        <div class="row">
          <select id="condition" required v-model="condition">
            <option value="" disabled>Skick</option>
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
            <input type="file" id="addedImages" accept="image/*" multiple @change="handleImageUpload" style="display: none;" ref="fileInput">
            <div :class="{ dragging: isDragging }">
              <i class="fa fa-cloud-upload"></i> 
              <div class="add-photos-text">
                <p class="header"><strong>Lägg till foton</strong></p> 
                <p class="subheader">eller dra och släpp</p> 
              </div>
            </div>
          </div>
          <div class="image-preview-row">
            <div v-for="(existingImage, index) in existingImages" :key="index" class="image-container">
              <img :src="existingImage.image_path" alt="Image preview">
              <button @click="removeImage(index)">✖</button>
            </div>
            <div v-for="(addedImagePreview, index) in addedImagesPreviews" :key="index" class="image-container">
              <img :src="addedImagePreview" alt="Image preview">
              <!--<button @click="removeImage(index)">✖</button>-->
            </div>
          </div>
        </div>
        <button type="submit-button">Publicera ändringar</button>
        <button type="button" @click="cancelForm">Avbryt</button>
      </form>
    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {

  data() {
    return {
      id: null,
      title: '',
      description: '',
      price: null,
      area: '',
      condition: '',
      buttonText: '',
      addedImages: [],
      addedImagesPreviews: [],
      existingImages: [],
    };
  },

  created() {
    this.id = this.$route.params.id;
    const auth = JSON.parse(sessionStorage.getItem('auth'));
    if (auth) {
      const token = auth.token;

      axios.get(`/items/${this.id}`, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
        .then(response => {
          // Update the form fields with the item data
          //lets go
          this.title = response.data.title;
          this.description = response.data.description;
          this.price = response.data.price;
          this.area = response.data.area || '';
          this.condition = response.data.condition || '';
          this.existingImages = response.data.images;

          // ... handle the image field ...
        })
        .catch(error => {
          console.error(error);
        });
    } else {
      console.error('Auth token not found in sessionStorage');
    }
  },

  watch: {
    '$route.query.newButtonText': function (newButtonText) {
      this.buttonText = newButtonText;
    },
  },
  methods: {
    submitForm() {
      console.log('Submit form method called');

      const formData = new FormData();
      formData.append('title', this.title);
      formData.append('description', this.description);
      formData.append('price', this.price);
      formData.append('area', this.area);
      formData.append('condition', this.condition);

      for (let i = 0; i < this.addedImages.length; i++) {
        formData.append('images', this.addedImages[i]);
      }

      // Get the token from the session storage
      const auth = JSON.parse(sessionStorage.getItem('auth'));
      const token = auth.token;

      if (auth) {
        // Send a PUT request to update the item
        axios.put(`/items/${this.id}`, formData, {
          headers: {
            "Authorization": "Bearer " + token,
            'Content-Type': 'multipart/form-data'
          }
        })
          .then(() => {
            console.log('Item updated successfully');
            this.navigateToHistory();
            // Navigate to another page if needed
          })
          .catch(error => {
            console.error('Error updating item:', error);
          });
      } else {
        console.error('Auth token not found in sessionStorage');
      }
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
      this.addedImages = [...this.addedImages, ...newImages];
      this.addedImagesPreviews = [...this.addedImagesPreviews, ...newImagePreviews];
    },
    openFileExplorer() {
      this.$refs.fileInput.click();
    },
    navigateToHistory() {
      this.$router.push('/profile-history')
    },

    cancelForm() {
      this.$router.push('/profile-history')
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
.ctrph::placeholder {
  text-align: center;
}
</style>