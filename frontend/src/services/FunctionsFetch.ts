const BASE_URL = import.meta.env.VITE_SERVER_HOST

/* Método GET */
export const getReservations = async () => {
  const res = await fetch(`${BASE_URL}reservations`, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `${localStorage.getItem('token')}`
    }
  })


  if (res.ok)
  {
    const data:any = await res.json()
    return data['message']
  }
  else {
    console.log("No se puede realizar: " + res)
  }
}

export const getUsers = async () => {
  const res = await fetch(`${BASE_URL}users/`, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `${localStorage.getItem('token')}`
    }
  })
  if (res.ok)
  {
    const data = await res.json()
    return data
  }
  console.log("Error del servidor: " + res)
}

export const getRooms = async () => {
  const res = await fetch(`${BASE_URL}broadrooms/`, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `${localStorage.getItem('token')}`
    }
  })

  if (res.ok)
  {
    const data = await res.json()
    return data
  }
  console.log("Error del servidor: " + res)
}

/* Método POST */
// función para registrar reservaciones
export const reserve = async (
  user_id: number,
  broadroom_id: number,
  start_time: Date,
  finish_time: Date
) => {
  const res = await fetch(`${BASE_URL}reservations/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `${localStorage.getItem('token')}`
    },
    body: JSON.stringify({
      users_id: user_id,
      broadrooms_id: broadroom_id,
      start_time: start_time,
      finish_time: finish_time
    })
  })
  const data = await res.json()
  return data
}

// función para registrar reservaciones
export const addUser = async (enrollment: string, name: string) => {
  const res = await fetch(`${BASE_URL}users/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `${localStorage.getItem('token')}`
    },
    body: JSON.stringify({
      enrollment: enrollment,
      name: name
    })
  })
  if (!res) {
    return {
      status: 'error',
      message: 'No se pudo hacer la petición!'
    }
  }

  return {
    status: 'success',
    message: 'El usuario se creó correctamente!'
  }
}

/* DELETE */
// función para registrar reservaciones
export const cancelReservation = async (id: number) => {
  const res = await fetch(`${BASE_URL}reservations/${id}/`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `${localStorage.getItem('token')}`
    }
  })
  if (!res) {
    return {
      status: 'error',
      message: 'La reservación no existe!'
    }
  }
  return {
    status: 'success',
    message: 'La reservación se eliminó correctamente!'
  }
}
