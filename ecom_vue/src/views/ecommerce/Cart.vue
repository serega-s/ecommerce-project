<template>
  <div class="container">
    <div class="row">
      <div class="col-md-8">
        <h1 class="uppercase">SHOPPING CART</h1>
        <div v-if="!cart.items.length">
          <div class="alert alert-secondary" role="alert">You cart is empty <router-link :to="{name: 'Home'}" class="underline">Go Back</router-link></div>
        </div>
        <div class="list-group list-group-flush">
          <div class="list-group-item">
            <CartItem
              v-for="item in cart.items"
              :key="item.product.id"
              :initialItem="item"
              @removeFromCart="removeFromCart"
            />
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="list-group list-group-flush">
            <div class="list-group-item">
              <h2 class="uppercase">Total ({{ cartTotalLength }})</h2>
              ${{ cartTotalPrice.toFixed(2) }}
            </div>
          </div>
          <div class="list-group-item">
            <router-link
              :to="{ name: 'Shipping' }"
              v-if="cartTotalLength"
              type="button"
              class="btn btn-dark"
            >
              Proceed to checkout
            </router-link>
            <button class="btn btn-dark" disabled v-else>
              Proceed to checkout
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CartItem from "@/components/CartItem"
export default {
  name: "Cart",
  data() {
    return {
      cart: {
        items: [],
      },
    }
  },
  mounted() {
    this.cart = this.$store.state.cart

    document.title = `Cart (${this.cartTotalLength || 0}) | Shop)`
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(
        (i) => i.product.id !== item.product.id
      )
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

  components: {
    CartItem,
  },
}
</script>

<style>
.box-element {
  box-shadow: hsl(0, 0%, 80%) 0 0 16px;
  background-color: #fff;
  border-radius: 4px;
  padding: 10px;
}

.product {
  border-radius: 0 0 4px 4px;
}

#cart-icon {
  width: 25px;
  display: inline-block;
  margin-left: 15px;
}

#cart-total {
  display: inline-block;
  text-align: center;
  color: #fff;
  background-color: red;
  width: 20px;
  height: 22px;
  margin: 0 0 -20px -9px;
  border-radius: 50%;
  font-size: 14px;
}

.row-image {
  width: 100px;
}

.form-field {
  width: 250px;
  display: inline-block;
  padding: 5px;
}

.cart-row {
  display: flex;
  align-items: flex-stretch;
  padding-bottom: 10px;
  margin-bottom: 10px;
  border-bottom: 1px solid #ececec;
}

.quantity {
  display: inline-block;
  font-weight: 700;
  padding-right: 10px;
}

.chg-quantity {
  width: 12px;
  cursor: pointer;
  display: block;
  margin-top: 5px;
  transition: 0.1s;
}

.chg-quantity:hover {
  opacity: 0.6;
}

.hidden {
  display: none !important;
}

.align-items-center {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
