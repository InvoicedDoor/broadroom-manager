<script setup lang="ts">
import { useRouter } from 'vue-router';
import { isAuthenticated } from './services/auth.service';
import LoginView from './views/auth/LoginView.vue';
import MainView from './views/MainView.vue';
import router from './router'; 
</script>

<template>
  <div id="app" class="root">
    <router-view></router-view>
  </div>
</template>

<style>
.root {
  width: 100vw;
  margin: 0;
  overflow: hidden;
}
</style>
