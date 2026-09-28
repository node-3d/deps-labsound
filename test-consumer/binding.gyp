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
			['OS=="mac"', { 'libraries': ['-Wl,-rpath,@loader_path/../../node_modules/@node-3d/deps-labsound/<(bin)', '-lLabSound', '-llibnyquist'], 'xcode_settings': { 'GCC_ENABLE_CPP_RTTI': 'YES', 'GCC_ENABLE_CPP_EXCEPTIONS': 'YES' } }],
			['OS=="win"', { 'libraries': ['-lLabSound', '-llibnyquist', '-lwinmm'], 'defines!': ['_HAS_EXCEPTIONS=0'], 'msvs_settings': { 'VCCLCompilerTool': { 'RuntimeLibrary': 2, 'ExceptionHandling': '1', 'AdditionalOptions!': ['/MT'], 'AdditionalOptions': ['/MD', '/EHsc', '/GR'] } } }],
		],
	}],
}
