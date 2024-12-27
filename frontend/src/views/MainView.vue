<template>
    <Navbar></Navbar>
    <Table :columns="columns"></Table> 
</template>

<script setup>
import ButtonReserve from '@/components/ButtonReserve.vue';
import Navbar from '@/components/Navbar.vue';
import Table from '@/components/Table.vue';

const columns = {
    user: "Usuario",
    room: "Sala",
    startTime: "Hora de inicio",
    finishTime: "Hora de término",
    actions: "Acciones",
}
</script>