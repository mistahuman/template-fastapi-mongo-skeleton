<script>
	import IconKit from './IconKit.svelte';
	export let title;
	export let content;
	export let href;
	export let icon;
</script>

<a {href} target="_blank" class="card p-4">
	<header class="card-header h3">{title}</header>
	<section class="p-1"><IconKit name={icon}></IconKit></section>
	<section class="p-4">{content}</section>
</a>

<style>
	.card-header {
		font-weight: bold;
		margin-bottom: 10px;
	}
</style>
