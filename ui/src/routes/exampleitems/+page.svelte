<script>
	export let data;
	import IconKit from '$lib/components/IconKit.svelte';
	import { Modal, getModalStore } from '@skeletonlabs/skeleton';
	import ModalDelete from '$lib/components/ModalDelete.svelte';
	import ModalExampleItem from '$lib/components/ModalExampleItem.svelte';
	import { postData, patchData, deleteData } from '$lib/utils/api.js';
	import { getToastStore } from '@skeletonlabs/skeleton';
	import { popup } from '@skeletonlabs/skeleton';

	const toastStore = getToastStore();
	const modalStore = getModalStore();

	let { exampleitems } = data;
	let newExampleItem = {
		title: 'Lorem ipsum',
		value: 100,
		code: 'LIPS01',
		description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
	};

	// Add exampleitem
	function saveExampleItem(exampleitem) {
		const modalComponent = {
			ref: ModalExampleItem
		};
		const modal = {
			type: 'component',
			component: modalComponent,
			title: 'Add ExampleItem',
			body: 'Fill out the form to add a exampleitem',
			formdata: exampleitem,
			response: (r) => apiAddExampleItem(r)
		};
		modalStore.trigger(modal);
	}

	async function apiAddExampleItem(r) {
		let message = 'Error! ExampleItem not added.';
		let type = 'variant-filled-error';
		if (r) {
			try {
				const response = await postData('exampleitems/', r);
				if (response) {
					type = 'variant-filled-success';
					message = 'ExampleItem added successfully';
					exampleitems = [...exampleitems, response];
				}
				console.log(response);
			} catch (error) {
				console.log(error);
			}
		} else {
			type = 'variant-filled-warning';
			message = 'ExampleItem addition canceled';
		}
		const toast = {
			message: message,
			timeout: 10000,
			background: type
		};
		toastStore.trigger(toast);
	}

	// Edit exampleitem
	function editExampleItem(example) {
		const modalComponent = {
			ref: ModalExampleItem
		};
		const modal = {
			type: 'component',
			component: modalComponent,
			title: 'Edit ExampleItem: ' + example.code,
			body: '',
			formdata: example,
			response: (r) => apiPatchExampleItem(example.id, r)
		};
		modalStore.trigger(modal);
	}

	async function apiPatchExampleItem(exampleItemId, body) {
		let message = 'Error! ExampleItem not updated.';
		let type = 'variant-filled-error';
		if (body) {
			try {
				const response = await patchData('exampleitems/' + exampleItemId, body);
				if (response) {
					type = 'variant-filled-success';
					message = 'ExampleItem updated successfully';
					const exampleitemIndex = exampleitems.findIndex(
						(exampleitem) => exampleitem.id === exampleItemId
					);
					if (exampleitemIndex !== -1) {
						exampleitems[exampleitemIndex] = response;
					}
				}
				console.log(response);
			} catch (error) {
				console.log(error);
			}
		} else {
			type = 'variant-filled-warning';
			message = 'Edit canceled';
		}
		const toast = {
			message: message,
			timeout: 10000,
			background: type
		};
		toastStore.trigger(toast);
	}

	// Delete exampleitem
	function deleteExampleItem(exampleitem) {
		const modalComponent = {
			ref: ModalDelete
		};
		const modal = {
			component: modalComponent,
			type: 'component',
			title: `Deleting exampleitem: ${exampleitem.title} (${exampleitem.code})`,
			body: 'Are you sure?',
			response: (r) => apiDeleteExampleItem(exampleitem.id, exampleitem, r)
		};
		modalStore.trigger(modal);
	}

	async function apiDeleteExampleItem(exampleItemId, body, resCancel) {
		let message = 'Error! ExampleItem not deleted.';
		let type = 'variant-filled-error';
		if (resCancel) {
			try {
				const response = await deleteData('exampleitems/' + exampleItemId);
				if (response.status) {
					type = 'variant-filled-success';
					message = 'ExampleItem deleted successfully';
					const exampleitemIndex = exampleitems.findIndex(
						(exampleitem) => exampleitem.id === body.id
					);
					if (exampleitemIndex !== -1) {
						exampleitems = exampleitems;
						exampleitems.splice(exampleitemIndex, 1);
					}
				}
				console.log(response);
			} catch (error) {
				console.log(error);
			}
		} else {
			type = 'variant-filled-warning';
			message = 'Deletion canceled';
		}
		const toast = {
			message: message,
			timeout: 10000,
			background: type
		};
		toastStore.trigger(toast);
	}

	// Search
	let searchTerm = '';

	$: filteredTableData = exampleitems.filter(
		(item) =>
			item.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
			item.code.toLowerCase().includes(searchTerm.toLowerCase()) ||
			item.description.toLowerCase().includes(searchTerm.toLowerCase())
	);
</script>

<h3 class="h3">ExampleItem List</h3>
<hr />
<div class="card">
	<header class="card-header flex justify-center">
		<div class="input-group input-group-divider grid-cols-[auto_1fr_auto]">
			<div class="input-group-shim">
				<IconKit name="magnify" />
			</div>
			<input type="search" placeholder="Search exampleitems" bind:value={searchTerm} />
		</div>
		<div class="ml-2">
			<button
				class="btn btn-md variant-ghost-surface"
				on:click={() => saveExampleItem(newExampleItem)}><span>Add exampleitem</span></button
			>
		</div>
	</header>
	{#if exampleitems.length}
		<section class="p-4">
			<div class="table-container">
				<!-- Native Table Element -->
				<table class="table table-hover">
					<thead>
						<tr>
							<th>Code</th>
							<th>Title</th>
							<th>Value</th>
							<th>Description</th>
							<th>Actions</th>
						</tr>
					</thead>
					<tbody>
						{#each filteredTableData as example (example.id)}
							<tr>
								<td>{example.code}</td>
								<td>{example.title}</td>
								<td>{example.value}</td>
								<td>{example.description}</td>
								<td>
									<button
										class="btn btn-sm variant-ghost-surface [&>*]:pointer-events-none"
										on:click={() => editExampleItem(example)}
										use:popup={{ event: 'hover', target: 'edit' + example.code, placement: 'top' }}
										><span><IconKit name="pencil" /></span></button
									>
									<div class="card p-2 variant-filled-secondary" data-popup={'edit' + example.code}>
										<p>Edit exampleitem</p>
										<div class="arrow variant-filled-secondary" />
									</div>
									<button
										class="btn btn-sm variant-ghost-surface [&>*]:pointer-events-none"
										on:click={() => deleteExampleItem(example)}
										use:popup={{
											event: 'hover',
											target: 'delete' + example.code,
											placement: 'top'
										}}><span><IconKit name="delete" /></span></button
									>
									<div
										class="card p-2 variant-filled-secondary"
										data-popup={'delete' + example.code}
									>
										<p>Delete exampleitem</p>
										<div class="arrow variant-filled-secondary" />
									</div>
								</td>
							</tr>
						{/each}
					</tbody>
					<tfoot />
				</table>
			</div>
		</section>
	{:else}
		<section class="p-4 text-center">
			<h5 class="h5">List exampleitems empty</h5>
		</section>
	{/if}
	<footer class="card-footer flex justify-center items-center">
		<!-- pagination -->
	</footer>
</div>
