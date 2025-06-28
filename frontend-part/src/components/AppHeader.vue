<template>
  <nav id="app-header-nav" class="navbar navbar-light align-items-center mt-2">
    <div class="container-fluid">
      <span class="fs-3 fw-bold target-txt"> URL Shortener </span>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#views-changer"
        aria-controls="navbarToggleExternalContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
    </div>
  </nav>
  <div id="views-changer" class="collapse w-100 position-absolute start-0">
    <div class="d-flex flex-column align-items-center p-3">
      <span>здесь будут кнопки</span>
      <span>здесь будут кнопки</span>
      <span>здесь будут кнопки</span>
    </div>
  </div>
</template>

<script></script>

<style scoped>
#views-changer {
  position: absolute;
  background-color: #84a98c;
  color: #cad2c5;
}
</style>
