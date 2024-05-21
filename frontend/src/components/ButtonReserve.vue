<script>
import ModalRegister from '@/components/ModalReserve.vue'

export default {
  name: 'Button-to-add',
  data() {
    return {
      showModalRegister: false,
      showModal: false,
      showAlert: false
    }
  },
  components: {
    ModalRegister
  }
}
</script>

<!-- Botón para agregar reservaciones -->
<template>
  <div class="add-button">
    <div v-if="showModalRegister" class="modal-overlay">
      <div class="modal">
        <header class="modal-header">
          <button @click="showModalRegister = false">Close</button>
          <div class="modal-title">
            <h2>Reserva una sala</h2>
          </div>
        </header>
        <ModalRegister></ModalRegister>
      </div>
    </div>
    <button class="add" @click="showModalRegister = true">Reservar una sala</button>
  </div>
</template>

<style>
header {
  background-color: #0978aa;
}

.modal-header {
  height: 5rem;
  display: flex;
  align-items: center;
  padding-left: 0.5rem;
}

.modal-header button {
  margin-right: 1rem;
  width: 8vw;
}

.modal-title {
  width: 100%;
  display: flex;
  justify-content: center;
}

.modal-title h2 {
  font-size: 30px;
  color: white;
}

.add-button {
  width: 100%;
  display: flex;
  justify-content: end;
  align-items: center;
  margin: 1rem;
  height: 3rem;
}

button {
  height: 3rem;
  color: white;
  appearance: none;
  border: none;
  background-color: #2446d6;
  border-radius: 20px;
}

.add-button > button {
  width: 14vw;
  margin-right: 3vw;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: #07bfff;
  padding: 20px;
  border-radius: 8px;
  height: 32rem;
  width: 30vw;
}

@media (max-width: 1232px) {
  .modal-title > h2 {
    font-size: large;
  }
}
</style>
