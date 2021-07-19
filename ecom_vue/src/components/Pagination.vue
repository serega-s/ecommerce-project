<template>
  
</template>

<script>
export default {
  name: "Pagination",
  props: {
    num_products: Number,
    // currentPage: Number
  },
  data() {
    return {
      isActive: 0,
      currentPage: 1,
      // isActive: this.isActive,
    }
  },
  mounted() {
    this.getLatestProducts()
    
  },
  methods: {
    goToPage(num) {
      this.currentPage = num
      this.isActive = num

      console.log(this.currentPage)
      
      this.getLatestProducts()
    },
    getLatestProducts() {
      this.$emit("getLatestProducts")
    },
  },
}
</script>
