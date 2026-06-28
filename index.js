import { getPaths } from '@node-3d/addon-tools';

const paths = getPaths(import.meta.dirname);

export const bin = paths.bin;
export const include = paths.include;
export const hrtf = `${import.meta.dirname}/hrtf`;

const depsLabsound = {
	...paths,
	hrtf,
};

export default depsLabsound;
