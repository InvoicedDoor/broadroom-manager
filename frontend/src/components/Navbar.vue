<template>
  <div class="navbar navbar-expand-lg bg-black">
    <div class="container-fluid">
      <h1 class="navbar-brand text-white">Administrador de sala de reuniones</h1>
    </div>
    <div class="mx-5 my-3 mb-4">
      <Popper hover arrow placement="top" content="Cerrar sesión" style="text-align:left; color: white;">
        <button @click="logout" type="button" class="btn btn-outline-light" style="padding:5px">
          <i class="fa-solid fa-right-from-bracket fs-1"></i>
        </button>
      </Popper>
    </div>
  </div>
  <div v-if="showModalRegister" class="modal-overlay">
    <div class="modal-user">
      <header class="modal-header">
        <button class="btn btn-primary" @click="showModalRegister = false">Close</button>
        <div class="modal-title">
          <h2>Crea un usuario</h2>
        </div>
      </header>
      <ModalAddUser></ModalAddUser>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import ModalAddUser from './ModalAddUser.vue'
import Popper from 'vue3-popper';
import { useRouter } from 'vue-router';

const router = useRouter()

const showModalRegister = ref(false);

const logout = async () => {
    localStorage.clear()
    router.push('/login')
}
</script>
