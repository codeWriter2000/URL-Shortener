<template>
  <teleport to="#modal">
    <div id="modal-overlay" v-if="isVisible"></div>
    <div
      id="app-modal-window"
      class="container position-fixed top-50 start-50 w-25 translate-middle rounded shadow p-2 my-3"
      v-if="isVisible"
    >
      <div class="row align-items-center m-0 p-2">
        <div class="col text-center text-xxl-start p-1">
          <span class="fs-6 fw-bolder" style="color: #2f3e46">
            URL Shortener modal
          </span>
        </div>
        <div class="col-12 text-center col-xxl-2 text-xxl-end">
          <button
            id="close-modal-btn"
            class="btn btn-outline-danger"
            @click="closeModal"
          >
            <img
              src="@/../public/cross-icon.png"
              style="height: 1.25rem"
              alt="close"
              class="icon"
            /></button
          ><!--  close modal button  -->
        </div>
      </div>
      <slot name="modal-content"></slot>
    </div>
  </teleport>
</template>

<script>
export default {
  name: "AppModal",
  emits: ["ModalClosed"],
  data() {
    return {
      isVisible: false,
    };
  },
  methods: {
    showModal() {
      this.isVisible = true;
      document.body.classList.add("modal-open");
    },
    closeModal() {
      this.isVisible = false;
      document.body.classList.remove("modal-open");
      this.$emit("ModalClosed");
    },
  },
};
</script>

<style></style>
