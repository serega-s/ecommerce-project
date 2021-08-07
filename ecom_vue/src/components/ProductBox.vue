<template>
  <div class="my-3 p-3 rounded card h-80" >
    <router-link :to="{ name: 'Product', params: { id: product.id } }"
      ><img class="card-img" :src="product.get_image"
    /></router-link>
    <div class="card-body">
      <router-link :to="{ name: 'Product', params: { id: product.id } }"
        ><div class="card-title">
          <h6 class="underline">{{ product.name }}</h6>
        </div></router-link
      >
      <div class="card-text">
        <div class="my-3">
          <div class="rating">
            <Rating :rating="Math.round(product.get_avg_rating)" />&nbsp;<span>{{
              product.reviews.length
            }} reviews</span>
          </div>
        </div>
      </div>
      <h3 class="card-text">${{ product.price }}</h3>
    </div>
  </div>
</template>

<script>
import Rating from "@/components/Rating.vue"
export default {
  name: "ProductBox",
  props: {
    product: Object,
  },
  components: {
    Rating,
  },
}
</script>

<style></style>
