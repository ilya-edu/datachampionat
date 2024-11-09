import httpClient from "@/httpClient";

export default class NodesService {

	static async query(q) {
		const response = await httpClient().get(`req?q=${q}`);

		return response.data;
	}
}
