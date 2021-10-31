<template>
  <div class="container">
    <div>
      <router-link class="btn-ib uppercase btn-outline-secondary my-3" to="/"
        ><i class="bi bi-arrow-left"></i> Go Back</router-link
      >
      <div>
        <div class="row">
          <div class="col-md-6">
            <img :src="product.get_image" class="img-fluid" />
          </div>
          <div class="col-md-3">
            <div class="list-group list-group-flush">
              <div class="list-group-item">
                <h3 class="uppercase">{{ product.name }}</h3>
              </div>
              <div class="list-group-item">
                <div class="rating">
                  <Rating :rating="Math.round(product.get_avg_rating)" />
                  &nbsp;
                  <span>{{ product.reviews.length || "No" }} reviews</span>
                </div>
              </div>
              <div class="list-group-item">Price: ${{ product.price }}</div>
              <div class="list-group-item">
                Description: {{ product.description }}
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="card">
              <div class="list-group list-group-flush">
                <div class="list-group-item">
                  <div class="row">
                    <div class="col">Price:</div>
                    <div class="col">
                      <strong>${{ product.price }}</strong>
                    </div>
                  </div>
                </div>
                <div class="list-group-item">
                  <div class="row">
                    <div class="col">Status:</div>
                    <div class="col">In Stock</div>
                  </div>
                </div>
                <div class="list-group-item">
                  <div class="row">
                    <div class="col">Count in Stock:</div>
                    <div class="col">{{ product.countInStock }}</div>
                  </div>
                </div>
                <div class="list-group-item">
                  <div class="row">
                    <div class="col">Qty:</div>
                    <div class="my-1 col-auto">
                      <input
                        type="number"
                        maxlength="2"
                        min="1"
                        :max="product.countInStock"
                        v-model="quantity"
                        class="form-control"
                        placeholder="Quantity..."
                      />
                    </div>
                  </div>
                </div>
                <div class="list-group-item">
                  <button
                    type="button"
                    v-if="product.is_available"
                    class="btn btn-dark"
                    @click="addToCart()"
                  >
                    Add to Cart
                  </button>
                  <div class="alert alert-danger" v-else>
                    Not In Stock
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6">
            <h4 class="uppercase">Reviews ({{ product.reviews.length }})</h4>

            <div class="list-group list-group-flush">
              <template v-if="$store.state.isAuthenticated">
              <div class="list-group-item">
                <div class="list-group-item">
                  <h4 class="uppercase">Leave a review</h4>

                  <div class="form-group">
                    <label class="form-label" for="rating">Rating</label
                    ><select v-model="rating" class="form-control"
                      ><option selected value="0">Select...</option
                      ><option value="1">1 - Poor</option
                      ><option value="2">2 - Fair</option
                      ><option value="3">3 - Good</option
                      ><option value="4">4 - Very Good</option
                      ><option value="5">5 - Excellent</option></select
                    >
                  </div>
                  <div class="form-group">
                    <label class="form-label" for="comment">Review</label
                    ><textarea
                      class="form-control"
                      v-model="comment"
                      style="height: 100px;"
                    ></textarea>
                  </div>
                  <br />
                  <button @click="addReview()" class="btn btn-dark">
                    Submit
                  </button>
                </div>
              </div>
              </template>
              <template v-else>
                <div class="alert alert-primary">You must <router-link class="underline" :to="{name: 'Login'}">log in</router-link>&nbsp;to leave a review!</div>
              </template>
              <div
                class="list-group-item"
                v-for="review in product.reviews"
                :key="review.id"
              >
                <strong>
                  {{ review.user.full_name }}
                </strong>
                <div class="rating">
                  <Rating :rating="review.rating" />
                </div>
                <p>{{ review.created_at }}</p>
                <p>{{ review.comment }}</p>
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

import Rating from "@/components/Rating.vue"
export default {
  name: "Product",
  components: {
    Rating,
  },
  data() {
    return {
      product: {
        reviews: [],
      },
      quantity: 1,
      rating: 0,
      comment: "",
      toast: {
        title: "",
        message: "",
      },
    }
  },
  mounted() {
    window.scrollTo(0, 0)
    this.getProduct()
  },
  methods: {
    addReview() {
      this.$store.commit("setIsLoading", true)

      const productID = this.$route.params.id

      if (this.rating > 0 && this.comment) {
        const formData = {
          rating: this.rating,
          comment: this.comment,
        }

        axios
          .post(`/api/v1/products/${productID}/add_comment/`, formData)
          .then((response) => {
            console.log(response.data)
            this.comment = ""
            this.rating = 0
            this.product.reviews = response.data.reviews
          })
          .catch((error) => {
            console.log(error.response)
          })
      }
      this.$store.commit("setIsLoading", false)
    },
    getProduct() {
      this.$store.commit("setIsLoading", true)
      const productID = this.$route.params.id
      axios
        .get(`/api/v1/products/${productID}`)
        .then((response) => {
          this.product = response.data
          this.product.reviews = response.data.reviews.reverse()

          document.title = `${this.product.name}, $${this.product.price} | Shop`
        })
        .catch((error) => {
          console.log(error.response)
        })
      this.$store.commit("setIsLoading", false)
    },
    addToCart() {
      if (this.product.countInStock < this.quantity) {
      } else {
        if (isNaN(this.quantity) || this.quantity < 1) {
          this.quantity = 1
        }
        const item = {
          product: this.product,
          quantity: this.quantity,
        }

        this.$store.commit("addToCart", item)

        this.$router.push({ name: "Cart" })
      }
    },
  },
}
</script>

<style>
.mb-3,
.my-3 {
  margin-bottom: 1rem !important;
}
.mt-3,
.my-3 {
  margin-top: 1rem !important;
}
.btn-ib {
  display: inline-block;
  font-weight: 600;
  color: #55595c;
  text-align: center;
  vertical-align: middle;
  user-select: none;
  background-color: transparent;
  border: 0 solid transparent;
  padding: 0.75rem 1.5rem;
  font-size: 0.875rem;
  line-height: 1.5rem;
  border-radius: 0;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}
</style>
