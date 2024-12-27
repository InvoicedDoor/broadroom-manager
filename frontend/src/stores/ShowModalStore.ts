import { defineStore } from "pinia";

export const useShowModalStore = defineStore('showModalStore', {
    state: ()=> ({
        showModalState: false
    }),
    getters: {
        getShowModal (state) {
            return state.showModalState
        }
    },
    actions: {
        showModal () {
            this.showModalState = true
        },
        hiddenModal () {
            this.showModalState = false
        }
    }
})