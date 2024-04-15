import axios from 'axios';

export async function fetchAdsData() {
  try {
    const token = JSON.parse(sessionStorage.getItem('auth')).token; // Fetch token from sessionStorage
    console.log('Token:', token); // Log the value of the token

    const response = await axios.get('/all_available_items', {
      headers: {
        "Authorization": "Bearer " + token
      }
    });
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

export async function fetchAdData(id) {
  try {
    const token = JSON.parse(sessionStorage.getItem('auth')).token; // Fetch token from sessionStorage
    console.log('Token:', token); // Log the value of the token

    const response = await axios.get(`/items/${id}`, {
      headers: {
        "Authorization": "Bearer " + token
      }
    });
    if (response.data) {
      return response.data;
    }else{
      throw new Error('No data found');
    }
  } catch (error) {
    console.error(error);
  }
}