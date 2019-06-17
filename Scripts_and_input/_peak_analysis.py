from subprocess import call
import sys

###### Center of Peak generation

dfh = open(sys.argv[1], 'r') # histone bed file
rfh = open(sys.argv[1][:-4] + '_peakCenter.bed', 'w')

threshold = int(sys.argv[2]) # up down how many kb? ex) 3000,4000

for i in dfh:
	line = i.strip('\n').split('\t')
	center = (int(line[2]) - int(line[1]))/2 + int(line[1])
	rfh.write(line[0] + '\t' + str(center) + '\t' + str(center + 1) + '\t' + line[3] + '\n')
	rfh.flush()
	
dfh.close()
rfh.close()

call("/gmi-l1/_90.User_Data/phenomata/Tools/bedtools2-master/bin/bedtools intersect -wao -a " + sys.argv[1][:-4] + '_peakCenter.bed -b hg19_100bp_tile_indexed_only-primary.bed > ' + 'Intersect_' + sys.argv[1][:-4] + '_peakCenter_tile.bed',shell=True)

dbf = open('Intersect_' + sys.argv[1][:-4] + '_peakCenter_tile.bed', 'r')

line = dbf.readline().strip('\n').split('\t')
db = {}
while line != ['']:
	id, chrom, start, end = line[0] + ':' + line[1] + '-' + line[2] + '/' + line[3], line[4], int(line[5]), int(line[6])
	tile_d = []
	for c in range(0, threshold/100): # upstream
		t_start = start - threshold + (100 * c)  #tile start
		t_end = t_start + 100 #tile end
		tile_d.append(chrom + ':' + str(t_start) + '-' + str(t_end))
	for c in range(0, threshold/100): # downstream
		t_start = end + (100 * c) # tile start
		t_end = t_start + 100 # tile end
		tile_d.append(chrom + ':' + str(t_start) + '-' + str(t_end))
	db[id] = tile_d
	line = dbf.readline().strip('\n').split('\t')

dbf.close()

db_met = {}
dfh = open("DMR_LUAD_100bp_tile_only_primary_histone-SE.txt", 'r')
dfh.readline()
for i in dfh:
	line = i.strip('\n').split('\t')
	newid = line[0].split(':')[0] + ':' + str(int(line[0].split(':')[1].split('-')[0])-1) + '-' + line[0].split(':')[1].split('-')[1]
	db_met[newid] = line[6] + '/' + line[7] # AvgTumour / AvgNormal
dfh.close()	

rfh1 = open('Metylation_around_Peak_' + sys.argv[1][:-4] + '_Tumour.txt', 'w')
rfh2 = open('Metylation_around_Peak_' + sys.argv[1][:-4] + '_Normal.txt', 'w')

for key in db:
	d_t = []
	d_n = []
	for i in db[key]:
		try:
			d_t.append(db_met[i].split('/')[0])
			d_n.append(db_met[i].split('/')[1])
		except KeyError:
			d_t.append(' ')
			d_n.append(' ')
	rfh1.write(key + '\t' + '\t'.join(d_t) + '\n')
	rfh2.write(key + '\t' + '\t'.join(d_n) + '\n')
	rfh1.flush()
	rfh2.flush()

rfh1.close()
rfh2.close()













