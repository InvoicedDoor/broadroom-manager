<!-- Renderizado de la tabla para el registro de las salas -->
<template>
  <ButtonReserve :getReservations="getReservations" />
  <div class="row">
    <div class="table-responsive">
      <table class="table table-hover table-centered mb-0">
        <thead>
          <tr class="table-dark">
            <th class="text-center col" v-for="(value, key) in props.columns">{{ value}}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in data" :key="item.id" class="table-active">
            <td class="col">{{ item.user }}</td>
            <td class="col">{{ item.room }}</td>
            <td class="text-center col">{{ item.start_time }}</td>
            <td class="text-center col">{{ item.finish_time }}</td>
            <td class="col">
              <div class="text-center">
                <button class="btn btn-outline-secondary" @click="deleteReservation(item.id)">Terminar</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
<<<<<<< HEAD
</template>

<!-- Código de TypeScript -->
<script setup>
import { getRegisters, cancelReservation } from '@/services/FunctionsFetch.ts'
import { onMounted, ref } from 'vue'
import { reservationsStore } from '@/stores/reservations';
import { toast } from 'vue3-toastify'
import ButtonReserve from './ButtonReserve.vue';

const props = defineProps({
  columns: {
    type: Object,
    required: true
=======
  <div class="table">
    <table>
      <thead>
        <tr>
          <th>Usuario</th>
          <th>Sala reservada</th>
          <th>Hora de inicio</th>
          <th>Hora de termino</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in getReservations" :key="item.id">
          <td>{{ item.user }}</td>
          <td>{{ item.room }}</td>
          <td>{{ formatDate(item.start_time) }}</td>
          <td>{{ formatDate(item.finish_time) }}</td>
          <td>
            <div class="acciones-registro">
              <button @click="deleteReservation(item.id)">Terminar</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<!-- Código de TypeScript -->
<script>
import { useReservationsStore } from '@/stores/ReservationsStore';
import { cancelReservation } from '@/services/FunctionsFetch';
import { mapState, mapActions } from 'pinia';

// Se ejecuta la función y se maneja la promesa con un await


export default {
  name: 'Table-Content',
  data() {
    return {
      data: [],
      showAlert: false
    }
  },
  computed: {
    ...mapState(useReservationsStore, ['getReservations'])
  },
  methods: {
    ...mapActions(useReservationsStore, ['getDataReservation']),
    // Función para dar un formato más legible al usuario
    formatDate(dateString) {
      const date = new Date(dateString)

      const day = String(date.getUTCDate()).padStart(2, '0')
      const month = String(date.getUTCMonth() + 1).padStart(2, '0')
      const year = date.getUTCFullYear()

      const hours = String(date.getUTCHours()).padStart(2, '0')
      const minutes = String(date.getUTCMinutes()).padStart(2, '0')
      const seconds = String(date.getUTCSeconds()).padStart(2, '0')

      return `${day}-${month}-${year} ${hours}:${minutes}:${seconds}`
    },
    async deleteReservation(id) {
      const confirmation = confirm("¿Estás seguro de querer eliminar la reservación?")
      if (confirmation) {
        const res = await cancelReservation(id)
        this.message = res.message
        this.typeAlert = res.status
        this.showAlert = true
        await this.getDataReservation()
      }
      this.message = 'No se borró la reservación.'
      this.typeAlert = 'error'
      this.showAlert = true
    },
    close() {
      this.showAlert = false
    }

>>>>>>> 8caf450adaed58061d66af7125fbada68ac29241
  }
})
const data = ref();
const reservationStore = reservationsStore()


onMounted(async () => {
  await getReservations()
});

const formatDate = (dateString) => {
  const date = new Date(dateString)
  
  const day = String(date.getUTCDate()).padStart(2, '0')
  const month = String(date.getUTCMonth() + 1).padStart(2, '0')
  const year = date.getUTCFullYear()
  
  const hours = String(date.getUTCHours()).padStart(2, '0')
  const minutes = String(date.getUTCMinutes()).padStart(2, '0')
  const seconds = String(date.getUTCSeconds()).padStart(2, '0')

  return `${day}-${month}-${year} ${hours}:${minutes}:${seconds}`
}

const deleteReservation = async (id) => {
  let res = await cancelReservation(id)
  data.value = await getRegisters()
  if (res.status === "error")
    toast.error(res.message)
  else
    toast.success(res.message)
}

const getReservations = async () => {
  await reservationStore.getReservations()
  data.value = reservationStore.reservations
}

</script>
