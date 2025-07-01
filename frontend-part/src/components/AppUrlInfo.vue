<template>
  <div id="url-info-block" class="container">
    <div id="sort-token-block" class="row">
      <p class="text-center m-0">
        <span class="text-uppercase" style="color: #2f3e46">
          ваш короткий токен:
        </span>
        <br />
        <span class="target-txt fw-bold fs-4">{{ urlObj.short_token }}</span>
      </p>
    </div>
    <div id="qr-block" class="row align-items-center justify-content-center">
      <div class="w-75">
        <img
          alt="qr-code"
          :src="`data:image/png;base64,${urlObj.qrcode}`"
          class="img-fluid rounded border border-dark bg-transparent my-2"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppUrlInfo",
  props: {
    urlObj: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style></style>
