import { isAuthenticated } from '@/services/auth.service';
import { createRouter, createWebHistory } from 'vue-router'

const LoginView = () => import('@/views/auth/LoginView.vue');
const RegisterView = () => import('@/views/auth/RegisterView.vue');
const MainView = () => import('@/views/MainView.vue');

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/login',
            name: 'login',
            component: LoginView,
            beforeEnter: (to, from, next) => {
                if (!isAuthenticated())
                {
                    next();
                } else
                {
                    next('/')
                }
            }
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterView,
            beforeEnter: (to, from, next) => {
                if (!isAuthenticated())
                {
                    next();
                } else
                {
                    next('/')
                }
            }
        },
        {
            path: '/',
            name: 'home',
            component: MainView,
            beforeEnter: (to, from, next) => {
                if (isAuthenticated())
                {
                    next();
                } else
                {
                    next('/login')
                }
            }
        },
        {
            path: '/:pathMatch(.*)*',
            redirect: '/',
        },
        
    ]
});

export default router;