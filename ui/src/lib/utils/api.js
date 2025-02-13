import { PUBLIC_API_URL } from '$env/static/public';

const baseUrl = PUBLIC_API_URL;

export async function fetchData(url) {
	try {
		const response = await fetch(baseUrl + url);
		if (!response.ok) {
			throw new Error('Error during request FETCH');
		}
		return await response.json();
	} catch (error) {
		console.error('Error FETCH:', error);
		throw error;
	}
}

export async function postData(url, body) {
	try {
		const response = await fetch(baseUrl + url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(body)
		});

		if (!response.ok) {
			throw new Error('Error during request POST');
		}

		return await response.json();
	} catch (error) {
		console.error('Error POST:', error);
		throw error;
	}
}

export async function patchData(url, body) {
	try {
		const response = await fetch(baseUrl + url, {
			method: 'PATCH',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(body)
		});

		if (!response.ok) {
			throw new Error('Error during request PATCH');
		}

		return await response.json();
	} catch (error) {
		console.error('Error PATCH:', error);
		throw error;
	}
}

export async function deleteData(url) {
	try {
		const response = await fetch(baseUrl + url, {
			method: 'DELETE',
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			throw new Error('Error during request DELETE');
		}

		return response;
	} catch (error) {
		console.error('Error DELETE:', error);
		throw error;
	}
}
