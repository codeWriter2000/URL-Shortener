<template>
  <div
    id="app-wrap"
    class="container position-fixed top-50 start-50 w-50 h-75 translate-middle rounded shadow"
  >
    <slot></slot>
  </div>
</template>

<script></script>

<style scoped>
#app-wrap {
  background-color: #dad7cd;
  backdrop-filter: blur(10px);
}
</style>
