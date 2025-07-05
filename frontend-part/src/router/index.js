import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("@/views/MainView.vue"),
  },
  {
    path: "/statistic/:statType",
    component: () => import("@/views/StatisticView.vue"),
  },
  {
    path: "/about",
    component: () => import("@/views/AboutView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
