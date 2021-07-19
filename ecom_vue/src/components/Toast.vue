<template>
  <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header">
      <img src="" class="rounded me-2" alt="..." />
      <strong class="me-auto">{{ toast.title }}</strong>
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="toast"
        aria-label="Close"
      ></button>
    </div>
    <div class="toast-body">
      {{ toast.message }}
    </div>
  </div>
</template>

<script>
export default {
  name: "Toast",
  props: {
    toast: Object,
  },
}
</script>

<style></style>
