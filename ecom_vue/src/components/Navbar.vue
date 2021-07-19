<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <router-link class="navbar-brand uppercase" to="/">Shop</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link
              class="nav-link uppercase"
              :class="{ active: isActive == 1 }"
              @click="activateClass(1)"
              aria-current="page"
              to="/"
              ><i class="bi bi-house"></i> Home</router-link
            >
          </li>
          <li class="nav-item">
            <router-link
              :to="{ name: 'Cart' }"
              class="nav-link uppercase"
              :class="{ active: isActive == 2 }"
              @click="activateClass(2)"
              aria-current="page"
              href="#"
              ><i class="bi bi-cart"></i>&nbsp;Cart</router-link
            >
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <form class="d-flex" action="/search">
              <input
                class="search-control form-control me-2"
                type="search"
                name="query"
                placeholder="Search..."
                aria-label="Search"
              />
              <button
                class="btn search-control btn-outline-success"
                type="submit"
              >
                <i class="bi bi-search" aria-hidden="true"></i>
              </button>
            </form>
          </li>
        </ul>
        <ul class="navbar-nav">
          <template v-if="$store.state.isAuthenticated">
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle uppercase"
                href="#"
                id="navbarDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                <i class="bi bi-person"></i>&nbsp;{{
                  $store.state.user.first_name
                }}
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li>
                  <router-link
                    :to="{ name: 'Profile' }"
                    class="dropdown-item"
                    >Profile</router-link
                  >
                </li>
                <li>
                  <a class="dropdown-item" href="#" @click="logout">Log out</a>
                </li>
              </ul>
            </li>
          </template>
          <template v-else>
            <li class="nav-item">
              <router-link
                :to="{ name: 'Login' }"
                :class="{ active: isActive == 2 }"
                @click="activateClass(2)"
                class="nav-link uppercase"
                href="#"
                >Login</router-link
              >
            </li>
          </template>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import axios from "axios"

export default {
  name: "Navbar",
  data() {
    return {
      isActive: 0,
    }
  },
  methods: {
    activateClass(el) {
      this.isActive = el
    },
    async logout() {
      this.$store.commit("setIsLoading", true)
      await axios
        .post("/api/v1/token/logout/")
        .then((response) => {
          console.log("Logged out")
        })
        .catch((error) => {
          console.log(error.response)
        })

      axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem("token")
      localStorage.removeItem("username")
      localStorage.removeItem("userid")
      localStorage.removeItem("useremail")

      this.$store.commit("removeToken")

      this.$router.push({ name: "Login" })
      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>

<style>
.navbar {
  height: 80px;
  padding: 0 10rem;
}
.bg-dark {
  background: #343a40 !important;
}
.dropdown-item:focus,
.dropdown-item:active {
  background: #343a40;
  color: #fff;
}

.search-control {
  height: 50px !important;
}

@media (max-width: 996px) {
  .navbar {
    padding: 10px 0;
    height: auto;
  }
}
</style>
