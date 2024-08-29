<!-- Renderizado de la tabla para el registro de las salas -->
<template>
  <div class="delete-alert">
    <div class="alert" :class="typeAlert" v-if="showAlert">
      <div class="alert-header">
        <button @click="close()">Close</button>
      </div>
      <div>{{ message }}</div>
    </div>
  </div>
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

  }
}
</script>

<!-- Estilos para la plantilla -->
<style>
.delete-alert {
  width: 100%;
  display: flex;
  justify-content: center;
}

.table {
  width: 100%;
  display: flex;
  justify-content: center;
}

.acciones-registro {
  width: 100%;
  display: grid;
  justify-content: center;
}

.acciones-registro button {
  margin: 5px;
  height: 5vh;
  width: 5vw;
  appearance: none;
  border: none;
  color: #2446d6;
  background-color: #76fff9;
  border-radius: 20px;
}

table {
  width: 95%;
}

th {
  font-size: 30px;
}

td {
  font-size: 20px;
  color: black;
}

thead {
  background-color: #0978aa;
}

tbody {
  background-color: #0efff9;
}
</style>
