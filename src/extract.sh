(
	cd src
	
	rm -rf build LabSound
	mkdir -p build
	
	git init LabSound
	(
		cd LabSound
		git remote add origin https://github.com/raub/LabSound.git
		git fetch --depth 1 origin 1cccca8c31a8a68ae1b47843481f7a06598ccbbb
		git checkout --detach FETCH_HEAD
	)
	
	rm -rf ../include/LabSound
	mkdir -p ../include/LabSound
	cp -r LabSound/include/LabSound/* ../include/LabSound
	
	(
		cd LabSound/third_party
		git clone --depth 1 -b 0.2.2 https://github.com/libsndfile/libsamplerate.git
		git clone --depth 1 -b 0.11.22 https://github.com/mackron/miniaudio.git
		git clone --depth 1 https://github.com/ddiakopoulos/libnyquist.git
	)
)
