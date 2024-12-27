const BASE_URL = 'http://localhost:5000'

interface Login
{
    email: string,
    password:string
}

interface Register
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
    const LOGIN_URL = `${BASE_URL}/login`
}

export const register = async (register: Register) => {
    const REGISTER_URL = `${BASE_URL}/register`
}