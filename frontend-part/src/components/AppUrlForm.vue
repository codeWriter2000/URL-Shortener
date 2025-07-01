<template>
  <form id="app-url-form" class="container my-4">
    <div id="url-input-block" class="row justify-content-center">
      <label for="url-input" class="form-label w-75 p-0">
        Введите URL:
        <input
          id="url-input"
          type="text"
          class="form-control text-center"
          v-model="originalUrl"
        />
      </label>
    </div>
    <div id="btn-block" class="row justify-content-center">
      <button
        id="get-token-btn"
        class="btn w-75 border rounded fw-bold text-uppercase"
        @click.prevent="btnClickFunc"
      >
        сформировать&ensp;короткий&ensp;токен
      </button>
    </div>
  </form>
  <AppModal ref="modal">
    <template #modal-content>
      <AppUrlInfo :url-obj="responseData" />
    </template>
  </AppModal>
</template>

<script>
import { API } from "@/../app-config";
import AppModal from "@/components/AppModal.vue";
import AppUrlInfo from "@/components/AppUrlInfo.vue";
export default {
  name: "AppUrlForm",
  emits: [],
  components: {
    AppModal,
    AppUrlInfo,
  },
  data() {
    return {
      originalUrl: "",
      isResponse: false,
      responseData: Object,
    };
  },
  methods: {
    validateModel() {
      return /^(https?:\/\/)/.test(this.originalUrl.trim());
    },
    async createToken(urlStr) {
      try {
        const response = await fetch(`http://${API}/api/url`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json;",
          },
          body: JSON.stringify({
            original_url: urlStr,
          }),
        });
        if (response.ok) {
          this.isResponse = true;
          this.responseData = await response.json();
          console.table(this.responseData);
          this.$refs.modal.showModal();
        } else {
          throw new Error(
            `Ошибка fetch формирования токена для url: ${urlStr}`
          );
        }
      } catch (error) {
        console.error(error);
      }
    },
    btnClickFunc() {
      const isValid = this.validateModel();
      if (isValid) {
        this.createToken(this.originalUrl.trim());
      } else {
        alert("Введенный URL не валиден!");
      }
    },
  },
};
</script>

<style scoped>
#get-token-btn {
  color: #dad7cd;
  background-color: #588157;
}
#get-token-btn:hover {
  color: #588157;
  background-color: #84a98c;
}
</style>
