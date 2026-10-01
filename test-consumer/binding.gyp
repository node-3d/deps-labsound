{
	'variables': {
		'dep_bin': '<!(node -p "require(\'@node-3d/deps-labsound\').bin")',
		'dep_include': '<!(node -p "require(\'@node-3d/deps-labsound\').include")',
		'bin': '<!(node -p "require(\'@node-3d/addon-tools\').getBin()")',
	},
	'targets': [{
		'target_name': 'consumer',
		'sources': ['consumer.cpp'],
		'include_dirs': ['<(dep_include)'],
		'library_dirs': ['<(dep_bin)'],
		'conditions': [
			['OS=="linux"', { 'cflags_cc!': ['-fno-rtti', '-fno-exceptions'], 'cflags_cc': ['-frtti', '-fexceptions'], 'libraries': ["-Wl,-rpath,'$$ORIGIN/../../node_modules/@node-3d/deps-labsound/<(bin)'", '-lLabSound', '-llibnyquist', '-lasound'] }],
			['OS=="mac"', {
				'cflags_cc!': ['-fno-rtti', '-fno-exceptions'],
				'cflags_cc': ['-frtti', '-fexceptions'],
				'libraries': [
					'-Wl,-rpath,@loader_path/../../node_modules/@node-3d/deps-labsound/<(bin)',
					'-llibnyquist',
					'-L<(dep_bin)',
					'<(dep_bin)/LabSound',
				],
				'xcode_settings': {
					'DYLIB_INSTALL_NAME_BASE': '@rpath',
					'GCC_ENABLE_CPP_RTTI': 'YES',
					'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
					'OTHER_LDFLAGS': ['-framework AudioUnit', '-framework CoreAudio', '-framework AudioToolbox'],
					'OTHER_CPLUSPLUSFLAGS!': ['-fno-rtti', '-fno-exceptions'],
					'OTHER_CPLUSPLUSFLAGS': ['-frtti', '-fexceptions'],
				},
			}],
			['OS=="win"', {
				'libraries': ['-lwinmm', '-luser32', '-lLabSound', '-llibnyquist'],
				'defines!': ['_HAS_EXCEPTIONS=0'],
				'msvs_settings': {
					'VCCLCompilerTool': {
						'ExceptionHandling': '1',
						'AdditionalOptions!': ['/EHa-s-c-', '/GR-', '/MT'],
						'AdditionalOptions': ['/EHsc', '/GR', '/MD'],
					},
				},
			}],
		],
	}],
}
