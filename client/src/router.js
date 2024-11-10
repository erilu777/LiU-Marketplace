import { createRouter, createWebHashHistory } from 'vue-router'; // Importera nödvändiga funktioner från vue-router
import { checkLoginStatus } from './components/checkAuth.js'; // Importera funktionen checkLoginStatus från checkAuth.js

import HomePage from './components/HomePage.vue';
import BuyPage from './components/BuyPage.vue';
import SellPage from './components/SellPage.vue';
import ProfilePage from './components/ProfilePage.vue';
import LogoutPage from './components/LogoutPage.vue';
import AdsDetails from './components/AdsDetails.vue';
import NewAdPage from './components/NewAdPage.vue';
import FAQPage from './components/FAQPage.vue';
import ContactPage from './components/ContactPage.vue';
import AboutPage from './components/AboutPage.vue';
import EditAdPage from './components/EditAdPage.vue';
import LoginPage from './components/LoginPage.vue';
import HistoryPage from './components/HistoryPage.vue';
import EditProfilePage from './components/EditProfilePage.vue';
import ConfirmPage from './components/ConfirmPage.vue';
import MessagesPage from './components/MessagesPage.vue';

const routes = [
  {
    path: '/home',
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
    },
    {
      path: '/newad',
      name: 'newad',
      component: NewAdPage
  },
  {
    path: '/newad/:category',
    name: 'newad',
    component: NewAdPage,
    props: route => ({
      buttonText: route.query.buttonText
    })
  },
  {
    path: '/vanliga-fragor',
    name: 'faq',
    component: FAQPage
  },
  {
    path: '/kontakta-oss',
    name: 'contact',
    component: ContactPage
  },
  {
    path: '/om-oss',
    name: 'about',
    component: AboutPage
  },
  {
    path: '/edit-ad/:id',
    name: 'edit',
    component: EditAdPage
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage,
    props: true
  },
  {
    path: '/profile-history',
    name: 'history',
    component: HistoryPage
  },
  {
    path: '/edit-profile',
    name: 'editprofile',
    component: EditProfilePage
  },
  {
    path: '/ad-confirm',
    name: 'confirm',
    component: ConfirmPage
  },
  {
    path: '/messages',
    name: 'Messages',
    component: MessagesPage
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior() {
    return{ top: 0} ;
  }
});

router.beforeEach((to, from, next) => {
  const publicPages = ['/vanliga-fragor', '/kontakta-oss', '/om-oss'];
  
  if (to.path == '/login' && checkLoginStatus()) {
    next({ name: 'home'}) // Om användaren är inloggad och försöker gå till /login, skicka användaren till /home
    } else if (publicPages.includes(to.path) && !checkLoginStatus()) {
      next()
    } else {
      next() // Om användaren inte är inloggad och försöker gå till /login, skicka användaren till /login
  }
})

export default router;