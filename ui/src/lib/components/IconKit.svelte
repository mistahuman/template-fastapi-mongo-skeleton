<script>
	import { IconSvgPack } from '$lib/utils/iconpack.js';

	export let name = '';

	export const color = '';
	export let size = '1.5em';
	export let defaultIcon =
		'M12 3V13.55C11.41 13.21 10.73 13 10 13C7.79 13 6 14.79 6 17S7.79 21 10 21 14 19.21 14 17V7H18V3H12Z';

	let svgD = IconSvgPack.find((a) => a.name === name);
	let d = svgD ? svgD.svg : defaultIcon;
	let viewbox = svgD ? svgD.viewbox : '0 0 24 24';
</script>

<span>
	<svg
		class="icon"
		viewBox={viewbox}
		fill="currentColor"
		width={size}
		height={size}
		xmlns="http://www.w3.org/2000/svg"
	>
		<path {d} />
	</svg>
</span>

<style>
	.icon {
		position: relative;
		display: inline-block;
	}
</style>
