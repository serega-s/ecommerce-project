<script>
export default {
  data: {
    cart: {
      items: [],
    },
  },
  mounted() {
    this.cart = this.$store.state.cart
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
