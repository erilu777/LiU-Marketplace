import { createRouter, createWebHistory } from 'vue-router'; // Importera nödvändiga funktioner från vue-router

import HomePage from './components/HomePage.vue';
import BuyPage from './components/BuyPage.vue';
import SellPage from './components/SellPage.vue';
import ProfilePage from './components/ProfilePage.vue';
import LogoutPage from './components/LogoutPage.vue';
import AdsDetails from './components/AdsDetails.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/buy',
    name: 'buy',
    component: BuyPage
  },
  {
    path: '/sell',
    name: 'sell',
    component: SellPage
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfilePage
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutPage
  },
  {
    path: '/ads/:id',
      name: 'AdsDetails',
      component: AdsDetails,
      props: route => ({
        id: parseInt(route.params.id),
        imageUrl: route.query.imageUrl,
        name: route.query.name,
        price: route.query.price,
        condition: route.query.condition,
        location: route.query.location,
        category: route.query.category,
        description: route.query.description
      })
    }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
