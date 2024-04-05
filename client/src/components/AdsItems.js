import axios from 'axios';

export let adsData = [];

axios.get('http://localhost:5000/items')  // replace with your Flask server URL
  .then(response => {
    adsData = response.data;
    console.log(adsData);
  })
  .catch(error => console.error(error));