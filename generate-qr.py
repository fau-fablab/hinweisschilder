#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (Copyleft) Harald

import os, qrcode
from qrcode.image.styledpil import StyledPilImage

fablabMainURL = "https://fablab.fau.de/"
'''
	!!! 
	Only place wordpress-permalinks in this list. Otherwise, links will break since machines are on sub-pages now.
	!!!
'''
maschines = {
	"fablab",
	"lasercutter",
	"multifunktionstisch",
	"schneideplotter",
	"textilpresse",
	"ultraschallbad",
	"cnc-drehbank",
	"cnc-fraese",
	"3d-drucker",
	"reflow-ofen",
	"staubsauger",
	"dremel",
	"fein-kleinbohrmaschine",
	"feinschleifer",
	"oberfraese",
	"pendelstichsaege",
	"tauchsaege",
	"platinenfertigung",
	"naehmaschine",
	"oesen-und-druckknopfpresse",
	"stickmaschine",
	"standbohrmaschine"
}

def makeQR(toolName, url):
	#print("generating qr code for " + toolName+"...")
	qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
	qr.add_data(url)
	img = qr.make_image(image_factory=StyledPilImage, embeded_image_path="./fab_cube.png")
	img.save(toolName+".png")


def main():
	os.chdir(os.path.dirname(os.path.abspath(__file__)))

	for name in maschines:
		if name != "fablab":
			makeQR(name, fablabMainURL + name)
		else:
			makeQR(name, fablabMainURL)
	
if __name__=="__main__":
	main()