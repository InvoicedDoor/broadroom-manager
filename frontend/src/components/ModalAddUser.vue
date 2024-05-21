<template>
  <div class="entries add-user">
    <div class="entry">
      <div class="section-title">
        <label>Nombre</label>
      </div>
      <input type="text" v-model="name" />
    </div>
    <div class="entry">
      <div class="section-title">
        <label>Matrícula</label>
      </div>
      <input type="text" v-model="enrollment" />
    </div>
    <button @click="createUser()">Registrar</button>
  </div>
</template>

<script>
const BASE_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ModalAdd',
  data() {
    return {
      name: '',
      enrollment: ''
    }
  },
  methods: {
    close() {
      this.$emit('close')
    },
    async createUser() {
      console.log(this.name, this.enrollment)
      if (!this.enrollment || !this.name) {
        return
      }

      const res = await fetch(`${BASE_URL}/api/users/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          name: this.name,
          enrollment: this.enrollment
        })
      })
      const data = await res.json()
      console.log(data)
      return data
    }
  }
}
</script>

<style></style>
