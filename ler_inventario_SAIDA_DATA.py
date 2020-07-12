# coding: utf-8


import json

import sys

fonte=sys.argv[1]

print fonte


with open(fonte) as f:
	data = json.load(f)

for ArchiveId in data['ArchiveList']:
	print ArchiveId['CreationDate']

