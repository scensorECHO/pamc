# this script analyzes an exported csv spreadsheet in order
# to parse relevant data from the asset management system

##list references##
# asset indices match at:.
# searchLine[3] -> exportLine['serial']
# searchLine[4] -> exportLine['userid']
# searchLine[5] -> exportLine['location']
# exportLine['serial'] is a partial string
# exportLine['location'] is a partial string

##requirements##
# asset export using template 'beassetuser'
# standard lease portfolio 
# code tested on python 2.7.9

from collections import deque
import threading

active = 1 # set true on while loop
assetsOut = deque([])
dataReady = deque([])
title = 'Customer Number,Type,Model,Serial,UserId,Location,Pay Start date,EOL Date,Product Description,Original Contract Number\n'
exportkeys = [] # 50 items, BEASSETUSER template
assetkeys = []
exportLines = []
searchLines = deque([])


def csvDataWriter():
	with open('parsedassets.csv','w') as csv:
		csv.write(title)
		totalCsv = ''
		while(active):
			if len(dataReady)>0:
				if len(assetsOut)>0:
					totalCsv += str(assetsOut.popleft())
					totalCsv += '\n'
					dataReady.popleft()
		csv.write(totalCsv)					
		csv.flush()
	return 1;

t = threading.Thread(target=csvDataWriter)
t.start()

with open('assetkeys','r') as ak:
	for key in ak.readline().split(','):
		assetkeys.append(key)

with open('exportkeys','r') as ek:
	for key in ek.readline().split(','):
		exportkeys.append(key)

with open('assetsexport.csv','r') as e:
	for line in e.readlines():
		pel = line.split(';')
		exportLines.append(dict([('userid',pel[49].strip()),('serial',pel[0].strip()),('location',pel[27].strip())]))
		
with open('assetstosearch.csv','r') as ats:
		for line in ats.readlines():	
			
			cols = line.split(',')
			if (len(cols) < 10):
				print ('Error reading line: '+line)
				continue

			newAsset = dict.fromkeys(assetkeys)
			for i in range(10):
				newAsset[i] = cols[i]   # custnum

			searchLines.append(newAsset)

def searchForAsset(srch):
	index = 0
	for export in exportLines:
		if srch[3] in export['serial']:
			return index
		index += 1
	return -1;

def concatSearchResults(srch):
	concatSearch = ''
	for i in range(10):
		concatSearch += srch[i]
		if(i == 9):
			break
		concatSearch+= ','
	return concatSearch;

def finishSearch(srch):
	results = concatSearchResults(srch)
	assetsOut.append(results)
	dataReady.append(1)

while len(searchLines) > 0:
	search = searchLines.popleft()
	if not search[4]:
		finishSearch(search)
		continue
	if not search[5]:
		finishSearch(search)
		continue
	info = None
	index = searchForAsset(search)
	if index >= 0:
		info = exportLines.pop(index)
		search[4] = info['userid']
		search[5] = info['location']
	else:
		search[5] = ''
	finishSearch(search)

active = 0
