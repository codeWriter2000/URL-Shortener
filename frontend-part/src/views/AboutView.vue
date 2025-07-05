<template>
  <AppWrap>
    <AppHeader style="z-index: 100" />
    <AppAbout />
  </AppWrap>
</template>

<script>
import AppWrap from "@/components/AppWrap.vue";
import AppHeader from "@/components/AppHeader.vue";
import AppAbout from "@/components/AppAbout.vue";
export default {
  name: "MainView",
  components: {
    AppWrap,
    AppHeader,
    AppAbout,
  },
};
</script>

<style></style>
