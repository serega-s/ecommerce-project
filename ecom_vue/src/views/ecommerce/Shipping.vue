<template>
  <div class="container">
    <div class="container">
      <div class="justify-content-md-center row">
        <div class="col-md-6 col-12">
          <!-- <div class="justify-content-center mb-4 nav">
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
          </div> -->
          <NavItem :active="1" />
          <h1>Shipping</h1>
          <form @submit.prevent="submitForm">
            <div class="form-group">
              <label class="form-label" for="address">Phone</label
              ><input
                required
                placeholder="Enter phone"
                type="number"
                class="form-control"
                v-model="shippingInfo.phone"
              />
            </div>
            <div class="form-group">
              <label class="form-label" for="address">Address</label
              ><input
                required
                placeholder="Enter address"
                type="text"
                class="form-control"
                v-model="shippingInfo.address"
              />
            </div>
            <div class="form-group">
              <label class="form-label" for="city">City</label
              ><input
                required=""
                placeholder="Enter city"
                type="text"
                class="form-control"
                v-model="shippingInfo.city"
              />
            </div>
            <div class="form-group">
              <label class="form-label" for="postalCode">Postal Code</label
              ><input
                required
                placeholder="Enter postal code"
                type="text"
                class="form-control"
                v-model="shippingInfo.postal_code"
              />
            </div>
            <div class="form-group">
              <label class="form-label" for="country">Country</label
              ><input
                required
                placeholder="Enter country"
                type="text"
                class="form-control"
                v-model="shippingInfo.country"
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
import NavItem from '@/components/NavItem.vue'
export default {
  name: "Shipping",
  data() {
    return {
      shippingInfo: {
        phone: "",
        address: "",
        postal_code: "",
        city: "",
        country: "",
      },
      errors: [],
    }
  },
  components: {NavItem},
  mounted() {
    document.title = "Shipping | Shop"

    this.cart = this.$store.state.cart
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
    submitForm() {
      this.errors = []

      if (this.shippingInfo.phone === "") {
        this.errors.push("The phone field is missing!")
      } else if (this.shippingInfo.address === "") {
        this.errors.push("The address field is missing!")
      } else if (this.shippingInfo.postal_code === "") {
        this.errors.push("The postal code field is missing!")
      } else if (this.shippingInfo.city === "") {
        this.errors.push("The city field is missing!")
      } else if (this.shippingInfo.country === "") {
        this.errors.push("The country field is missing!")
      }

      if (!this.errors.length) {
        this.$store.commit("setIsLoading", true)

        localStorage.setItem("shippingInfo", JSON.stringify(this.shippingInfo))

        this.$router.push({ name: "Payment" })

        this.$store.commit("setIsLoading", false)
      }
    },
  },
}
</script>
