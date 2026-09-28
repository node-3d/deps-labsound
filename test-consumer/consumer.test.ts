import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import test from 'node:test';

import '@node-3d/deps-labsound';

const require = createRequire(import.meta.url);
const consumer = require('./build/Release/consumer.node') as { probe: () => number };

test('links and loads the LabSound candidate', () => assert.equal(consumer.probe(), 1));
