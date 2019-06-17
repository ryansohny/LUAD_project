from subprocess import call
import sys
input1 = sys.argv[1]  # Metylation_around_Peak_TFBS-ENCODE_Tumour.txt
input2 = sys.argv[2]  # Metylation_around_Peak_TFBS-ENCODE_Normal.txt
#/bin/grep

#call("/gmi-l1/_90.User_Data/phenomata/Tools/bedtools2-master/bin/bedtools intersect -wao -a " + sys.argv[1][:-4] + '_peakCenter.bed -b hg19_100bp_tile_indexed_only-primary.bed > ' + 'Intersect_' + sys.argv[1][:-4] + '_peakCenter_tile.bed',shell=True)

#/gmi-l1/_90.User_Data/phenomata/LUAD/01.Epigenome/02.DMC/04.Tile-based-approach/NEW_ANALYSIS_20170726/06.DMR/07.TranscriptionFactorBindingSite/01.TF_met/01.Tumour
#/gmi-l1/_90.User_Data/phenomata/LUAD/01.Epigenome/02.DMC/04.Tile-based-approach/NEW_ANALYSIS_20170726/06.DMR/07.TranscriptionFactorBindingSite/01.TF_met/02.Normal

dbf = open("TF_list.txt", 'r')
tfdb = []

for i in dbf:
	tfdb.append(i.strip())

# TUMOUR

for tf in tfdb:
	# make file for a specific TF
	call("/bin/grep " + tf + " " + input1 + " > ./01.TF_met/01.Tumour/" + tf + "_tumour.txt", shell=True)
	dfh = open("./01.TF_met/01.Tumour/" + tf + "_tumour.txt", 'r')
	rfh = open("./01.TF_met/01.Tumour/" + tf + "_tumour-AVG.txt", 'w')

	line = i.strip('\n').split('\t')

	met_t = map(lambda x: float(x) if x != ' ' else None, line[1:])
	c = map(lambda x: 1 if x != ' ' else 0, line[1:])

	for i in dfh:
		line = i.strip('\n').split('\t')
		met = map(lambda x: float(x) if x != ' ' else None, line[1:])
		for j in range(len(met_t)):
			if met[j] != None and met_t[j] != None:
				met_t[j] += met[j]
				c[j] += 1
			elif met[j] != None:
				met_t[j] = met[j]
				c[j] += 1
			elif met[j] == None and met_t[j] != None:
				pass
			else:
				pass
	# First assume there is no None in met_t
	try:
		met_avg = map(lambda x: float(met_t[x])/c[x], range(len(met_t)))
	except ZeroDivisionError:
		print 'fuck'
	rfh.write(tf + '\t' + '\t'.join(map(lambda x: str(x), met_avg)) + '\n')
	dfh.close()
	rfh.close()

# NORMAL

for tf in tfdb:
        # make file for a specific TF
        call("/bin/grep " + tf + " " + input2 + " > ./01.TF_met/02.Normal/" + tf + "_normal.txt", shell=True)
        dfh = open("./01.TF_met/02.Normal/" + tf + "_normal.txt", 'r')
        rfh = open("./01.TF_met/02.Normal/" + tf + "_normal-AVG.txt", 'w')

        line = i.strip('\n').split('\t')

        met_t = map(lambda x: float(x) if x != ' ' else None, line[1:])
        c = map(lambda x: 1 if x != ' ' else 0, line[1:])

        for i in dfh:
                line = i.strip('\n').split('\t')
                met = map(lambda x: float(x) if x != ' ' else None, line[1:])
                for j in range(len(met_t)):
                        if met[j] != None and met_t[j] != None:
                                met_t[j] += met[j]
                                c[j] += 1
                        elif met[j] != None:
                                met_t[j] = met[j]
                                c[j] += 1
                        elif met[j] == None and met_t[j] != None:
                                pass
                        else:
                                pass
        # First assume there is no None in met_t
        try:
                met_avg = map(lambda x: float(met_t[x])/c[x], range(len(met_t)))
        except ZeroDivisionError:
                print 'fuck'
        rfh.write(tf + '\t' + '\t'.join(map(lambda x: str(x), met_avg)) + '\n')
        dfh.close()
        rfh.close()

from scipy import stats

# tf name in tfdb 





