<template>
  <div class="container">
    <!-- <button type="button" class="btn btn-outline-light my-3" onclick="javascript:history.go(-1)">Go Back</button> -->
    <div>
      <h1>Order:</h1>
      <div class="row">
        <div class="col-md-8">
          <div class="list-group list-group-flush">
            <div class="list-group-item">
              <h2>Shipping</h2>
              <p>
                <strong>Name: {{ order.user.full_name }}</strong>
              </p>
              <p>
                <strong>Email: </strong><a href="">{{ order.user.username }}</a>
              </p>
              <p>
                <strong>Shipping: </strong>{{ order.shipping.country }},
                {{ order.shipping.address }}, {{ order.shipping.postal_code }},
                {{ order.shipping.phone }},
              </p>

              <div
                role="alert"
                class="fade alert alert-success show"
                v-if="order.delivery_status === 'Delivered'"
              >
                {{ order.delivery_status }}
              </div>
              <div
                role="alert"
                class="fade alert alert-info show"
                v-else-if="order.delivery_status !== 'Not Delivered'"
              >
                {{ order.delivery_status }}
              </div>
              <div role="alert" class="fade alert alert-warning show" v-else>
                {{ order.delivery_status }}
              </div>
            </div>

            <div class="list-group-item">
              <h2>Payment Method</h2>
              <p><strong>Method: </strong>{{ order.paymentMethod }}</p>
              <div
                role="alert"
                class="fade alert alert-success show"
                v-if="order.is_paid"
              >
                Paid
              </div>
              <div role="alert" class="fade alert alert-warning show" v-else>
                Not Paid
              </div>
            </div>

            <div class="list-group-item">
              <h2>Order Items</h2>
              <div class="list-group list-group-flush">
                <div
                  class="list-group-item"
                  v-for="item in order.orderitems"
                  :key="item.id"
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
                  <div class="col">{{ order.get_items_total }} pcs</div>
                </div>
              </div>
              <div class="list-group-item">
                <div class="row">
                  <div class="col">Shipping:</div>
                  <div class="col">${{ order.shipping_price }}</div>
                </div>
              </div>
              <div class="list-group-item">
                <div class="row">
                  <div class="col">Total:</div>
                  <div class="col">${{ order.get_price_total }}</div>
                </div>
              </div>
              <div class="list-group-item">
                <button
                  type="button"
                  class="btn btn-dark"
                  disabled
                  v-if="order.is_paid"
                >
                  Paid Successfully
                </button>
                <button
                  type="button"
                  class="btn btn-dark"
                  @click="confirmOrder"
                  v-else
                >
                  Order
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
  name: "Order",
  mounted() {
    document.title = "Order | Shop"
    this.getOrder()
  },
  data() {
    return {
      order: {
        user: {},
        shipping: {},
      },
    }
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
    async getOrder() {
      this.$store.commit("setIsLoading", true)
      const orderID = this.$route.params.id

      await axios
        .get(`/api/v1/orders/${orderID}/`)
        .then((response) => {
          console.log(response.data)
          this.order = response.data
        })
        .catch((error) => {
          console.log(error.response)
        })
      this.$store.commit("setIsLoading", false)
    },
    async confirmOrder() {
      this.$store.commit("setIsLoading", true)
      const orderID = this.$route.params.id

      await axios
        .post(`/api/v1/orders/confirm-order/${orderID}/`)
        .then((response) => {
          console.log(response.data)
          this.getOrder()
        })
      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>

<style></style>
