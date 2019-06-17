dfh = open("LUAD_100bp_tile_only_primary.paired-ttest.txt", 'r')
dfh.readline()
rfh = open("LUAD_100bp_tile_only_primary.paired-ttest.bed", 'w')
for i in dfh:
	line = i.strip('\n').split('\t')
	chrom, start, end = line[0].split(':')[0], str(int(line[0].split(':')[1].split('-')[0]) -1), str(int(line[0].split(':')[1].split('-')[1]))
	rfh.write(chrom + '\t' + start + '\t' + end + '\n')	
	rfh.flush()
