<script>
import { reserve, getUsers, getRooms } from '@/services/FunctionsFetch.ts'
import { useReservationsStore } from '@/stores/ReservationsStore';
import { useShowModalStore } from '@/stores/ShowModalStore';

import { mapActions, mapState } from 'pinia';

let users = await getUsers()
let rooms = await getRooms()

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
  }
}
</script>

<template>
  <div class="alert" :class="typeAlert" v-if="showAlert">
    <div class="alert-header">
      <button @click="close()">Close</button>
    </div>
    <div>{{ message }}</div>
  </div>
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
  </div>
</template>

<style>
.entries {
  background-color: none;
  height: 90%;
  margin-top: 1%;
}

.error {
  background-color: red;
  color: white;
}

.success {
  background-color: rgb(25, 214, 7);
  color: white;
}

.entry {
  height: 3rem;
  width: 100%;
  display: flex;
  margin-top: 2rem;
  margin-bottom: 1rem;
  align-items: center;
  border: 1px black solid;
  border-radius: 5px;
  background-color: #0978aa;
}

.alert-header {
  display: flex;
}

select,
input {
  width: 62%;
  height: 2rem;
  border: 1px black solid;
  border-radius: 5px;
  margin-left: 0.5rem;
}

.entry > .section-title {
  width: 35%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px black solid;
  border-radius: 5px;
}

.alert {
  /* background: #0978aa; */
  border: solid;
  position: absolute;
  padding: 20px;
  border-radius: 8px;
  height: 10rem;
  width: 28vw;
}

.entries label {
  font-size: 1rem;
  color: white;
  width: 100%;
  text-align: center;
}

.entries button {
  font-size: 1rem;
  width: 100%;
  margin-top: 0.5rem;
}

.room-info {
  display: grid;
  grid-row: auto;
}

.room-name,
.room-description {
  grid-column: auto;
}
</style>
