import { fetchData } from '../../lib/utils/api.js';

export const load = async ({ params }) => {
	const resp = await fetchData('exampleitems/');
	const exampleitems = resp.exampleitems;
	return {
		exampleitems
	};
};
