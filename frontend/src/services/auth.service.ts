const BASE_URL = import.meta.env.VITE_SERVER_HOST

export interface Login
{
    email: string,
    password:string
}

export interface Register
{
    name: string,
    enrollment: string,
    email: string,
    password: string,
    bornDate: Date
}

export const isAuthenticated = () => {
    const token = localStorage.getItem('token')
    return !!token
}

export const login = async (login: Login) => {
    const LOGIN_URL = `${BASE_URL}auth/login/`
    const res = await fetch(LOGIN_URL, {
        method: 'POST',
        body: JSON.stringify(login)
    })

    const data = await res.json()

    if (res.ok)
    {
        localStorage.setItem('token', data!.token)
        return {
            message: data!.message,
            status: "Success"
        }
    }
    else
        return {
            message: data!.message,
            status: "Failed"
        }
}

export const register = async (register: Register) => {
    const REGISTER_URL = `${BASE_URL}auth/register/`
}