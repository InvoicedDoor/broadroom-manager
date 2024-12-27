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
          </div>
          <div class="modal-body">
            <ModalRegister :getReservations="props.getReservations" />
          </div>
        </div>
      </div>
    </div>
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
