TARGET=hinweisschilder
default: gen-image all
gen-image: 3d-drucker.png
3d-drucker.png: ./generate-qr.py
	./generate-qr.py

include fablab-document/Makefile.include
