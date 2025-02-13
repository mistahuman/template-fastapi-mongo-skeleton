<script>
	import { routes } from '$lib/utils/routes.js';
	import { page } from '$app/stores';
	import IconKit from '$lib/components/IconKit.svelte';
</script>

<nav class="list-nav p-4">
	<ul>
		{#each routes as route}
			<li>
				<a href={route.href} aria-current={$page.url.pathname === route.href}>
					<span><IconKit name={route.icon} /></span>
					<span class="flex-auto"> {route.title}</span>
				</a>
			</li>
		{/each}
	</ul>
</nav>
