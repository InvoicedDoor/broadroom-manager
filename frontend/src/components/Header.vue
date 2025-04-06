<template>
    <div class="d-flex" :style="headerStyle">
        <div class="w-50">
            <img class="m-2" src="https://sii.upa.edu.mx/image/icono/logo_upp.png" :style="imageStyle" alt="" srcset="">
        </div>
        <div class="d-flex justify-content-end align-items-center w-50">
            <div class="user-info cursorpointer">
                <div class="circular-container bg-upa-main-color">
                    <i class="fa fa-user text-ligth"></i>
                </div>
                <div class="tx-upa-main-color mx-3">
                    <h4>Jorge Ricardo Ramirez Hernandez</h4>
                </div>
            </div>
            <div class="circular-container text-red cursorpointer margin-logout">
                <i class="fa fa-right-from-bracket mx-4"></i>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

    const headerStyle = {
        backgroundColor: 'white',
        color: 'white',
        padding: '10px',
        height: '12vh',
    }

    const imageStyle = {
        height: '8vh',
    }
</script>

<style>
.user-info {
    display: flex;
    width: 45%;
    align-items: center;
}
.bg-upa-main-color {
    background-color: #011140;
    color: white;

}
.tx-upa-main-color {
    color: #011140;
    font-family: 'Inter', sans-serif;
}
.cursorpointer {
    cursor: pointer;
}
.text-red {
    background-color: red;
    color: white;
}
.circular-container {
    width: 3vw;
    height: 3vw;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 100%;
}
.margin-logout {
    margin-right: 2vw;
    margin-left: 2vw;
}

</style>