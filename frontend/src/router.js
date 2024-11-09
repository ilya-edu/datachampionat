import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
	{
		path: "/",
		name: "Main",
		component: () => import("@/pages/MainPage.vue")
	},
	{
		path: "/nodes",
		name: "Nodes",
		component: () => import("@/pages/NodesPage.vue")
	}
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes
});

export default router;
