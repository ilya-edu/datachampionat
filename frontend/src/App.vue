<template>
	<v-app>
		<BaseLayout>
			<router-view />
		</BaseLayout>
	</v-app>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout";
export default {
	components: { BaseLayout },
  metaInfo() {
        return {
            title: "CNCIOT",
            meta: [
                { name: 'description', content:  ''},
                { property: 'og:title', content: "CNCIOT"},
                { property: 'og:site_name', content: 'CNCIOT'},
                {property: 'og:type', content: 'website'},
                {name: 'robots', content: 'index,follow'}
            ]
        }
  }

};
</script>
