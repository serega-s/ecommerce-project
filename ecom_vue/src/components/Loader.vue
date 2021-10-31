<template>
  <div class="d-flex justify-content-center">
    <div
      class="is-loading-bar "
      :class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-default">
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>
