<template>
  <AppWrap>
    <AppHeader style="z-index: 100" />
    <AppUrlForm style="z-index: 0" />
    <hr style="z-index: 0" />
    <NearestCreatedTokens style="z-index: 0" />
  </AppWrap>
</template>

<script>
import AppWrap from "@/components/AppWrap.vue";
import AppHeader from "@/components/AppHeader.vue";
import AppUrlForm from "@/components/AppUrlForm.vue";
import NearestCreatedTokens from "@/components/NearestCreatedTokens.vue";
export default {
  name: "MainView",
  components: {
    AppWrap,
    AppHeader,
    AppUrlForm,
    NearestCreatedTokens,
  },
};
</script>

<style></style>
