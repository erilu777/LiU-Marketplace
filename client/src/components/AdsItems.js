import axios from 'axios';

export async function fetchAdsData() {
  try {
    const response = await axios.get('http://localhost:5000/items');
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
}