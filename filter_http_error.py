#!/usr/bin/env python
import sys
source = open(sys.argv[1],'r')
found = {}
for x in source.readlines():
	if " HTTP/1.1\" 500" not in x:
		continue
	x = ' '.join(x.split(" ")[6:]).split("HTTP/1.1")[0]
	if x in found.keys():
		found[x] = found[x]+1
	else:
		found[x]=1

for z in found.keys():
	print   str(found[z]) + " <= times of =>  "  + z.strip()
