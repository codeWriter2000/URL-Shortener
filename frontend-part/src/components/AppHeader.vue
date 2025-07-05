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
    <div class="d-flex flex-column align-items-center shadow">
      <span @click="goTo('/')">формирование короткого токена</span>
      <span @click="goTo('/statistic/token_generation')">
        популярность ресурсов по формированию токенов
      </span>
      <span @click="goTo('/statistic/visiting_origins')">
        популярность ресурсов по посещению
      </span>
      <span @click="goTo('/about')">о приложении URL Shortener</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppHeader",
  methods: {
    goTo(pathTo) {
      this.$router.push({ path: pathTo });
    },
  },
};
</script>

<style scoped>
#views-changer {
  position: absolute;
  background-color: #84a98c;
  color: #cad2c5;
}
#views-changer span {
  width: 100%;
  text-align: center;
  text-transform: uppercase;
  cursor: pointer;
  padding-top: 0.45rem;
  padding-bottom: 0.45rem;
}
#views-changer span:hover {
  text-decoration: underline;
  background-color: #588157;
  font-weight: bold;
  color: #cad2c5;
}
</style>
