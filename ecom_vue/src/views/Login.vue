<template>
  <div class="container">
    <div class="container">
      <div class="justify-content-md-center row">
        <div class="col-md-6 col-12">
          <h1 class="title uppercase">Sign In</h1>
          <form class="form" @submit.prevent="submitForm">
            <div class="form-group">
              <label class="form-label" for="username">Email</label
              ><input
                placeholder="Email"
                type="email"
                name="username"
                class="form-control"
                v-model="username"
              />
            </div>
            <div class="form-group">
              <label class="form-label" for="password">Password</label
              ><input
                placeholder="Password"
                type="password"
                id="password"
                class="form-control"
                v-model="password"
              />
            </div>
            <br />
            <button type="submit" class="btn btn-dark">Sign In</button>
          </form>
          <div class="py-3 row">
            <div class="col">
              New Customer?
              <router-link class="underline" :to="{ name: 'SignUp' }">Register</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    }
  },
  mounted() {
    document.title = 'Log In | Shop'
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)
      axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem("token")

      const formData = {
        username: this.username,
        password: this.password,
      }

      await axios
        .post("/api/v1/token/login", formData)
        .then((response) => {
          const token = response.data.auth_token

          this.$store.commit("setToken", token)
          axios.defaults.headers.common["Authorization"] = "Token " + token

          localStorage.setItem("token", token)
        })
        .catch((error) => {
          console.log(error.response)
        })

      await axios
        .get("/api/v1/users/me/")
        .then((response) => {
          this.$store.commit("setUser", {
            username: response.data.username,
            id: response.data.id,
            first_name: response.data.first_name,
            last_name: response.data.last_name,
          })

          localStorage.setItem("username", response.data.username)
          localStorage.setItem("userid", response.data.id)
          localStorage.setItem("first_name", response.data.first_name)
          localStorage.setItem("last_name", response.data.last_name)

          this.$router.push("/")
        })
        .catch((error) => {
          console.log(error.response)
        })
      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>

<style></style>
