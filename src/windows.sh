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
		# libnyquist does not detect MSVC's ARM64 target macro. Its AVX and
		# minimp3 SIMD paths are x86-specific on the pinned upstream source.
		# Opus and Vorbis choose x86 intrinsic paths from _WIN64, which is also
		# defined on ARM64. Disable those paths and use their scalar fallbacks.
		sed -i 's/#elif (defined(_MSC_VER) && _MSC_VER >= 1400) && (defined (WIN64) || defined (_WIN64))/#elif 0/' third_party/libnyquist/third_party/opus/celt/float_cast.h
		sed -i 's/#elif (defined(_MSC_VER) && _MSC_VER >= 1400) && (defined (WIN32) || defined (_WIN32))/#elif 0/' third_party/libnyquist/third_party/opus/celt/float_cast.h
		sed -i 's/#if (defined(_MSC_VER) && defined(_WIN64)) || (defined(__GNUC__) && defined (__x86_64__))/#if 0/' third_party/libnyquist/third_party/libvorbis/src/os.h

		architecture_args=(
			-DCMAKE_CXX_FLAGS=/DARCH_CPU_LITTLE_ENDIAN\ /DMINIMP3_NO_SIMD
			-DLIBNYQUIST_ENABLE_AVX=OFF
		)
	fi

	MSYS_NO_PATHCONV=1 cmake -A "${BUILD_PLATFORM:-x64}" "${toolset_args[@]}" "${architecture_args[@]}" -DLABSOUND_USE_RTAUDIO=ON ..
	cmake --build . --target libnyquist --config Release
	cmake --build . --target LabSound --config Release
)

(
	cd src
	
	cp LabSound/build/bin/Release/LabSound.lib build/LabSound.lib
	cp LabSound/build/third_party/libnyquist/lib/Release/libnyquist.lib build/libnyquist.lib
)
