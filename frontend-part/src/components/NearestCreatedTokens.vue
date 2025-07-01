<template>
  <div id="nearest-header-block" class="container mb-2 w-100">
    <div class="row justify-content-center align-items-center">
      <div class="col-8 p-0 text-start">
        <p id="nearest-header" class="m-0 p-0">
          Список URL, на которые формировался токен
        </p>
      </div>
      <div class="col-4 p-0 d-flex flex-row align-items-center">
        <p class="w-50 m-0 p-0">Показать:</p>
        <select
          id="url-count"
          class="w-50 form-select py-0"
          name="choose-url-count"
          v-model="showCount"
          @change="getNearest"
        >
          <option value="5">5 ссылок</option>
          <option value="10">10 ссылок</option>
          <option value="15">15 ссылок</option>
          <option value="30">30 ссылок</option>
        </select>
      </div>
    </div>
  </div>
  <div id="nearest-token-wrap" class="table-responsive h-50 el-w-scroll">
    <table id="url-table" class="table text-center url-table">
      <thead class="sticky-top">
        <tr>
          <th class="col-1">#</th>
          <th class="col">Адрес ресурса</th>
          <th class="col-3">Время создания</th>
        </tr>
      </thead>
      <tbody v-if="isNearest && nearest.length" class="overflow-y">
        <tr v-for="(item, idx) in nearest" :key="idx">
          <td>{{ idx + 1 }}</td>
          <td>{{ shortUrl(item.original_url) }}</td>
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
      showCount: "5", // количество отображаемых ссылок
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
        const response = await fetch(
          ` http://${API}/api/nearest/${this.showCount}`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json;",
            },
          }
        );
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
    shortUrl(variable) {
      let exStr;
      const maxLen = 50;
      if (variable.length >= maxLen) {
        exStr = variable.substring(0, maxLen);
      } else {
        exStr = variable;
      }
      return exStr;
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
  background-color: #dad7cd !important;
  color: #84a98c !important;
}
.url-table tr:hover td {
  background-color: #84a98c !important;
  color: #dad7cd !important;
  font-weight: bold;
}
</style>
