import { createStore } from "vuex"

export default createStore({
  state: {
    isLoading: false,
    user: {
      id: "",
      username: "",
      email: "",
      first_name: "",
      last_name: "",
    },
    shippingInfo: {
      address: "",
      phone: "",
      postal_code: "",
      city: "",
      country: "",
    },
    cart: {
      items: [],
    },
    isAuthenticated: false,
    token: "",
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("cart")) {
        state.cart = JSON.parse(localStorage.getItem("cart"))
      } else {
        localStorage.setItem("cart", JSON.stringify(state.cart))
      }

      if (localStorage.getItem("token")) {
        state.token = localStorage.getItem("token")
        state.isAuthenticated = true
        state.user.username = localStorage.getItem("username")
        state.user.id = localStorage.getItem("userid")
        state.user.first_name = localStorage.getItem("first_name")
        state.user.last_name = localStorage.getItem("last_name")
        state.user.email = localStorage.getItem("useremail")
        state.shippingInfo.address = localStorage.getItem("address")
        state.shippingInfo.postalcode = localStorage.getItem("postalcode")
        state.shippingInfo.city = localStorage.getItem("city")
        state.shippingInfo.country = localStorage.getItem("country")
        state.shippingInfo.phone = localStorage.getItem("phone")
      } else {
        state.user.id = ""
        state.user.username = ""
        state.token = ""
        state.user.email = ""
        state.user.first_name = ""
        state.user.last_name = ""
        state.isAuthenticated = false
        state.shippingInfo.address = ""
        state.shippingInfo.phone = ""
        state.shippingInfo.postalcode = ""
        state.shippingInfo.city = ""
        state.shippingInfo.country = ""
      }
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(
        (i) => i.product.id === item.product.id
      )
      if (exists.length) {
        exists[0].length =
          parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        state.cart.items.push(item)
      }

      localStorage.setItem("cart", JSON.stringify(state.cart))
    },
    clearCart(state) {
      state.cart = { items: [] }
      localStorage.setItem("cart", JSON.stringify(state.cart))
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.user.id = ""
      state.user.username = ""
      state.user.email = ""
      state.user.first_name = ""
      state.user.last_name = ""
      state.shippingInfo.address = ""
      state.shippingInfo.phone = ""
      state.shippingInfo.city = ""
      state.shippingInfo.country = ""
      state.shippingInfo.postalcode = ""
      state.token = ""
      state.isAuthenticated = false
    },
    setUser(state, user) {
      state.user = user
    },
    setShipInfo(state, info) {
      state.shippingInfo = info
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
  },
  actions: {},
  modules: {},
})
