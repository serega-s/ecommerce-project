<template>
  <div class="container">
    <div>
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
            class="nav-link active"
            role="button"
            tabindex="2"
            >Payment</router-link
          >
        </div>
        <div class="nav-item">
          <router-link
            class="nav-link active"
            :to="{ name: 'Placeorder' }"
            role="button"
            tabindex="3"
            >Place Order</router-link
          >
        </div>
      </div>
      <div class="row">
        <div class="col-md-8">
          <div class="list-group list-group-flush">
            <div class="list-group-item">
              <h2>Shipping</h2>
              <p>
                <strong>Shipping: </strong
                >{{ $store.state.shippingInfo.country }},
                {{ $store.state.shippingInfo.address }},
                {{ $store.state.shippingInfo.postalcode }}
              </p>
            </div>
            <div class="list-group-item">
              <h2>Payment Method</h2>
              <p><strong>Method: </strong>PayPal</p>
            </div>
            <div class="list-group-item">
              <h2>Order Items</h2>
              <div class="list-group list-group-flush">
                <div
                  class="list-group-item"
                  v-for="item in cart.items"
                  :key="item.product.id"
                >
                  <div class="row">
                    <div class="col-md-1">
                      <img
                        :src="item.product.get_image"
                        class="img-fluid rounded"
                      />
                    </div>
                    <div class="col">
                      <router-link
                        class="underline"
                        :to="{
                          name: 'Product',
                          params: { id: item.product.id },
                        }"
                        >{{ item.product.name }}</router-link
                      >
                    </div>
                    <div class="col-md-4">
                      {{ item.quantity }} X {{ item.product.price }} = ${{
                        getItemTotal(item).toFixed(2)
                      }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card">
            <div class="list-group list-group-flush">
              <div class="list-group-item uppercase"><h2>Order Summary</h2></div>
              <div class="list-group-item">
                <div class="row">
                  <div class="col">Items:</div>
                  <div class="col">{{ cartTotalLength }} pcs</div>
                </div>
              </div>
              <div class="list-group-item">
                <div class="row">
                  <div class="col">Shipping:</div>
                  <div
                    class="col"
                    v-if="cartTotalPrice < 100 && cartTotalLength < 2"
                  >
                    $5.00
                  </div>
                  <div class="col" v-else>$0.00</div>
                </div>
              </div>
              <div class="list-group-item">
                <div class="row">
                  <div class="col">Total:</div>
                  <div class="col">${{ cartTotalPrice }}</div>
                </div>
              </div>
              <div class="list-group-item">
                <button type="button" class="btn btn-dark" @click="placeOrder">
                  Place Order
                </button>
              </div>
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
  name: "Placeorder",
  data() {
    return {
      cart: {
        items: [],
      },
      paymentMethod: "Credit Card",

      shipping_price: 0,
    }
  },
  mounted() {
    document.title = "Placeorder | Shop"

    this.cart = this.$store.state.cart
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
    async placeOrder() {
      this.$store.commit("setIsLoading", true)

      const items = []

      for (let i = 0; i < this.cart.items.length; i++) {
        const item = this.cart.items[i]
        const obj = {
          product: item.product.id,
          quantity: item.quantity,
          price: item.product.price * item.quantity,
        }

        items.push(obj)
      }

      if (this.cartTotalPrice < 100 && this.cartTotalLength < 2) {
        this.shipping_price = 5.0
      } else {
        this.shipping_price = 0.0
      }

      const formData = {
        order_items: items,
        paymentMethod: this.paymentMethod,
        shipping_price: this.shipping_price,
        total_price: this.cartTotalPrice,
        address: this.$store.state.shippingInfo.address,
        phone: this.$store.state.shippingInfo.phone,
        city: this.$store.state.shippingInfo.city,
        postal_code: this.$store.state.shippingInfo.postalcode,
        country: this.$store.state.shippingInfo.country,
      }

      await axios
        .post("/api/v1/products/add_order_items/", formData)
        .then((response) => {
          console.log(response.data)
          this.$store.commit("clearCart")
          this.$router.push("/")

          console.log("SHIPPING_PRICE:", this.shipping_price)
        })
        .catch((error) => {
          console.log(error.response)
        })

      this.$store.commit("setIsLoading", false)
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
        return parseFloat((acc += curVal.product.price * curVal.quantity))
      }, 0)
    },
  },
}
</script>

<style lang="scss">
.active {
  color: black;
}
</style>
