#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (C) Max

import PyQRNative

def makeQR(text,dest):
	size=3
	# this function mostly taken from http://www.blog.pythonlibrary.org/2012/05/18/creating-qr-codes-with-python/
	for size in range(1,5):
		try:
			qr = PyQRNative.QRCode(size, PyQRNative.QRErrorCorrectLevel.M)
			qr.addData(text)
			qr.make()
		except TypeError:
			# erhöhe size, weil URL zu lang für gewählte size
			if size==5:
				raise Exception("URL zu lang - size in makeQR erhöhen oder besser URL kürzen")
			continue
		break
	im = qr.makeImage()
	img_file = open(dest, 'wb')
	im.save(img_file, 'PNG')
	img_file.close()




import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

codes = []
maschinen = ["lasercutter","3d-drucker","schneideplotter","cnc-fraese","cnc-drehbank", "platinenfertigung","3d-drucker-makerbot","cnc-fraese-roland","farblaserdrucker-canon-clc3200","3d-drucker-ultimaker","reflow-ofen","absaugmobil-cleantec-ctm-26","oberfrase-1010","multifunktionstisch-mft-3","tauchsage-ts-55-r"]
for m in maschinen:
	codes = codes + [["https://fablab.fau.de/tool/" + m, m]]
# TODO something like cd (dirname $0) - change to the directory that the script lives inside
for [text, dest] in codes:
	makeQR(text, dest+".png")
	
