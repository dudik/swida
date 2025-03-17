import { createRouter, createWebHistory } from 'vue-router'
import OrderList from '../views/OrderList.vue'
import OrderForm from '../views/OrderForm.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'order-list',
      component: OrderList,
    },
    {
      path: '/order-form',
      name: 'order-form',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: OrderForm,
    },
  ],
})

export default router
