<template>
  <div class="justify-content-center mb-4 nav">
    <template v-if="this.active == 1">
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
    </template>
    <template v-else-if="this.active == 2">
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
          class="nav-link disabled"
          :to="{ name: 'Placeorder' }"
          role="button"
          tabindex="3"
          >Place Order</router-link
        >
      </div>
    </template>
    <template v-else-if="this.active == 3">
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
    </template>
    <!-- <div class="nav-item">
      <router-link
        :to="{ name: 'Shipping' }"
        class="nav-link"
        :class="{ 'active': this.active == 1 }"
        tabindex="1"
        >Shipping</router-link
      >
    </div>
    <div class="nav-item">
      <router-link
        :to="{ name: 'Payment' }"
        class="nav-link"
        :class="{ 'active': this.active == 2 }"
        role="button"
        tabindex="2"
        >Payment</router-link
      >
    </div>
    <div class="nav-item">
      <router-link
        class="nav-link"
        :class="{ 'active': this.active == 3 }"
        :to="{ name: 'Placeorder' }"
        role="button"
        tabindex="3"
        >Place Order</router-link
      >
    </div> -->
  </div>
</template>

<script>
export default {
  props: ["active"],
}
</script>

<style></style>
