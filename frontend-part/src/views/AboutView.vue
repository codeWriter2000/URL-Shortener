<template>
  <AppWrap>
    <AppHeader style="z-index: 100" />
    это вид для справочной информации о приложении
  </AppWrap>
</template>

<script>
import AppWrap from "@/components/AppWrap.vue";
import AppHeader from "@/components/AppHeader.vue";
export default {
  name: "MainView",
  components: {
    AppWrap,
    AppHeader,
  },
};
</script>

<style></style>
