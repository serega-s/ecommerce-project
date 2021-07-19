<template>
  <div class="container">
    <h1 class="uppercase">Search keyword: "{{ query }}"</h1>
    <div>
      <div class="row">
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
  name: "Search",
  components: {
    ProductBox,
  },
  data() {
    return {
      products: [],
      query: "",
      currentPage: 1,
      isActive: 0,
      num_products: 0,
    }
  },
  mounted() {
    document.title = "Search | Shop"
    let uri = window.location.search.substring(1)
    let params = new URLSearchParams(uri)

    if (params.get("query")) {
      this.query = params.get("query")
      this.performSearch()
    }

    this.isActive = 1
  },
  methods: {
    goToPage(num) {
      this.currentPage = num
      this.isActive = num
      this.performSearch()
    },
    async performSearch() {
      this.$store.commit("setIsLoading", true)

      await axios
        .post("/api/v1/products/", { query: this.query })
        .then((response) => {
          this.num_products = response.data.pages
        })
        .catch((error) => {
          console.log(error.response)
        })

      await axios
        .post(`/api/v1/products/?page=${this.currentPage}`, {
          query: this.query,
        })
        .then((response) => {
          this.products = response.data.products
        })
        .catch((error) => {
          console.log(error.response)
        })

      this.$store.commit("setIsLoading", false)
    },
  },
}
</script>
