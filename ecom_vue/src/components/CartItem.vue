<template>
  <div class="row">
    <div class="col-md-2">
      <!-- {{item}} -->
      <img :src="item.product.get_image" class="img-fluid rounded" />
    </div>
    <div class="col-md-3">
      <router-link
        class="underline"
        :to="{ name: 'Product', params: { id: item.product.id } }"
        >{{ item.product.name }}</router-link
      >
    </div>
    <div class="col-md-3">${{ item.product.price }}</div>
    <div class="col-md-3">
      {{ item.quantity }}pcs
      <!-- <br /> -->
      <a class="" @click="incrementQuantity(item)" style="cursor: pointer;padding: 3px; margin: 0;"
        ><i class="bi bi-plus"></i
      ></a>
      <a class="" @click="decrementQuantity(item)" style="cursor: pointer;padding: 3px; margin: 0;"
        ><i class="bi bi-dash"></i
      ></a>
    </div>
    <div class="col-md-1">
      <a type="button" class="btn btn-light" href="#" @click="removeFromCart(item)">
        <i class="bi bi-trash"></i>
      </a>
    </div>
    <hr />
  </div>
</template>

<script>
export default {
  name: "CartItem",
  props: {
    initialItem: Object,
  },
  data() {
    return {
      item: this.initialItem,
    }
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
    decrementQuantity(item) {
      item.quantity -= 1
      if (item.quantity === 0) {
        this.$emit("removeFromCart", item)
      }
      this.updateCart()
    },
    incrementQuantity(item) {
      item.quantity += parseInt(1)
      this.updateCart()
    },
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart))
    },
    removeFromCart(item) {
      this.$emit("removeFromCart", item)
      this.updateCart()
    },
  },
}
</script>
