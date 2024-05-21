<template>
  <div v-if="showModal" class="modal-overlay">
    <div class="modal">
      <button @click="showModal = false">Close</button>
      <div class="entries">
        <label>Nombre</label>
      </div>
    </div>
  </div>
</template>

<script>
const BASE_URL = 'http://127.0.0.1:8000'
const createRegister = async () => {
  const res = await fetch(`${BASE_URL}/api/reservations/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: {}
  })
  const data = await res.json()
  return data
}

export default {
  name: 'ModalAdd',
  methods: {
    close() {
      this.$emit('close')
    }
  }
}
</script>

<style>
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
  height: 80vh;
  width: 80vw;
}
</style>
