<template>
  <v-app id="inspire">
		<v-main>
			<slot />
		</v-main>

  </v-app>
</template>

<script>
import Header from "@/layouts/Header";
export default {
	name: "BaseLayout",
	components: { Header },
  data: () => ({
      collapseOnScroll: true,
      links: ['Главная']
    }),
};
</script>

<style lang="scss">
@import "../assets/scss/common";

</style>
