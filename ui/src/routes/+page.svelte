<script>
	import NavCard from '$lib/components/NavCard.svelte';
	import { routes } from '$lib/utils/routes.js';
</script>

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-10 text-center flex-col items-center">
		<h2 class="h2">Welcome to a simple template built on the following stack.</h2>
		<div class="p-4 space-y-4">
			<div class="grid grid-cols-4 gap-4">
				{#each routes as card (card.href)}
					<NavCard title={card.title} content={card.content} href={card.href} icon={card.icon} />
				{/each}
			</div>
		</div>
		<div class="space-y-2">
			<p>Try editing the following:</p>
			<p><code class="code">/fastapi/app/ for backend</code></p>
			<p><code class="code">/ui/ for frontend</code></p>
		</div>
		<div class="space-y-2">
			<p>Try exampleitems:</p>
			<a class="btn variant-filled" href="/exampleitems" rel="noreferrer"> Launch Example </a>
		</div>
	</div>
</div>

<style lang="postcss">
</style>
