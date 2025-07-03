<template>
  <div id="origin-chart-block" class="container my-4">
    <div
      id="chart-block"
      class="row align-items-center justify-content-between"
    >
      <canvas class="col-3" ref="chartCanvas"></canvas>
      <div class="col">
        здесь будет таблица с данными о ресурсах на которые формировали токены
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
      originData: Object,
      labels: Array,
      counts: Array,
    };
  },
  methods: {
    // метод для сортировки
    sortData(obj) {
      const entries = Object.entries(obj); // объект в массив пар
      entries.sort((a, b) => a[1] - b[1]); // Сортируем по значению
      return Object.fromEntries(entries);
    },

    // метод получения данных с API
    async getOrigins() {
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
          maintainAspectRatio: false,
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
    this.getOrigins();
  },
  mounted() {
    this.drawChart();
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
