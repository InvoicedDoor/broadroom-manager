<<<<<<< HEAD
<template>
  <div class="row d-flex justify-content-end m-3">
    <button type="button" class="btn btn-outline-dark bg-black" style="width: 10vw;" data-bs-toggle="modal"
      data-bs-target="#reserveModal">
      Reservar sala
    </button>

    <div class="modal fade" id="reserveModal" tabindex="-1" aria-labelledby="reserveModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-sm">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="reserveModalLabel">Reserva una sala</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
=======
<script>
import ModalRegister from '@/components/ModalReserve.vue'
import { useShowModalStore } from '@/stores/ShowModalStore';
import { mapActions, mapState } from 'pinia';

export default {
  name: 'Button-to-add',
  data() {
    return {
      showAlert: false
    }
  },
  computed: {
    ...mapState(useShowModalStore, ['getShowModal'])
  },
  components: {
    ModalRegister
  },
  methods: {
    ...mapActions(useShowModalStore, ['showModal', 'hiddenModal'])
  }
}
</script>

<!-- Botón para agregar reservaciones -->
<template>
  <div class="add-button">
    <div v-if="getShowModal" class="modal-overlay">
      <div class="modal">
        <header class="modal-header">
          <button @click="hiddenModal()">Close</button>
          <div class="modal-title">
            <h2>Reserva una sala</h2>
>>>>>>> 8caf450adaed58061d66af7125fbada68ac29241
          </div>
          <div class="modal-body">
            <ModalRegister :getReservations="props.getReservations" />
          </div>
        </div>
      </div>
    </div>
<<<<<<< HEAD
=======
    <button class="add" @click="showModal()">Reservar una sala</button>
>>>>>>> 8caf450adaed58061d66af7125fbada68ac29241
  </div>
</template>

<script setup>
import ModalRegister from '@/components/ModalReserve.vue'
import { ref } from 'vue';

const showModalRegister = ref(false);

const props = defineProps({
  getReservations: {
    type: Function,
    required: true
  }
})

</script>
