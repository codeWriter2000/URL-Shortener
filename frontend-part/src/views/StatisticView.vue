<template>
  <AppWrap>
    <AppHeader style="z-index: 100" />
    <OriginChart />
  </AppWrap>
</template>

<script>
import AppWrap from "@/components/AppWrap.vue";
import AppHeader from "@/components/AppHeader.vue";
import OriginChart from "@/components/OriginChart.vue";
export default {
  name: "StatisticView",
  components: {
    AppWrap,
    AppHeader,
    OriginChart,
  },
};
</script>

<style></style>
