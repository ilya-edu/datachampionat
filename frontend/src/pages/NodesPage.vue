
<template>
    <v-main>
      <v-container>
        <v-row id='nodes-list'>
          <v-col
            v-for="node in nodes "
            :key="node.id"
            width="300"
            cols=columnCount
          >
      			<PreviewNodeComponent
      				class="node"
      				:key="node.id"
      				:node="node"
      			/>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
</template>
<script>

import NodesService from "@/services/NodesService.js";

export default {
	name: "Nodes",
  components: {
		PreviewNodeComponent
	},
	async mounted() {
    // this.nodes = await NodesService.getAll();
  },
	data: () => ({
    
	}),
  computed: {
    columnCount() {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return 1
        case 'sm': return 2
        case 'md': return 2
        case 'lg': return 3
        case 'xl': return 3
      }
    }
  },
  metaInfo() {
        return {
            title: "CNCIOT — список нод",
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

<style scoped lang="css">
  #nodes-list {
    padding-top: 4em;
  }
</style>
