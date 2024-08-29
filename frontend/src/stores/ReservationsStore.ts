import { defineStore } from "pinia";
import { getReservations } from "@/services/FunctionsFetch";

const dataRaw = await getReservations()

export const useReservationsStore = defineStore('reservationsStore', {
    state: ()=> ({
        reservations: dataRaw
    }),
    getters: {
        getReservations (state) {
            return state.reservations
        }
    },
    actions: {
        async getDataReservation () {
            const dataReservations = await getReservations()
            this.reservations = await dataReservations
        }
    }
})