import type { getPaths } from '@node-3d/addon-tools';

type AddonPaths = ReturnType<typeof getPaths>;

export declare const bin: AddonPaths['bin'];
export declare const include: AddonPaths['include'];
export declare const hrtf: string;

declare const depsLabsound: AddonPaths & {
	hrtf: string;
};
export default depsLabsound;
