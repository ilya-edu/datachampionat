import axios from "axios"

const httpClient = () => {
	const baseUrl = "https://smart.kovalev.team/api/";

	return axios.create({
		baseURL: baseUrl,
		headers: {
			"Content-Type": "application/json"
		}
	})
}

export default httpClient;
