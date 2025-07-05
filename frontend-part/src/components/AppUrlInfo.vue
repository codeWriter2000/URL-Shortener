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
      <div class="w-75 p-0">
        <img
          alt="qr-code"
          :src="`data:image/png;base64,${urlObj.qrcode}`"
          class="img-fluid rounded border border-dark bg-transparent my-2"
        />
      </div>
    </div>
    <div
      id="copy-btn-block"
      class="row align-items-center justify-content-center my-2"
    >
      <button
        id="copy-btn"
        class="btn rounded shadow text-uppercase fw-bold w-75"
        @click.prevent="copyToBuffer"
      >
        скопировать
      </button>
    </div>
  </div>
</template>

<script>
import { API } from "@/../app-config";
export default {
  name: "AppUrlInfo",
  props: {
    urlObj: {
      type: Object,
      required: true,
    },
  },
  methods: {
    async copyToBuffer() {
      const urlToCopy = `http://${API}/${this.urlObj.short_token}`;
      try {
        await navigator.clipboard.writeText(urlToCopy);
        alert("Короткая ссылка на ресурс скопирована в буфер обмена");
      } catch (error) {
        alert("Произошла ошибка при копировании");
      }
    }, // копирование в буфер обмена (работает на navigator API только на localhost и https)
  },
};
</script>

<style>
#copy-btn {
  color: #dad7cd;
  background-color: #588157;
}
#copy-btn:hover {
  color: #588157;
  background-color: #84a98c;
}
</style>
