<template>
  <div class="container">
    <div class="justify-content-md-center row">
      <div class="col-md-6 col-12">
        <NavItem :active="2" />
        <!-- <div class="justify-content-center mb-4 nav">
          <div class="nav-item">
            <router-link
              to="/"
              class="nav-link active"
              role="button"
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
              class="nav-link disabled"
              :to="{ name: 'Placeorder' }"
              role="button"
              tabindex="3"
              >Place Order</router-link
            >
          </div>
        </div> -->
        <form class="">
          <div class="form-group">
            <legend class="form-label">Select Method</legend>
            <div class="col">
              <div class="form-check">
                <input
                  name="paymentMethod"
                  type="radio"
                  class="form-check-input"
                  checked=""
                /><label title="Credit Card" for="paypal" class="form-check-label"
                  >Credit Card</label
                >
              </div>
            </div>
          </div>
          <br />
          <button
            @click.prevent="$router.push({ name: 'Placeorder' })"
            type="submit"
            class="btn btn-dark"
          >
            Continue
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Payment",
  data() {
    return {
      paymentActive: true,
      shippingActive: false,
      placeorderActive: false,
    }
  },
  mounted() {
    document.title = "Payment | Shop"
  },
}
</script>