<template>
  <div class="container">
    <div class="container">
      <div class="justify-content-md-center row">
        <div class="col-md-6 col-12">
          <h1 class="title uppercase">Sign Up</h1>
          <form class="form" @submit.prevent="submitForm">
            <div class="form-group">
              <label class="form-label" for="first_name">First Name</label
              ><input
                placeholder="First Name"
                type="text"
                name="first_name"
                class="form-control"
                v-model="first_name"
              />
            </div>
            <div class="form-group">
              <label class="form-label" for="last_name">Last Name</label
              ><input
                placeholder="Last Name"
                type="text"
                name="last_name"
                class="form-control"
                v-model="last_name"
              />
            </div>
            <div class="form-group">
              <label class="form-label" for="email">Email</label
              ><input
                placeholder="Email"
                type="email"
                name="username"
                class="form-control"
                v-model="username"
              />
            </div>
            <!-- <div class="form-group">
              <label class="form-label" for="email">Email Address</label
              ><input
                placeholder="Email"
                type="email"
                name="email"
                class="form-control"
                v-model="email"
              />
            </div> -->
            <div class="form-group">
              <label class="form-label" for="password">Password</label
              ><input
                placeholder="Password"
                type="password"
                name="password"
                class="form-control"
                v-model="password"
              />
            </div>
            <div class="form-group">
              <label class="form-label" for="password">Confirm Password</label
              ><input
                placeholder="Confirm Password"
                type="password"
                class="form-control"
                v-model="password2"
              />
            </div>
            <br />
            <button type="submit" class="btn btn-dark">Sign Up</button>
          </form>
          <div class="py-3 row">
            <div class="col">
              Have an Account?
              <router-link class="underline" :to="{ name: 'Login' }">Log in</router-link>
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
  name: "SignUp",
  data() {
    return {
      username: "",
      first_name: "",
      last_name: "",
      email: "",
      password: "",
      password2: "",
    }
  },
  mounted() {
    document.title = 'Sign Up | Shop'
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true)
      axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem("token")

      const formData = {
        first_name: this.first_name,
        last_name: this.last_name,
        username: this.username,
        password: this.password,
      }

      await axios
        .post("/api/v1/users/", formData)
        .then((response) => {
          console.log("success:", response.data)
        })
        .catch((error) => {
          console.log(error.response)
        })
      await axios
        .post("/api/v1/token/login/", formData)
        .then((response) => {
          const token = response.data.auth_token

          this.$store.commit("setToken", token)

          axios.defaults.headers.common["Authorization"] = "Token " + token

          localStorage.setItem("token", token)
        })
        .catch((error) => {
          console.log(error.response)
        })
      const fullName = {
        first_name: this.first_name,
        last_name: this.last_name,
      }
      await axios
        .patch("/api/v1/users/me/", fullName)
        .then((response) => {
          console.log(response.data)
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
