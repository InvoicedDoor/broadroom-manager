<template>
    <div class="d-flex justify-content-center align-items-center" style="width: 100vw; height: 100vh;">
        <div class="card bg-light" :style="screenWidth < 800 ? {width: '80%', height: 'auto',} : screenWidth < 1200 ? {width: '50%', height: 'auto',} : screenWidth < 1400 ? {width: '40%', height: 'auto',} : {width: '30%', height: 'auto',}">
            <div class="text-center m-4">
                <h1>Iniciar sesión</h1>
            </div>
            <div class="card-body mt-5">
                <div class="mb-3">
                    <label for="emailInput" class="form-label">Usuario</label>
                    <input 
                    class="form-control" 
                    type="email" 
                    id="emailInput" 
                    placeholder="correo@example.com"
                    @input="inputMail">
                </div>
                <div class="mb-3">
                    <label for="passwordInput" class="form-label">Contraseña</label>
                    <input 
                    class="form-control" 
                    type="password"  
                    id="passwordInput" 
                    placeholder="contraseña"
                    @input="inputPassword">
                </div>
                <div class="mb-2 d-flex" style="width: 100%; justify-content: end;">
                    <a href="" class="form-text">Registrarse</a>
                </div>
                <div class="col-auto">
                    <button 
                    class="btn btn-outline-primary mb-4 w-100" 
                    type="button"  
                    id="passwordInput" 
                    @click="handleInputButton">Iniciar sesión</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import { onMounted, ref } from 'vue';
import { toast } from 'vue3-toastify';

const email = ref()
const password = ref()
let screenWidth = ref(window.innerWidth);

onMounted(() => {
    window.addEventListener('resize', updateWidth);
})

const updateWidth = () => {
    screenWidth.value = window.innerWidth;
}

const inputMail = (e) => {
    email.value = e.target.value
    console.log(email.value)
}

const inputPassword = (e) => {
    password.value = e.target.value
    console.log(password.value)
}

const handleInputButton = () => {
    if (email.value != undefined && password.value != undefined)
        toast.success(`Se enviará ${email.value} y ${password.value}`)
    else
        toast.error("Complete los campos requeridos.", {
    autoClose: 3000,
    position: 'top-right',
    closeOnClick: true,
    pauseOnHover: true,
})
}
</script>