<template>
	<header>
		<div class="left-side d-flex align-center">
			<router-link to="/" style="height: 75px">
				<img src="../assets/img/logo.svg" alt="logo" height="75" width="75" />
			</router-link>

			<nav class="ml-8">
				<router-link class="nav-link-count" to="/" exact>
					<span class="label">Заявки</span>
				</router-link>

				<router-link class="nav-link" to="/substations">Подстанции</router-link>
				<router-link class="nav-link" to="/online">Онлайн датчики</router-link>
			</nav>
		</div>

		<div class="right-side">
			<v-btn
				outlined
				color="#fff"
				@click="$refs.uploadModal.show()"
				style="margin-right: 20px"
			>
				<v-icon left>publish</v-icon>
				Создать заявку

				<CreateTicketModalComponent ref="uploadModal" />
			</v-btn>

			<v-avatar>
				<img src="../assets/img/avatar.jpeg" alt="avatar" />
			</v-avatar>
		</div>
	</header>
</template>

<script>
export default {
	name: "Header"
};
</script>

<style scoped lang="scss">
@import "../assets/scss/variables";

header {
	background: $primary;
	color: white;
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 0 5%;

	.new-tickets-count {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		color: white;
		background: #f44336;
		border-radius: 50%;
		width: 25px;
		height: 25px;
		margin-left: 10px;
	}

	nav .nav-link,
	nav .nav-link-count .label {
		padding: 16px 0;
		font-weight: 500;
		font-size: 18px;
		color: white;
	}

	nav .nav-link-count {
		&.router-link-active .label {
			border-bottom: 2px solid white;
			padding-bottom: 2px;
		}

		.new-tickets-count {
			margin-right: 20px;
		}
	}

	nav .nav-link {
		margin-right: 50px;

		&.router-link-active {
			border-bottom: 2px solid white;
			padding-bottom: 2px;
		}
	}
}
</style>
