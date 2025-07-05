<template>
  <div id="origin-chart-block" class="container my-4">
    <div
      id="chart-block"
      class="row align-items-center justify-content-between"
    >
      <canvas style="width: 20vw; height: 20vw" ref="chartCanvas"></canvas>
      <div
        class="col-7 border-start"
        style="height: 60vh; border-color: #52796f !important"
      >
        <p id="info-block-title" class="fw-bold fs-4" style="color: #588157">
          Популярность ресурсов
          <br />
          {{ subTitle }}
        </p>
        <div class="overflow-auto el-w-scroll" style="max-height: 48vh">
          <div v-for="(item, idx) in originData" :key="idx">
            <span class="row w-100">
              <strong class="col-6">{{ idx }}</strong>
              <span class="col text-end">&mdash;&emsp;{{ item }}</span>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { API } from "@/../app-config";
import { Chart } from "chart.js/auto";
export default {
  name: "OriginChart",
  data() {
    return {
      isData: false,
      chart: null,
      subTitle: String,
      originData: Object,
      labels: Array,
      counts: Array,
    };
  },
  methods: {
    // метод для отрисовки в зависимости от параметров маршрута
    loadData(statType) {
      if (statType === "token_generation") {
        this.subTitle = "(по формированию токенов)";
        this.getOriginsTokenCreate();
      } else if (statType === "visiting_origins") {
        this.subTitle = "(по посещению)";
        this.getOriginsLogStatistic();
      }
    },

    // метод для сортировки
    sortData(obj) {
      const entries = Object.entries(obj); // объект в массив пар
      entries.sort((a, b) => b[1] - a[1]); // Сортируем по значению
      return Object.fromEntries(entries);
    },

    // метод получения данных с API (популярность по формированию токенов)
    async getOriginsTokenCreate() {
      try {
        const response = await fetch(
          `http://${API}/api/distinct_origins_from_storage`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json;",
            },
          }
        );
        if (response.ok) {
          const data = await response.json();
          this.originData = this.sortData(data);
          this.isData = true;
          this.drawChart();
        } else {
          throw new Error(
            "Ошибка fetch получения статистики ресурсов, на которые формируются токены"
          );
        }
      } catch (error) {
        console.error(error);
      }
    },

    // метод получения данных с API (популярность по посещению)
    async getOriginsLogStatistic() {
      try {
        const response = await fetch(
          `http://${API}/api/origin_statistic_by_logs`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json;",
            },
          }
        );
        if (response.ok) {
          const data = await response.json();
          this.originData = this.sortData(data);
          this.isData = true;
          this.drawChart();
        } else {
          throw new Error(
            "Ошибка fetch получения статистики посещения ресурсов"
          );
        }
      } catch (error) {
        console.error(error);
      }
    },

    // метод отрисовки графика
    drawChart() {
      if (this.chart) {
        this.chart.destroy();
      }
      this.chart = new Chart(this.$refs.chartCanvas.getContext("2d"), {
        type: "doughnut",
        data: {
          labels: Object.keys(this.originData),
          datasets: [
            {
              label: "Количество формирований токена",
              data: Object.values(this.originData),
            },
          ],
        },
        options: {
          responsive: false,
          plugins: {
            legend: {
              display: false,
            },
          },
        },
      });
    },
  },
  created() {
    this.loadData(this.$route.params.statType);
  },
  watch: {
    "$route.params.statType"(newVal) {
      this.loadData(newVal);
    },
  },
  beforeUnmount() {
    if (this.chart) {
      this.chart.destroy();
    }
  },
};
</script>

<style scoped>
canvas {
  height: 40vh;
}
</style>
