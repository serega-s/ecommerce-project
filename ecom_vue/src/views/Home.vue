<template>
  <div class="container">
    <div>
      <div
        id="carouselExampleFade"
        class="carousel slide carousel-fade"
        data-bs-ride="carousel"
      >
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img :src="carouselImages[0]" class="d-block w-100" alt="..." />
          </div>
          <div class="carousel-item">
            <img :src="carouselImages[1]" class="d-block w-100" alt="..." />
          </div>
          <div class="carousel-item">
            <img :src="carouselImages[2]" class="d-block w-100" alt="..." />
          </div>
          <div class="carousel-item">
            <img
              src="https://miro.medium.com/max/1200/0*M_fyzQ163vM0hWsZ"
              class="d-block w-100"
              alt="..."
            />
          </div>
        </div>
        <button
          class="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExampleFade"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button
          class="carousel-control-next"
          type="button"
          data-bs-target="#carouselExampleFade"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
    <br />
    <h1 class="uppercase">Latest Products</h1>
    <div>
      <div class="row">
        <!-- <div class="col-lg-4">
          <form method="GET" class="form" @change.prevent="getLatestProducts">
            <p>
              <label for="name">Name</label>
              <input type="text" class="form-control" placeholder="Name">
            </p>
            <p>
              <label for="description">Description</label>
              <input type="text" class="form-control" placeholder="Description">
            </p>
            <p>
              <label for="description">Brand</label>
              <input type="text" class="form-control" placeholder="Brand">
            </p>
            <p>
              <label for="price">Price Range</label>
              <input type="text" class="form-control" placeholder="Min Price" v-model="min_price">
              <input type="text" class="form-control" placeholder="Max Price" v-model="max_price">
            </p>

            <button class="btn btn-success" type="submit">Search</button>
          </form>
        </div> -->
        <div
          class="col-xl-3 col-lg-4 col-md-6 col-sm-12"
          v-for="product in products"
          :key="product.id"
        >
          <ProductBox :product="product" />
        </div>
      </div>
      <ul class="pagination">
        <li
          class="page-item"
          v-for="num in num_products"
          :key="num"
          style="cursor: pointer;"
          :class="{ active: isActive == num }"
          @click="goToPage(parseInt(num))"
        >
          <span class="page-link">{{ num }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import ProductBox from "@/components/ProductBox.vue"

import axios from "axios"

export default {
  name: "Home",
  data() {
    return {
      products: [],
      currentPage: 1,
      isActive: 0,
      num_products: 0,
      carouselImages: [],
      name: '',
      brand: '',
      description: '',
      min_price: 0,
      max_price: 0,
    }
  },
  mounted() {
    this.getLatestProducts()
    this.isActive = 1
    document.title = "Home | Shop"
  },
  methods: {
    goToPage(num) {
      this.currentPage = num
      this.isActive = num
      this.getLatestProducts()
    },
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true)

      await axios
        .get("/api/v1/products/")
        .then((response) => {
          console.log(response.data)
          
          this.num_products = response.data.pages
          this.carouselImages[0] = response.data.products[0].get_image
          this.carouselImages[1] = response.data.products[1].get_image
          this.carouselImages[2] = response.data.products[2].get_image
        })
        .catch((error) => {
          console.log(error.response)
        })

      await axios
        .get(`/api/v1/products/?page=${this.currentPage}`)
        .then((response) => {
          this.products = response.data.products
        })
        .catch((error) => {
          console.log(error.response)
        })
      this.$store.commit("setIsLoading", false)
    },
  },
  components: {
    ProductBox,
  },
}
</script>

<style scoped>
.carousel {
  width: 55%;
  margin: 10px auto;
}
</style>
