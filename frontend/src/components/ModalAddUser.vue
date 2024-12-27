<template>
  <div class="entries add-user">
    <div class="entry">
      <div class="section-title">
        <label>Nombre</label>
      </div>
      <input type="text" v-model="name" />
    </div>
    <div class="entry">
      <div class="section-title">
        <label>Matrícula</label>
      </div>
      <input type="text" v-model="enrollment" />
    </div>
    <button @click="createUser()">Registrar</button>
  </div>
</template>

<script setup>
import { addUser } from '@/services/FunctionsFetch';
import { ref } from 'vue';
import { toast } from 'vue3-toastify';

const name =  ref('');
const enrollment = ref('');

const close = () => {
  $emit('close')
}

const createUser = async () => {
  if (!enrollment.value || !name.value) {
    return
  }

  const res = await addUser(enrollment.value, name.value);
  if (res.status === 'success')
  {
    toast.success(res.message, {
      position: "top-right",
      autoClose: 3000,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
    })
    return
  }
  else if(res.status === "error")
  {
    toast.error(res.message, {
      position: "top-right",
      autoClose: 3000,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
    })
    return
  }
  else
  {
    toast.error("No hay respuesta, intentelo más tarde", {
      position: "top-right",
      autoClose: 3000,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
    })
    return
  }
}
</script>

<style></style>
