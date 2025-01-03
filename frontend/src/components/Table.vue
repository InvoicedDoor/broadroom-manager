<!-- Renderizado de la tabla para el registro de las salas -->
<template>
  <ButtonReserve :getReservations="getRegisterReservations" />
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
            <td class="text-center col">{{ formatDate(item.start_time) }}</td>
            <td class="text-center col">{{ formatDate(item.finish_time) }}</td>
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
</template>

<!-- Código de TypeScript -->
<script setup>
import { getReservations, cancelReservation } from '@/services/FunctionsFetch.ts'
import { onMounted, ref } from 'vue'
import { reservationsStore } from '@/stores/reservations';
import { toast } from 'vue3-toastify'
import ButtonReserve from './ButtonReserve.vue';

const props = defineProps({
  columns: {
    type: Object,
    required: true
  }
})
const data = ref();
const reservationStore = reservationsStore()


onMounted(async () => {
  await getRegisterReservations()
});

const formatDate = (dateString) => {
  const date = new Date(dateString)

  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0'); // Meses son 0-indexed
  const day = String(date.getDate()).padStart(2, '0');
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  const seconds = String(date.getSeconds()).padStart(2, '0');

  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

const deleteReservation = async (id) => {
  let res = await cancelReservation(id)
  await getRegisterReservations()
  if (res.status === "error")
    toast.error(res.message)
  else
    toast.success(res.message)
}

const getRegisterReservations = async () => {
  data.value = await reservationStore.getReservations()
}

</script>
