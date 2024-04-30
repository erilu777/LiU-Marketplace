
import 'bootstrap/dist/css/bootstrap.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies'

createApp(App)
    .use(router)
    .use(VueCookies)
    .mount('#app')
