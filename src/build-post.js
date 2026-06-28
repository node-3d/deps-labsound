import fs from 'node:fs/promises';
import path from 'node:path';

const {
	getPlatform, getBin, ensuredir, copy,
} = await import('@node-3d/addon-tools');


const bin = getBin();
const binPath = path.resolve(bin);
const platform = getPlatform();


const fail = (error) => {
	console.error(error);
	process.exit(-1);
};


try {
	await ensuredir(binPath);
	
	if (['linux', 'aarch64'].includes(platform)) {
		await copy(
			path.resolve(`src/alsa-${platform}/libasound.so`),
			`${binPath}/libasound.so`,
		);
	}
	
	await fs.cp(path.resolve('src/build'), binPath, { recursive: true });
} catch (error) {
	fail(error);
}
