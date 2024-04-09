import axios from 'axios';

export async function fetchAdsData() {
  try {
    const token = JSON.parse(sessionStorage.getItem('auth')).token; // Hämta token från sessionStorage
    console.log('Token:', token); // Log the value of the token

    const response = await axios.get('/items', {
      headers: {
        "Authorization": "Bearer " + token
      }
    });
    return response.data;
  } catch (error) {
    console.error(error);
  }
}