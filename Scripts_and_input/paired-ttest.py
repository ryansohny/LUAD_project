import sys
from scipy import stats
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
dfh = open(sys.argv[1], 'r')
rfh = open(sys.argv[1][:-3] + 'sam40.paired-ttest.txt', 'w')
line = dfh.readline().strip().split('\t')
rfh.write('ID\ttstat\tpval\t' + '\t'.join(line[1:]) + '\n') # t/n 
rfh.flush()
line = dfh.readline().strip('\n').split('\t')
while line != ['']:
	id, pre_normal, pre_tumor, normal, tumor, c = line[0], map(lambda x: float(x) if x != ' ' else None, line[1:51]), map(lambda x: float(x) if x != ' ' else None, line[51:]), [], [], 0
	for i in range(0,50):
		if pre_normal[i] != None and pre_tumor[i] != None:
			c += 1
			normal.append(pre_normal[i])
			tumor.append(pre_tumor[i])
	if c >= 40:
		ttest = stats.ttest_rel(tumor, normal)
		t, pval = str(ttest[0]), str(ttest[1])
		rfh.write(id + '\t' + t + '\t' + pval + '\t' + '\t'.join(line[1:]) + '\n')
		rfh.flush()
	else:
		pass
	line = dfh.readline().strip('\n').split('\t')
