<template>
  <div class="container">
    <div>
      <NavItem :active="3" />
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
      </div> -->
      <div class="row">
        <div class="col-md-8">
          <div class="list-group list-group-flush">
            <div class="list-group-item">
              <h2>Shipping</h2>
              <p>
                <strong>Shipping: </strong>
                {{ shippingInfo.country }}, {{ shippingInfo.address }},
                {{ shippingInfo.postal_code }},
                {{ shippingInfo.phone }}
              </p>
            </div>
            <div class="list-group-item">
              <h2>Payment Method</h2>
              <p><strong>Method: </strong>{{ paymentMethod }}</p>
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
              <div class="list-group-item uppercase">
                <h2>Order Summary</h2>
              </div>
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
import NavItem from "@/components/NavItem.vue"

import axios from "axios"
import cartComputed from "@/mixins/cartComputed.vue"
export default {
  name: "Placeorder",
  data() {
    return {
      paymentMethod: "Credit Card",
      shippingInfo: JSON.parse(localStorage.getItem("shippingInfo")),
      shipping_price: 0,
    }
  },
  mixins: [cartComputed],
  components: {NavItem},
  mounted() {
    document.title = "Placeorder | Shop"
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
          price: parseFloat(item.product.price * item.quantity).toFixed(2),
        }

        items.push(obj)
      }
      this.cartTotalPrice < 100 && this.cartTotalLength < 2
        ? (this.shipping_price = 5.0)
        : (this.shipping_price = 0.0)

      const formData = {
        orderitems: items,
        paymentMethod: this.paymentMethod,
        shipping_price: this.shipping_price,
        total_price: this.cartTotalPrice,
        address: this.shippingInfo.address,
        phone: this.shippingInfo.phone,
        city: this.shippingInfo.city,
        postal_code: this.shippingInfo.postal_code,
        country: this.shippingInfo.country,
      }

      await axios
        .post("/api/v1/orders/add_order_items/", formData)
        .then((response) => {
          this.$store.commit("clearCart")
          localStorage.removeItem("shippingInfo")
          this.$router.push({ name: "Order", params: { id: response.data.id } })
        })
        .catch((error) => {
          console.log(error.response)
          this.$router.push({ name: "Cart" })
        })

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>

<style lang="scss">
.active {
  color: black;
}
</style>
