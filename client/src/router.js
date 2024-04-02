import { createRouter, createWebHistory } from 'vue-router'; // Importera nödvändiga funktioner från vue-router

import HomePage from './components/HomePage.vue';
import BuyPage from './components/BuyPage.vue';
import SellPage from './components/SellPage.vue';
import ProfilePage from './components/ProfilePage.vue';
import LogoutPage from './components/LogoutPage.vue';

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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
