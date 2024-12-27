import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getRegisters } from '@/services/FunctionsFetch'

export const reservationsStore = defineStore('reservations', () => {
    const reservations = ref()
    async function getReservations() {
        reservations.value = await getRegisters();
    }

    return { reservations, getReservations }
})