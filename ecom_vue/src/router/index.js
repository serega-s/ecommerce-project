import { createRouter, createWebHistory } from "vue-router"
import store from "../store"
import Cart from "../views/ecommerce/Cart.vue"
import Payment from "../views/ecommerce/Payment.vue"
import Placeorder from "../views/ecommerce/Placeorder.vue"
import Order from "../views/ecommerce/Order.vue"
import Product from "../views/ecommerce/Product.vue"
import Profile from "../views/ecommerce/Profile.vue"
import Search from "../views/ecommerce/Search.vue"
import Shipping from "../views/ecommerce/Shipping.vue"
import Home from "../views/Home.vue"
import Login from "../views/Login.vue"
import SignUp from "../views/SignUp.vue"

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUp,
  },

  {
    path: "/product/:id",
    name: "Product",
    component: Product,
  },
  {
    path: "/cart",
    name: "Cart",
    component: Cart,
  },
  {
    path: "/search",
    name: "Search",
    component: Search,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/shipping",
    name: "Shipping",
    component: Shipping,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/payment",
    name: "Payment",
    component: Payment,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/placeorder",
    name: "Placeorder",
    component: Placeorder,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: '/order/:id',
    name: 'Order',
    component: Order,
    meta: {
      requireLogin: true
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !store.state.isAuthenticated
  ) {
    next({ name: "Login", query: { to: to.path } })
  } else {
    next()
  }
})

export default router
