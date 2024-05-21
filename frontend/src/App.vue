<script setup lang="ts">
import Navbar from './components/Navbar.vue'
import ButtonReserve from './components/ButtonReserve.vue'
import Table from './components/Table.vue'
</script>

<template>
  <div class="root">
    <Navbar></Navbar>
    <ButtonReserve></ButtonReserve>
    <Table></Table>
  </div>
</template>

<style>
.root {
  width: 100vw;
  margin: 0;
  overflow: hidden;
}
</style>
