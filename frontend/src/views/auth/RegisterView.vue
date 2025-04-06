<template>
    <div class="d-flex justify-content-center align-items-center" style="width: 100vw; height: 100vh;">
        <div class="card bg-light" :style="screenWidth < 800 ? {width: '80%', height: 'auto',} : screenWidth < 1200 ? {width: '50%', height: 'auto',} : screenWidth < 1400 ? {width: '40%', height: 'auto',} : {width: '30%', height: 'auto',}">
            <div class="text-center m-4">
                <h1>Registrarse</h1>
            </div>
            <div class="card-body">
                <div class="mb-3">
                    <label for="nameInput" class="form-label">Nombre</label>
                    <input 
                    class="form-control" 
                    type="text" 
                    id="nameInput" 
                    placeholder="Nombre completo"
                    @input="inputName">
                </div>
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
import { login } from '@/services/auth.service';

const name = ref()
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
}

const inputName = (e) => {
    name.value = e.target.value
}

const inputPassword = (e) => {
    password.value = e.target.value
}

const handleInputButton = async () => {
    if (email.value != undefined && password.value != undefined)
    {
        console.log()

        return
        const loginValues = {
            email: email.value,
            password: password.value
        }

        const res = await login(loginValues);

        if (res.status == "Success")
        {
            toast.success(res.message)
            window.location.href ='/'
        }
        else
            toast.warn(res.message)
    }
    else
        toast.error("Complete los campos requeridos.", {
    autoClose: 3000,
    position: 'top-right',
    closeOnClick: true,
    pauseOnHover: true,
})
}
</script>