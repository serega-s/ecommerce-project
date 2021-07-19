import axios from "axios"
import "bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"
import { createApp } from "vue"
import "../node_modules/bootstrap-icons/font/bootstrap-icons.css"
import App from "./App.vue"
import router from "./router"
import store from "./store"

axios.defaults.baseURL = "http://127.0.0.1:8000"
createApp(App)
  .use(store)
  .use(router, axios)
  .mount("#app")
