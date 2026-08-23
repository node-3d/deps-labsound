(
	cd src/LabSound
	mkdir -p build
	cd build
	
	toolset_args=()
	if [[ -n "${CMAKE_TOOLSET:-}" ]]; then
		toolset_args=(-T "$CMAKE_TOOLSET")
	fi

	architecture_args=()
	if [[ "${BUILD_PLATFORM:-x64}" == 'ARM64' ]]; then
		# libnyquist does not detect MSVC's ARM64 target macro.
		architecture_args=(-DCMAKE_CXX_FLAGS=/DARCH_CPU_LITTLE_ENDIAN)
	fi

	cmake -A "${BUILD_PLATFORM:-x64}" "${toolset_args[@]}" "${architecture_args[@]}" -DLABSOUND_USE_RTAUDIO=ON ..
	cmake --build . --target libnyquist --config Release
	cmake --build . --target LabSound --config Release
)

(
	cd src
	
	cp LabSound/build/bin/Release/LabSound.lib build/LabSound.lib
	cp LabSound/build/third_party/libnyquist/lib/Release/libnyquist.lib build/libnyquist.lib
)
