<script setup>
import { reserve, getUsers, getRooms } from '@/services/FunctionsFetch.ts'
import { reservationsStore } from '@/stores/reservations';
import { onMounted, ref } from 'vue';
import { toast } from 'vue3-toastify';

const users = ref();
const rooms = ref();
const showAlert = ref(false);
const typeAlert = ref('');
const message = ref('');
const room = ref('');
const user = ref('');
const start = ref('');
const finish = ref('');
const room_id = ref('default');
const user_id = ref('default');
const reservationStore = reservationsStore();



onMounted(async () => {
  users.value = await getUsers();
  rooms.value = await getRooms();
});

const props = defineProps({
  getReservations: {
    type: Function,
    required: true
  }
})

const formatDate = (date) => {
  const localDate = new Date(date.value)
  return date.toLocaleString('es-MX', {
    timeZone: 'America/Mexico_City', // Asegura que coincida con la zona horaria del backend
    hour12: true, // Formato de 12 horas (AM/PM)
  });
}

const doReservation = async () => {
  if (!user_id.value || !room_id.value || !start.value || !finish.value) {
    toast.error('Complete los campos primero')
    return;
  }
  
  formatDate(start)
  formatDate(finish)

  const res = await reserve(user_id.value, room_id.value, start.value, finish.value)

  if (res.status === 'error')
    toast.error(res.message)
  else
    toast.success(res.message)

  await props.getReservations();
}

</script>

<template>
  <div class="mb-3">
    <label>Usuario</label>
    <select v-model="user" class="form-select">
      <option disabled value="default">Selecciona una usuario</option>
      <option @click="user_id = $event.target.id" v-for="user in users" :key="user.user_id" :id="user.user_id">
        {{ user.name }}
      </option>
    </select>
  </div>
  <div class="mb-3">
    <label>Sala</label>
    <select v-model="room" class="form-select">
      <option disabled value="default">Selecciona una sala</option>
      <option @click="room_id = room.broadroom_id" v-for="room in rooms" :key="room.broadroom_id"
        :id="room.broadroom_id">
        {{ room.name }}
      </option>
    </select>
  </div>
  <div class="mb-3">
    <label class="form-label">Hora de inicio</label>
    <input class="form-control" type="datetime-local" v-model="start" />
  </div>
  <div class="mb-3">
    <label class="form-label">Hora de término</label>
    <input class="form-control" type="datetime-local" v-model="finish" />
  </div>
  <button class="btn btn-primary" v-on:click="doReservation()">Reservar</button>
</template>
