import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { createBootstrap } from 'bootstrap-vue-next'
import Toast from 'vue3-toastify'

import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import 'bootstrap-icons/font/bootstrap-icons.css';
import 'vue3-toastify/dist/index.css';

const app = createApp(App)

app.use(createPinia())
app.use(createBootstrap())
app.use(Toast)
app.use(router)

app.mount('#app')

export default app;