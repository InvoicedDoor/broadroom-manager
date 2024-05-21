<template>
  <div class="navbar">
    <div class="title">
      <h1>Administrador de sala de reuniones</h1>
    </div>
    <div class="options">
      <button @click="showModalRegister = true">Agregar usuario</button>
    </div>
  </div>
  <div v-if="showModalRegister" class="modal-overlay">
    <div class="modal-user">
      <header class="modal-header">
        <button @click="showModalRegister = false">Close</button>
        <div class="modal-title">
          <h2>Crea un usuario</h2>
        </div>
      </header>
      <ModalAddUser></ModalAddUser>
    </div>
  </div>
</template>

<script>
import ModalAddUser from './ModalAddUser.vue'

export default {
  name: 'Navbar-properties',
  data() {
    return {
      showModalRegister: false
    }
  },
  components: {
    ModalAddUser
  }
}
</script>

<style scoped>
.modal-user {
  background: #07bfff;
  padding: 20px;
  border-radius: 8px;
  height: 22rem;
  width: 30vw;
}

.navbar {
  background-color: #0978aa;
  height: 14vh;
  display: flex;
  align-items: center;
  width: 100dvw;
  margin: 0;
  padding: 0;
}

.navbar .options {
  display: flex;
  width: 10%;
  justify-content: center;
}

h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  color: white;
}

h3 {
  font-size: 1.2rem;
}

.title {
  width: 90%;
  display: flex;
  justify-content: center;
}

.navbar h1 {
  text-align: center;
}

.options {
  width: 10%;
  height: 7vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

button {
  border: none;
  background-color: #07bfff;
  appearance: none;
  height: 5vh;
  border-radius: 20px;
}

@media (min-width: 1024px) {
  .navbar h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
