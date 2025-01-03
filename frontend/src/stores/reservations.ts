import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getReservations } from '@/services/FunctionsFetch'

export const reservationsStore = defineStore('reservations', () => {
    const reservations = ref()
    async function getReservationStore() {
        reservations.value = await getReservations();
    }

    return { reservations, getReservations }
})