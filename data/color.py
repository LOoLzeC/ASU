#-*-coding:utf-8-*-
# Coded By Deray
'''
	 Rebuild Copyright Can't make u real programmer
'''
# Report Bug On My Other Sosmed
# instagram: @reyy05_
# facebook: https://facebook.com/achmad.luthfi.hadi.3

# Manual Color

import sys

if ("linux" in sys.platform.lower()):
	
	W = '\033[1;37m' 
	N = '\033[0m'
	R = '\033[1;37m\033[31m'
	B = '\033[1;37m\033[34m' 
	G = '\033[1;32m'
	O = '\033[33m'
	C = '\033[36m'
	notice  = "{}{}[*]{} ".format(N,B,N)
	warning = "{}[-]{} ".format(R,N)
	good    = "{}[!]{} ".format(G,N)
	warn    = "{}[!]{} ".format(O,N)
	
else:
	
	W = ''
	N = ''
	R = ''
	B = ''
	G = ''
	O = ''
	C = ''
	notice  = ''
	warning = ''
	good    = ''
	warn    = ''
