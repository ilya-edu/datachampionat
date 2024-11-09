<template>
  <v-card
      :style="cardStyle"
      :color="this.node.image_color"
    >
      <div class="d-flex flex-no-wrap justify-space-between">
        <div>
          <v-card-title
            class="headline"
            v-text="node.title"
          ></v-card-title>

          <v-card-subtitle v-text="node.title"></v-card-subtitle>
          <v-card-actions>
            <v-btn
              v-if="node.preview_description === 'Ellie Goulding'"
              class="ml-2 mt-3"
              fab
              icon
              height="40px"
              right
              width="40px"
            >
              <v-icon>mdi-play</v-icon>
            </v-btn>

            <v-btn
              v-else
              class="ml-2 mt-5"
              outlined
              rounded
              small
            >
             ПОДРОБНЕЕ
            </v-btn>
          </v-card-actions>
        </div>

        <v-avatar
          class="ma-3"
          size="125"
          tile
          left="0"
        >
          <v-img :src="node.image"></v-img>
        </v-avatar>
      </div>
    </v-card>
</template>

<script>

export default {
	name: "MainCardComponent",
	props: {
		node: {
			type: Object,
			required: true,
			default: null
		}
	},
	computed: {
    cardStyle() {
      var hex = this.node.image_color
      var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
      var r = result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
      } : null;
      return {
        "background-color": this.node.image_color,
        "background": `linear-gradient(180deg, rgba(${r.r}, ${r.g}, ${r.b}, 1), rgba(${r.r - 35}, ${r.g - 35}, ${r.b - 35}, 1))`
      };
    },
	}
};
</script>

<style scoped lang="scss">

</style>
