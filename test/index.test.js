import assert from 'node:assert/strict';
import { existsSync } from 'node:fs';
import { describe, it } from 'node:test';
import deps, { hrtf } from '../index.js';

describe('Paths', () => {
	it('exports an object', () => {
		assert.strictEqual(typeof deps, 'object');
	});

	it('exports "bin" string', () => {
		assert.strictEqual(typeof deps.bin, 'string');
	});

	it('exports "include" string', () => {
		assert.strictEqual(typeof deps.include, 'string');
	});

	it('exports the bundled HRTF directory', () => {
		assert.strictEqual(hrtf, deps.hrtf);
		assert.ok(existsSync(hrtf));
	});
});
