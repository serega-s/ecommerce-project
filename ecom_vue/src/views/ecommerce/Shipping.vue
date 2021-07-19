<template>
  <div class="container">
    <div class="container">
      <div class="justify-content-md-center row">
        <div class="col-md-6 col-12">
          <div class="justify-content-center mb-4 nav">
            <div class="nav-item">
              <router-link
                :to="{ name: 'Shipping' }"
                class="active nav-link"
                tabindex="1"
                >Shipping</router-link
              >
            </div>
            <div class="nav-item">
              <router-link
                :to="{ name: 'Payment' }"
                class="nav-link disabled"
                role="button"
                tabindex="2"
                aria-disabled="true"
                >Payment</router-link
              >
            </div>
            <div class="nav-item">
              <router-link
                :to="{ name: 'Placeorder' }"
                class="nav-link disabled"
                role="button"
                tabindex="3"
                aria-disabled="true"
                >Place Order</router-link
              >
            </div>
          </div>
          <h1>Shipping</h1>
          <form @submit.prevent="submitForm">
            <div class="form-group">
              <label class="form-label" for="address">Phone</label
              ><input
                required
                placeholder="Enter phone"
                type="number"
                class="form-control"
                v-model="phone"
              />
            </div>
            <div class="form-group">
              <label class="form-label" for="address">Address</label
              ><input
                required
                placeholder="Enter address"
                type="text"
                class="form-control"
                v-model="address"
              />
            </div>
            <div class="form-group">
              <label class="form-label" for="city">City</label
              ><input
                required=""
                placeholder="Enter city"
                type="text"
                class="form-control"
                v-model="city"
              />
            </div>
            <div class="form-group">
              <label class="form-label" for="postalCode">Postal Code</label
              ><input
                required
                placeholder="Enter postal code"
                type="text"
                class="form-control"
                v-model="postalcode"
              />
            </div>
            <div class="form-group">
              <label class="form-label" for="country">Country</label
              ><input
                required
                placeholder="Enter country"
                type="text"
                class="form-control"
                v-model="country"
              />
            </div>
            <br />
            <button type="submit" class="btn btn-dark">
              Continue
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Shipping",
  data() {
    return {
      phone: "",
      address: "",
      postalcode: "",
      city: "",
      country: "",
      errors: [],
    }
  },
  mounted() {
    document.title = "Shipping | Djackets"

    this.cart = this.$store.state.cart
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
    submitForm() {
      this.errors = []
      localStorage.removeItem("address")
      localStorage.removeItem("postalcode")
      localStorage.removeItem("city")
      localStorage.removeItem("phone")
      localStorage.removeItem("country")

      if (this.phone === "") {
        this.errors.push("The phone field is missing!")
      }

      if (this.address === "") {
        this.errors.push("The address field is missing!")
      }

      if (this.postalcode === "") {
        this.errors.push("The postal code field is missing!")
      }

      if (this.city === "") {
        this.errors.push("The city field is missing!")
      }

      if (this.country === "") {
        this.errors.push("The country field is missing!")
      }

      if (!this.errors.length) {
        this.$store.commit("setIsLoading", true)

        this.$store.commit("setShipInfo", {
          address: this.address,
          phone: this.phone,
          postalcode: this.postalcode,
          city: this.city,
          country: this.country,
        })

        localStorage.setItem("address", this.address)
        localStorage.setItem("postalcode", this.postalcode)
        localStorage.setItem("phone", this.phone)
        localStorage.setItem("city", this.city)
        localStorage.setItem("country", this.country)

        this.$router.push({ name: "Payment" })

        this.$store.commit("setIsLoading", false)
      }
    },
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return parseInt((acc += parseInt(curVal.quantity)))
      }, 0)
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return parseInt((acc += curVal.product.price * curVal.quantity))
      }, 0)
    },
  },
}
</script>
