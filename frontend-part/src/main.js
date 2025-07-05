import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// импорт Bootstrap
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

// Импорт глобального CSS
import "@/../public/base.css";

createApp(App).use(router).mount("#app");
