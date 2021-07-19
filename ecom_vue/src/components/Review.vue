<template>
  <div>
    <strong> {{ review.user.first_name }} {{ review.user.last_name }} </strong>
    <div class="rating">
      <template v-if="review.rating == 1">
        <span
          ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
        ></span>
      </template>
      <template v-if="review.rating == 2">
        <span
          ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
        ></span>
        <span
          ><i class="bi bi-star-fill" style="color: rgb(248, 232, 37);"></i
        ></span>
      </template>
      <template v-if="review.rating == 3">
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
      <template v-if="review.rating == 4">
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
      <template v-if="review.rating == 5">
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
    </div>
    <p>{{ review.created_at }}</p>
    <p>{{ review.comment }}</p>
  </div>
</template>

<script>
export default {
  name: "Review",
  props: {
    review: Object
  }
}
</script>

<style></style>
