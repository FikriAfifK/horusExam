import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../store/auth'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Dashboard from '../views/Dashboard.vue'
import UpdateUser from '../views/UpdateUser.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', name: 'Login', component: Login },
        { path: '/register', name: 'Register', component: Register },
        { path: '/dashboard', name: 'Dashboard', component: Dashboard, meta: { requiresAuth: true } },
        { path: '/update/:id', name: 'UpdateUser', component: UpdateUser, meta: { requiresAuth: true } },
        { path: '/:pathMatch(.*)*', redirect: '/' },
    ],
})

// Proteksi halaman yang butuh login
router.beforeEach((to, from, next) => {
    const auth = useAuthStore()

    const isLoggedIn = auth.isAuthenticated

    if (to.meta.requiresAuth && !isLoggedIn) {
        next({ path: '/', query: { redirect: to.fullPath } })
    } else if ((to.path === '/' || to.path === '/register') && isLoggedIn) {
        next('/dashboard')
    } else {
        next()
    }
})

export default router