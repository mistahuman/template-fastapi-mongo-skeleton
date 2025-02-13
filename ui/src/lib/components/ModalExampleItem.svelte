<script>
	// Props
	/** Exposes parent props to this component. */
	export let parent;

	// Stores
	import { getModalStore } from '@skeletonlabs/skeleton';
	const modalStore = getModalStore();

	// Form Data
	const formData = $modalStore[0].formdata;

	function onFormSubmit() {
		if ($modalStore[0].response) $modalStore[0].response(formData);
		modalStore.close();
	}

	// Base Classes
	const cBase = 'card p-4 w-modal shadow-xl space-y-4';
	const cHeader = 'text-2xl font-bold';
	const cForm = 'border border-surface-500 p-4 space-y-4 rounded-container-token';
</script>

{#if $modalStore[0]}
	<div class="modal-example-form {cBase}">
		<header class={cHeader}>{$modalStore[0].title ?? '(title missing)'}</header>
		<article>{$modalStore[0].body ?? '(body missing)'}</article>
		<form class="modal-form {cForm}">
			<label class="label">
				<span>Title <sup>*</sup></span>
				<input
					class="input"
					type="text"
					bind:value={formData.title}
					placeholder="Insert exampleitem title"
				/>
			</label>
			<label class="label">
				<span>Value <sup>*</sup></span>
				<input
					class="input"
					type="number"
					bind:value={formData.value}
					placeholder="Insert exampleitem code"
				/>
			</label>
			<label class="label">
				<span>Code <sup>*</sup></span>
				<input
					class="input"
					type="text"
					bind:value={formData.code}
					placeholder="Insert exampleitem code"
				/>
			</label>
			<label class="label">
				<span>Description</span>
				<textarea
					class="input"
					type="text"
					bind:value={formData.description}
					placeholder="Insert exampleitem description"
				/>
			</label>
		</form>
		<!-- prettier-ignore -->
		<footer class="modal-footer {parent.regionFooter}">
        <button class="btn {parent.buttonNeutral}" on:click={parent.onClose}>Cancel</button>
        <button class="btn {parent.buttonPositive}" on:click={onFormSubmit}>Save</button>
    </footer>
	</div>
{/if}
