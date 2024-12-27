<script setup>
import { reserve, getUsers, getRooms } from '@/services/FunctionsFetch.ts'
<<<<<<< HEAD
import { reservationsStore } from '@/stores/reservations';
import { onMounted, ref } from 'vue';
import { toast } from 'vue3-toastify';
=======
import { useReservationsStore } from '@/stores/ReservationsStore';
import { useShowModalStore } from '@/stores/ShowModalStore';

import { mapActions, mapState } from 'pinia';
>>>>>>> 8caf450adaed58061d66af7125fbada68ac29241

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

<<<<<<< HEAD


onMounted(async () => {
  users.value = await getUsers();
  rooms.value = await getRooms();
});

const props = defineProps({
  getReservations: {
    type: Function,
    required: true
=======
export default {
  name: 'Button-to-add',
  data() {
    return {
      users: users,
      showAlert: false,
      typeAlert: '',
      message: '',
      rooms: rooms,
      room_id: 'default',
      user_id: 'default',
      user: '',
      room: '',
      start: '',
      finish: ''
    }
  },
  computed: {
    ...mapState(useReservationsStore, ['getReservations'])
  },
  methods: {
    ...mapActions(useReservationsStore, ['getDataReservation']),
    ...mapActions(useShowModalStore, ['hiddenModal']),
    async doReservation() {
      if (!this.user_id || !this.room_id || !this.start || !this.finish) {
        this.typeAlert = 'error'
        this.message = 'Complete los campos primero'
        this.showAlert = true
        return
      }

      const res = await reserve(this.user_id, this.room_id, this.start, this.finish)
      if (new Date().toISOString() === this.finish) {
        await this.getReservations()
      } 
      this.typeAlert = res.status
      this.message = res.message
      this.showAlert = true
      await this.getDataReservation()
      this.hiddenModal()
    },
    async close() {
      this.showAlert = false
    }
>>>>>>> 8caf450adaed58061d66af7125fbada68ac29241
  }
})

const doReservation = async () => {
  if (!user_id.value || !room_id.value || !start.value || !finish.value) {
    toast.error('Complete los campos primero')
    return;
  }

  const res = await reserve(user_id.value, room_id.value, start.value, finish.value)

  console.log(res.status)

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
<<<<<<< HEAD
  <div class="mb-3">
    <label>Sala</label>
    <select v-model="room" class="form-select">
      <option disabled value="default">Selecciona una sala</option>
      <option @click="room_id = room.broadroom_id" v-for="room in rooms" :key="room.broadroom_id"
        :id="room.broadroom_id">
        {{ room.name }}
      </option>
    </select>
=======
  <div class="entries">
    <div class="entry">
      <div class="section-title">
        <label>Usuario</label>
      </div>
      <select v-model="user" name="select-user" id="select-user">
        <option disabled value="default">Selecciona una usuario</option>
        <option
          @click="user_id = $event.target.id"
          v-for="user in users"
          :key="user.user_id"
          :id="user.user_id"
        >
          {{ user.name }}
        </option>
      </select>
    </div>
    <div class="entry">
      <div class="section-title">
        <label>Sala</label>
      </div>
      <select v-model="room" name="select-room" id="select-room">
        <option disabled value="default">Selecciona una sala</option>
        <option
          @click="room_id = room.broadroom_id"
          v-for="room in rooms"
          :key="room.broadroom_id"
          :id="room.broadroom_id"
        >
          <div class="room-info">
            {{ room.name }}
          </div>
        </option>
      </select>
    </div>
    <div class="entry">
      <div class="section-title">
        <label>Hora de inicio</label>
      </div>
      <input type="datetime-local" v-model="start" />
    </div>
    <div class="entry">
      <div class="section-title">
        <label>Hora de término</label>
      </div>
      <input name="finish-time" type="datetime-local" v-model="finish" />
    </div>
    <button v-on:click="doReservation()">Reservar</button>
>>>>>>> 8caf450adaed58061d66af7125fbada68ac29241
  </div>
  <div class="mb-3">
    <label class="form-label">Hora de inicio</label>
    <input class="form-control" type="time" v-model="start" />
  </div>
  <div class="mb-3">
    <label class="form-label">Hora de término</label>
    <input class="form-control" type="time" v-model="finish" />
  </div>
  <button class="btn btn-primary" v-on:click="doReservation()">Reservar</button>
</template>
