# LabSound binaries and headers

This is a part of [Node3D](https://github.com/node-3d) project.

[![NPM](https://badge.fury.io/js/@node-3d%2Fdeps-labsound.svg)](https://badge.fury.io/js/@node-3d/deps-labsound)
[![Lint](https://github.com/node-3d/deps-labsound/actions/workflows/lint.yml/badge.svg)](https://github.com/node-3d/deps-labsound/actions/workflows/lint.yml)
[![Test](https://github.com/node-3d/deps-labsound/actions/workflows/test.yml/badge.svg)](https://github.com/node-3d/deps-labsound/actions/workflows/test.yml)

```bash
npm install @node-3d/deps-labsound
```




This dependency package distributes **LabSound**
binaries and headers through **npm** for **Node.js** addons.

* Platforms: Windows x64, Linux x64/ARM64, macOS ARM64.
* Libraries: LabSound, libnyquist.
* Linking: static lib.
* Backend: RtAudio.

LabSound is documented in the
[official repository](https://github.com/LabSound/LabSound).

The original LabSound sources are slightly modified, and now include:
* Unreleased commits from [LabSound/LabSound](https://github.com/LabSound/LabSound).
* Extra work from [Avataren/LabSound:Bugfixes](https://github.com/Avataren/LabSound/tree/Bugfixes).
* CMake configuration tweaks to build fewer binaries.
* Locally added fixes for AudioNode and AudioContext.
* See fork [raub/LabSound](https://github.com/raub/LabSound) - you can review all changes since `LabSound@1.2.0`.


> For unmodified `LabSound@1.2.0`, use `@node-3d/deps-labsound@<=5.0.0`.


## binding.gyp

See the [@node-3d/webaudio native source](https://github.com/node-3d/webaudio/tree/master/src/cpp) for a consuming addon example.


## HRTF Database

The copy of
[LabSound's HRTF Assets](https://github.com/LabSound/LabSound/tree/master/assets/hrtf)
is contained in the **hrtf** directory. Its absolute path is accessible as:

```js
import { hrtf } from '@node-3d/deps-labsound';
```


## Legal notice

This software uses the [LabSound audio engine](https://github.com/LabSound/LabSound) under BSD Clause 2.
A copy of the LabSound license [is included](LABSOUND_BSD), and can also be found at
[LabSound repository](https://github.com/LabSound/LabSound/blob/master/LICENSE).

## Binary Origin

Release archives are built by this repository's public GitHub Actions workflows.

Attestations: https://github.com/node-3d/deps-labsound/attestations

To verify a downloaded archive:

```bash
gh release download <tag> -R node-3d/deps-labsound -p <platform>.gz
gh attestation verify <platform>.gz -R node-3d/deps-labsound
```
