# КЛИЕНТСКАЯ ЧАСТЬ URL SHORTENER

## структура клиентская части

- [app-config.js](app-config.js) - конфигурационный файл (настройка связи с API);
- [base.css](./public/base.css) - основные стили приложения;
- [router](./src/router/index.js) - настройка маршрутизации приложения;
- [views](./src/views/) - директория c видами приложения;
    - [MainView](./src/views/MainView.vue) - основной вид приложения;
    - [StatisticView](./src/views/StatisticView.vue) - вид для отображения статистик использования приложения;
    - [AboutView](./src/views/AboutView.vue) - вид для отображения справочной информации;
- [components](./src/components/) - директория с компонентами;
    - [AppWrap](./src/components/AppWrap.vue) - карточка-обертка;
    - [AppHeader](./src/components/AppHeader.vue) - заголовок с навигацией;
    - [AppModal](./src/components/AppModal.vue) - модальное окно с логикой телепортирования;
    - [AppUrlForm](./src/components/AppUrlForm.vue) - форма ввода полного URL стороннего ресурса;
    - [AppUrlInfo](./src/components/AppUrlInfo.vue) - компонент отображения короткого токена и QR кода;
    - [AppAbout](./src/components/AppAbout.vue) - компонент со справкой о приложении;
    - [NearestCreatedTokens](./src/components/NearestCreatedTokens.vue) - компонент для отображения списка URL, на которые недавно сформировали короткие токены;
    - [OriginChart](./src/components/OriginChart.vue) - компонент со статистикой и круговой диаграммой.


## порядок запуска
1. Установка необходимых зависимостей: `$ npm install`;
2. Запуск клиентской части (dev): `$ npm run serve`;
3. В случае возникновения ошибок: `$ npm run lint-- --fix`.
