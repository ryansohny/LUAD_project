##############################################################################################################
# create 1. all data with DMR annotation (ex. DMR1, DMR2, DMR2, DMR2, DMR3....) 2. only hyper-DMR and hypo-DMR
##############################################################################################################

# For NEW!!!! "LUAD_100bp_tile.paired-ttest.txt" : < 0.01 cutoff ==> p value <  0.000433498607443
import numpy as np
dfh = open("LUAD_100bp_tile_only_primary.paired-ttest.Annotation.txt", 'r')

rfh1 = open("DMR_LUAD_100bp_tile_only_primary.txt", 'w')

rfh2 = open("Hyper-DMR_LUAD_100bp_tile_only_primary.txt", 'w') # after creating rfh1, go through all and output like ==> id \t tumor avg met \t normal avg met \t tumor median met \t normal median met \t rest of the columns
rfh3 = open("Hypo-DMR_LUAD_100bp_tile_only_primary.txt", 'w')

header = dfh.readline().strip().split('\t')
# header write
# AVERAGE ==> < Sum(k=1 => n)(Sk - Nk) / n > where n is count of pair without na value 
rfh1.write(header[0] + '\tDMR\tDiffAvg\tDiffMedian\tAvgTumor\tAvgNormal\tAnnotation\t' + '\t'.join(header[2:]) + '\n')
rfh2.write(header[0] + '\tDMR\tDiffAvg\tDiffMedian\tAvgTumor\tAvgNormal\tAnnotation\t' + '\t'.join(header[2:]) + '\n')
rfh3.write(header[0] + '\tDMR\tDiffAvg\tDiffMedian\tAvgTumor\tAvgNormal\tAnnotation\t' + '\t'.join(header[2:]) + '\n')
dmrn_hypo = 0 # For DMR numbering
dmrn_hyper = 0
for i in dfh:
	line = i.strip('\n').split('\t')
	id = line[0]
	normal = map(lambda x: float(x) if x != ' ' else None, line[4:54])
	tumor = map(lambda x: float(x) if x != ' ' else None, line[54:])
	diff = list()
	normal4avg, tumor4avg = list(), list()
	for j in range(0,50):
		if normal[j] != None and tumor[j] != None:
			diff.append(tumor[j] - normal[j])
			normal4avg.append(normal[j])
			tumor4avg.append(tumor[j])
	avg, med = str(np.mean(diff)), str(np.median(diff))
	tavg, navg = str(np.mean(tumor4avg)), str(np.mean(normal4avg))
#	avgT, avgN =float(sum(filter(lambda x: x != None, tumor))) / (len(tumor) - tumor.count(None)), float(sum(filter(lambda x: x != None, tumor))) / (len(normal) - normal.count(None))
	if float(line[3]) < 0.000433498607443:
		if float(line[2]) > 0: # Tumour Hypermethylation
			dmrn_hyper += 1
			rfh1.write(id + '\t' + 'Hyper-DMR-' + str(dmrn_hyper) + '\t' + avg + '\t' + med + '\t' + tavg + '\t' + navg + '\t' + line[1] + '\t' + '\t'.join(line[2:]) + '\n')
			rfh2.write(id + '\t' + 'Hyper-DMR-' + str(dmrn_hyper) + '\t' + avg + '\t' + med + '\t' + tavg + '\t' + navg + '\t' + line[1] + '\t' + '\t'.join(line[2:]) + '\n')
		elif float(line[2]) < 0: # Normal Hypomethylation
			dmrn_hypo += 1
			rfh1.write(id + '\t' + 'Hypo-DMR-' + str(dmrn_hypo) + '\t' + avg + '\t' + med + '\t' + tavg + '\t' + navg + '\t' + line[1] + '\t' + '\t'.join(line[2:]) + '\n')
			rfh3.write(id + '\t' + 'Hypo-DMR-' + str(dmrn_hypo) + '\t' + avg + '\t' + med + '\t' + tavg + '\t' + navg + '\t' + line[1] + '\t' + '\t'.join(line[2:]) + '\n')
	else:
		rfh1.write(id + '\t' + '.' + '\t' + avg + '\t' + med + '\t' + tavg + '\t' + navg + '\t' + line[1] + '\t' + '\t'.join(line[2:]) + '\n')
	rfh1.flush()
	rfh2.flush()
	rfh3.flush()
