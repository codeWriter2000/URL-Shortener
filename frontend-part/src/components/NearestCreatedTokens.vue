<template>
  <div id="nearest-token-wrap">
    <table id="url-table" class="table text-center url-table">
      <thead>
        <tr>
          <th class="col-1">#</th>
          <th class="col">Адрес ресурса</th>
          <th class="col-3">Время создания</th>
        </tr>
      </thead>
      <tbody v-if="isNearest && nearest.length" class="overflow-y">
        <tr v-for="(item, idx) in nearest" :key="idx">
          <td>{{ idx + 1 }}</td>
          <td>{{ item.original_url }}</td>
          <td>{{ createdInfo(item.created) }}</td>
        </tr>
      </tbody>
      <tbody v-if="isNearest && !nearest.length">
        <tr>
          <td colspan="3">еще нет ни одного URL</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { API } from "@/../app-config";
export default {
  name: "NearestCreatedTokens",
  data() {
    return {
      isNearest: false, // переменная состояния получения ответа
      nearest: Object, // объект, хранящий объекты (url, created)
    };
  },
  methods: {
    createdInfo(variable) {
      const created = new Date(variable);
      return created.toLocaleDateString("ru-RU", {
        hour: "2-digit",
        minute: "2-digit",
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
      });
    },
    async getNearest() {
      try {
        const response = await fetch(` http://${API}/api/nearest/10`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json;",
          },
        });
        if (response.ok) {
          this.nearest = await response.json();
          this.isNearest = true;
        } else {
          throw new Error(
            "Ошибка fetch получения ближайших ресурсов для которых сформированы токены"
          );
        }
      } catch (error) {
        console.error(error);
      }
    },
  },
  created() {
    this.getNearest();
  },
};
</script>

<style>
.url-table {
  border-color: #52796f !important;
  border-style: solid;
  border-width: thin;
}
.url-table th {
  background-color: #588157 !important;
  color: #dad7cd !important;
}
.url-table td {
  background-color: #84a98c !important;
  color: #dad7cd !important;
}
.url-table tr:hover td {
  background-color: #dad7cd !important;
  color: #84a98c !important;
  font-weight: bold;
}
</style>
