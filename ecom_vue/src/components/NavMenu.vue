<template>
  <div class="justify-content-center mb-4 nav">
    <div class="nav-item">
      <router-link
        to="/"
        class="nav-link"
        role="button"
        tabindex="1"
        :class="{ active: shippingActive }"
        >Shipping</router-link
      >
    </div>
    <div class="nav-item">
      <router-link
        :to="{name: 'Payment'}"
        class="nav-link"
        :class="{ active: paymentActive }"
        role="button"
        tabindex="2"
        >Payment</router-link
      >
    </div>
    <div class="nav-item">
      <router-link
        class="nav-link"
        :to="{name: 'Placeorder'}"
        :class="{ active: placeorderActive }"
        role="button"
        tabindex="3"
        >Place Order</router-link
      >
    </div>
  </div>
</template>

<script>
export default {
  props: {
    shippingActive: Boolean,
    paymentActive: Boolean,
    placeorderActive: Boolean,
  },
}
</script>

<style></style>
