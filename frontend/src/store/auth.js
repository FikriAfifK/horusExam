import { defineStore } from 'pinia'
import api from '../services/api'
import router from '../router'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: JSON.parse(localStorage.getItem('user')) || null,
        token: localStorage.getItem('token') || null,
    }),

    getters: {
        isAuthenticated: (state) => !!state.token,
    },

    actions: {
        async login(username, password) {
            try {
                const res = await api.post('/users/login', { username, password })
                this.token = res.data.token
                this.user = res.data.user
                localStorage.setItem('token', this.token)
                localStorage.setItem('user', JSON.stringify(this.user))
                router.push('/dashboard')
            } catch (err) {
                const msg = err.response?.data?.error || 'Login gagal. Periksa kembali username/password.'
                alert(msg)
                console.error('Login error:', err)
            }
        },
        async register(data) {
            try {
                await api.post('/users/register', data)
                alert('Registrasi berhasil, silakan login!')
                router.push('/')
            } catch (err) {
                const msg = err.response?.data?.error || 'Registrasi gagal. Periksa kembali input Anda.'
                alert(msg)
                console.error('Registrasi error:', err)
            }
        },
        logout() {
            this.user = null
            this.token = null
            localStorage.removeItem('token')
            localStorage.removeItem('user')
            router.push('/')
        },
    },
})