import { exec as execCb } from 'node:child_process';
import { promisify } from 'node:util';

const exec = promisify(execCb);

const {
	getPlatform,
} = await import('@node-3d/addon-tools');


const platform = getPlatform();

const getScriptForLib = () => `src/${platform}.sh`;


const fail = (error) => {
	console.error(error);
	process.exit(-1);
};


const updateSystem = async () => {
	try {
		if (!['linux', 'aarch64'].includes(platform)) {
			return;
		}
		
		console.log('Updating System');
		const { stderr } = await exec(`sh src/update-${platform}.sh`);
		if (stderr) {
			console.error(stderr);
		}
		console.log('-------------------');
		console.log('Extracting Alsa');
		const { stderr2 } = await exec(`sh src/extract-${platform}.sh`);
		if (stderr2) {
			console.error(stderr2);
		}
		console.log('-------------------');
	} catch (error) {
		fail(error);
	}
};


const buildLib = async () => {
	try {
		console.log('LABSOUND Build Started');
		const { stderr, stdout } = await exec(`sh ${getScriptForLib()}`);
		if (stdout) {
			console.error(stdout);
		}
		if (stderr) {
			console.error(stderr);
		}
		console.log('LABSOUND Build Finished');
		console.log('-------------------');
	} catch (error) {
		fail(error);
	}
};


try {
	await updateSystem();
	
	await buildLib();
} catch (error) {
	fail(error);
}
