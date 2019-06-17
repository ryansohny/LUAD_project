def calc_benjamini_hochberg_corrections(p_values, num_total_tests):
        """
        Calculates the Benjamini-Hochberg correction for multiple hypothesis
        testing from a list of p-values *sorted in ascending order*.

        See
        http://en.wikipedia.org/wiki/False_discovery_rate#Independent_tests
        for more detail on the theory behind the correction.

        **NOTE:** This is a generator, not a function. It will yield values
        until all calculations have completed.

        :Parameters:
        - `p_values`: a list or iterable of p-values sorted in ascending
                order
        - `num_total_tests`: the total number of tests (p-values)

        """
        prev_bh_value = 0
        for i, p_value in enumerate(p_values):
		bh_values=[]
                bh_value = p_value * num_total_tests / (i + 1)
                # Sometimes this correction can give values greater than 1,
                # so we set those values at 1
                bh_value = min(bh_value, 1)

                # To preserve monotonicity in the values, we take the
                # maximum of the previous value or this one, so that we
                # don't yield a value less than the previous.
                bh_value = max(bh_value, prev_bh_value)
                prev_bh_value = bh_value
                if bh_value>=0.01:
			dfh.seek(0)
			dfh.readline()
			for j in dfh:
				line = j.strip('\n').split('\t')
				pvalue = float(line[2])
				if pvalue < p_value:
					rfh.write(line[0] + '\t' + '\t'.join(line[3:]) + '\n')
					rfh.flush()
			print p_value
			break
import sys
dfh=open(sys.argv[1],'r')
rfh=open(sys.argv[1][:-4]+'_BH_filtered_q0.01.txt','w')
line = dfh.readline().strip().split('\t')
rfh.write(line[0] + '\t' + '\t'.join(line[3:]) + '\n')
rfh.flush()
p_values=[]
num_total_tests=0
for i in dfh:
	line=i.strip('\n').split('\t')
	p_values.append(float(line[2]))
       	num_total_tests+=1
p_values=sorted(p_values)
calc_benjamini_hochberg_corrections(p_values, num_total_tests)


##########              NEW     p 0.01 cutoff    0.000433498607443 

# For "LUAD_100bp_tile.paired-ttest.txt" : < 0.01 cutoff ==> p value <  0.000337769492065
# For "LUAD_100bp_tile.sam40.paired-ttest.txt" : < 0.01 cutoff ==> p value < 0.000327201031637

# For "LUAD_100bp_tile.paired-ttest.txt" : < 0.005 cutoff ==> p value <  0.000147488809067

# For "LUAD_100bp_tile.paired-ttest.txt" : < 0.001 cutoff ==> p value <  2.14694639453e-05

# For "LUAD_100bp_tile.paired-ttest.txt" : < 0.0001 cutoff ==> p value < 1.32695497801e-06

# For "LUAD_100bp_tile.paired-ttest.txt" : < 0.0005 cutoff ==> p value < 9.27941712453e-06
