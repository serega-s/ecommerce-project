<template>
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <h2 class="uppercase">User Profile</h2>

        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="first_name">First Name</label>
            <input
              required
              type="text"
              name="first_name"
              v-model="first_name"
              placeholder="First Name"
              class="form-control"
            />
          </div>
          <div class="form-group">
            <label for="last_name">Last Name</label>
            <input
              required
              type="text"
              name="last_name"
              v-model="last_name"
              placeholder="Last Name"
              class="form-control"
            />
          </div>
          <div class="form-group">
            <label for="last_name">Email</label>
            <input
              required
              type="email"
              name="username"
              v-model="username"
              placeholder="Email"
              class="form-control"
            />
          </div>
          <div class="form-group">
            <label for="current_password">Current Password</label>
            <input
              type="password"
              name="current_password"
              v-model="current_password"
              placeholder="Current Password"
              title="If you leave password fields blank, password will not update!"
              class="form-control"
            />
          </div>
          <div class="form-group">
            <label for="password">New Password</label>
            <input
              type="password"
              name="new_password"
              v-model="new_password"
              placeholder="Password"
              title="If you leave password fields blank, password will not update!"
              class="form-control"
            />
          </div>
          <div class="form-group">
            <label for="password2">Repeat New Password</label>
            <input
              type="password"
              v-model="re_new_password"
              placeholder="Repeat Password"
              title="If you leave password fields blank, password will not update!"
              class="form-control"
            />
          </div>
          <br />
          <button type="submit" class="btn btn-dark">Update</button>

          <div class="form-group">
            <br />
            <div class="alert alert-danger" v-if="errors.length">
              <p v-for="error in errors" :key="error">{{ error }}</p>
            </div>
          </div>
        </form>
      </div>
      <div class="col-md-9">
        <h2 class="uppercase">My Orders</h2>
        <div class="table-responsive">
          <table class="table-sm table table-striped">
            <thead>
              <tr>
                <th>ID</th>
                <th>Date</th>
                <th>Total</th>
                <th>Paid</th>
                <th>Delivered</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="order,i in orders" :key="order.id">
                <td><b>#</b>{{ i + 1 }}</td>
                <td>{{ order.created_at }}</td>
                <td>${{ order.total_price }}</td>
                <td><span v-if="order.is_paid ===  false">Not Paid</span><span v-else>Paid</span></td>
                <td><span v-if="order.is_delivered ===  false">Not Delivered</span><span v-else>Delivered</span></td>
                <td><router-link :to="{name: 'Order', params: {id: order.id}}" class="btn btn-dark">Details</router-link></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "Profile",
  data() {
    return {
      username: "",
      first_name: "",
      last_name: "",
      current_password: "",
      new_password: "",
      re_new_password: "",
      errors: [],
      orders: [],
    }
  },
  mounted() {
    this.getUser()
    this.getMyOrders()
  },
  methods: {
    async getUser() {
      this.$store.commit("setIsLoading", true)
      await axios
        .get("/api/v1/users/me/")
        .then((response) => {
          console.log(response.data)
          this.first_name = response.data.first_name
          this.last_name = response.data.last_name
          this.username = response.data.username
        })
        .catch((error) => {
          console.log(error.response)
        })
      this.$store.commit("setIsLoading", false)
    },
    async submitForm() {
      this.$store.commit("setIsLoading", true)

      this.errors = []

      const formData = {
        username: this.username,
        first_name: this.first_name,
        last_name: this.last_name,
      }
      await axios
        .patch("/api/v1/users/me/", formData)
        .then((response) => {
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else if (error.message) {
            this.errors.push("Something went wrong. Please try again!")
          }
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

          this.$router.push({ name: "Profile" })
        })
        .catch((error) => {
          console.log(error.response)
        })
      if (this.new_password && this.re_new_password && this.current_password) {
        if (this.new_password !== this.re_new_password) {
          this.errors.push("Passwords did not match!")
          return
        }
        const passwordData = {
          new_password: this.new_password,
          re_new_password: this.re_new_password,
          current_password: this.current_password,
        }

        await axios
          .post("/api/v1/users/set_password/", passwordData)
          .then((response) => {
          })
          .catch((error) => {
            console.log(error.response)

            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                )
              }
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again!")
            }
          })
      }
      this.$store.commit("setIsLoading", false)
    },
    async getMyOrders() {
      this.$store.commit("setIsLoading", true)

      await axios
        .get("/api/v1/my-orders/")
        .then((response) => {
          this.orders = response.data
        })
        .catch((error) => {
          console.log(error.response)
        })

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>

<style>
.table {
  width: 100%;
  margin-bottom: 1rem;
  color: #55595c;
}
table {
  display: table;
  border-collapse: separate;
  box-sizing: border-box;
  text-indent: initial;
  border-spacing: 2px;
  border-color: grey;
}
.table thead th {
  vertical-align: bottom;
  border-bottom: 2px solid rgba(0, 0, 0, 0.05) !important;
}

.table td,
.table th {
  padding: 1.5rem;
}
.table-sm td,
.table-sm th {
  padding: 0.3rem;
}
.table td,
.table th {
  padding: 0.75rem;
  vertical-align: top;
  border-top: 1px solid rgba(0, 0, 0, 0.05);
}
th {
  font-size: 0.765625rem;
  text-transform: uppercase;
}
</style>
