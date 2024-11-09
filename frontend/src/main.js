import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./vuetify";
import "roboto-fontface/css/roboto/roboto-fontface.css";
import { store } from "@/store";
import VueMeta from 'vue-meta'
Vue.config.productionTip = false;

new Vue({
	router,
	vuetify,
	store: store,
	render: h => h(App)
}).$mount("#app");

Vue.use(VueMeta)
