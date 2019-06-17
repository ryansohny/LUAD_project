import sys

# RE programming

s = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY', 'chrUn_gl000220', 'chr4_gl000193_random', 'chrM', 'chrUn_gl000225', 'chr6_mcf_hap5', 'chr17_gl000205_random', 'chrUn_gl000230', 'chrUn_gl000224', 'chrUn_gl000234', 'chr7_gl000195_random', 'chrUn_gl000219', 'chrUn_gl000226', 'chrUn_gl000211', 'chr9_gl000199_random', 'chrUn_gl000229', 'chrUn_gl000238', 'chr6_dbb_hap3', 'chrUn_gl000212', 'chr1_gl000192_random', 'chrUn_gl000247', 'chrUn_gl000214', 'chrUn_gl000228', 'chr9_gl000198_random', 'chrUn_gl000241', 'chr6_qbl_hap6', 'chrUn_gl000240', 'chr4_gl000194_random', 'chrUn_gl000216', 'chrUn_gl000218', 'chrUn_gl000231', 'chr6_mann_hap4', 'chrUn_gl000223', 'chrUn_gl000213', 'chrUn_gl000217', 'chrUn_gl000237', 'chr6_ssto_hap7', 'chr19_gl000209_random', 'chr4_ctg9_hap1', 'chr17_ctg5_hap1', 'chr19_gl000208_random', 'chrUn_gl000232', 'chr17_gl000203_random', 'chr6_cox_hap2', 'chrUn_gl000221', 'chrUn_gl000235', 'chr1_gl000191_random', 'chr17_gl000204_random', 'chrUn_gl000246', 'chr11_gl000202_random', 'chr8_gl000197_random', 'chrUn_gl000222', 'chrUn_gl000239', 'chr17_gl000206_random', 'chrUn_gl000248', 'chr9_gl000201_random', 'chr6_apd_hap1', 'chrUn_gl000215', 'chrUn_gl000242', 'chrUn_gl000244', 'chrUn_gl000243', 'chrUn_gl000227', 'chr18_gl000207_random', 'chr21_gl000210_random', 'chr8_gl000196_random', 'chr9_gl000200_random', 'chrUn_gl000233', 'chrUn_gl000236', 'chrUn_gl000245', 'chrUn_gl000249']

dbf = open("/gmi-l1/_90.User_Data/phenomata/01.Reference/HG19/UCSC_hg19.length.sorted.txt", 'r')
dbf2 = open("UCSC_hg19.length.index.txt", 'w')
db = {}
for i in dbf:
	line = i.strip().split('\t')
	db[line[0]] = line[1] + '\t' + line[2]

for i in s:
	dbf2.write(i + '\t' + db[i] + '\n')

dbf.close()
dbf2.close()
dfh = open("UCSC_hg19.length.index.txt", 'r')


tile = int(sys.argv[1]) # variable
rfh = open("hg19_" + str(tile) + 'bp_tile.bed', 'w')
for i in dfh:
	line = i.strip().split('\t')
	chrom, start, end = line[0], int(line[1]), int(line[2])
	for j in range(start, end+1, tile):
		if j + 99  > end:
			rfh.write(chrom + '\t' + str(j) + '\t' + str(end) + '\n') # 1-based
			rfh.flush()
		else:
			rfh.write(chrom + '\t' + str(j) + '\t' + str(j+99) + '\n') # 1-based
			rfh.flush()

dfh.close()
rfh.close()

db = {}
dbf = open("Chr_order_file.txt", 'r')
dfh = open("hg19_" + str(tile) + 'bp_tile.bed', 'r')
rfh = open("hg19_" + str(tile) + 'bp_tile_indexed.bed', 'w')
for i in dbf:
	line = i.strip().split('\t')
	db[line[1]] = int(line[0])
for i in dfh:
	line = i.strip().split('\t')
	id1, id2 = db[line[0]] * 1000000000 + int(line[1]), db[line[0]] * 1000000000 + int(line[2])
	rfh.write('\t'.join(line) + '\t' + str(id1) + '\t' + str(id2) + '\n')
	rfh.flush()
