import sys
dfh = open("/gmi-l1/_90.User_Data/phenomata/LUAD/01.Epigenome/02.DMC/04.Methylation_By_Bait_Region/NEW_ANALYSIS_20170726/Header.final.txt", 'r')
header = '\t'.join(dfh.readline().strip().split('\t')[4::2])
dfh.close()

dfh = open(sys.argv[1], 'r') # hg19_100bp_tile.bed
rfh = open('TEST_LUAD_100bp_tile.txt', 'w')
dbf = open("LUAD_methyl_all_Strand_integrated.txt", 'r')
rfh.write('ID' + '\t' + header + '\n')
rfh.flush()
# ID	sample name .....
dbf.readline()
line1 = dfh.readline().strip().split('\t') # tile bed
line2 = dbf.readline().strip().split('\t') # met coverage

met = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # coverage of C reads at CpG site
cov = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # total coverage at CpG site
metper = [] # methylation percentage
trigger = 0

while line1 != ['']:
	start, end = int(line1[3]), int(line1[4])
	while line2 != ['']:
		id = int(line2[0])
		if start <= id <= end:
			line2 = line2[3:]
			for i in range(0,200,2):
				if int(line2[i]) + int(line2[i+1]) >= 5:
					met[i/2] += int(line2[i])
					cov[i/2] += ( int(line2[i]) + int(line2[i+1]) )
					trigger = 1
			line2 = dbf.readline().strip().split('\t')
		else:
			if trigger == 1:
				for j in range(0,100):
					if cov[j] != 0:
						metper.append(str(float(met[j])/cov[j]))
					else:
						metper.append(' ')
				rfh.write(line1[0] + ':' + line1[1] + '-' + line1[2] + '\t' + '\t'.join(metper) + '\n')
				rfh.flush()
				line1 = dfh.readline().strip().split('\t')
				start, end = int(line1[3]), int(line1[4])
				met = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # coverage of C reads at CpG site
				cov = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # total coverage at CpG site
				metper = [] # methylation percentage
				trigger = 0
			else:
				line1 = dfh.readline().strip().split('\t')
				break
	if line2 == ['']:
		break
