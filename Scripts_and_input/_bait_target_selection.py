dbf = open("intersect_100bptile_bait.bed", 'r')
db = {}

dfh = open("LUAD_100bp_tile.sam40.paired-ttest.txt", 'r')
rfh = open("LUAD_100bp_tile_only_primary.paired-ttest.txt", 'w')
for i in dbf:
	line = i.strip('\n').split('\t')
	if line[3] != '.':
		db[line[0] + ':' + str(int(line[1])+1) + '-' + line[2]] = ''

rfh.write(dfh.readline())

for i in dfh:
	line = i.strip('\n').split('\t')
	try:
		db[line[0]]
		rfh.write('\t'.join(line) + '\n')
	except KeyError:
		pass
