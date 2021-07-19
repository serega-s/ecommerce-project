<template>
  <span>
    <template v-if="rating == 0">
      <span><i class="bi bi-star" style="color: rgb(248, 232, 37);"></i></span>
      <span><i class="bi bi-star" style="color: rgb(248, 232, 37);"></i></span>
      <span><i class="bi bi-star" style="color: rgb(248, 232, 37);"></i></span>
      <span><i class="bi bi-star" style="color: rgb(248, 232, 37);"></i></span>
      <span><i class="bi bi-star" style="color: rgb(248, 232, 37);"></i></span>
    </template>
    <template v-if="rating == 1">
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
    </template>
    <template v-if="rating == 2">
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
    </template>
    <template v-if="rating == 3">
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
    </template>
    <template v-if="rating == 4">
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
    </template>
    <template v-if="rating == 5">
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
      <span
        ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
      ></span>
    </template>
  </span>
</template>

<script>
export default {
  name: "Rating",
  props: {
    rating: Number,
  },
}
</script>
