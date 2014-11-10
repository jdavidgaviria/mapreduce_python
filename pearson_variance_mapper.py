#!/usr/bin/env python
import sys

# reads the num of features on the table as parameter
n_feat=int(sys.argv[1])

# reads the feature means as parameter
means_str=sys.argv[2].split(',')

# partial counter for rows processed
row_count=0

# OPTIMIZATION:
# initializes a dict to use as accumulator for partial sums of feature
feat_sum_dict={}
feat_mean_dict={}
for j in range(n_feat):
	feat_sum_dict[j]=float(0)
	feat_mean_dict[j]=float(means_str[j])

# reads a stream of rows from standard input
for row in sys.stdin:
		
	# splits the row into features
	feats = row.rstrip("\n").split(' ')
	row_count+=1
	
	# For every feature...
	for j in feat_sum_dict.keys():		

		# ...sum it to the accumulator values
		feat_sum_dict[j] += (float(feats[j]) - feat_mean_dict[j])**2

# OPTIMIZATION:
# After the mapper is done reading rows.
# For evey feature...
for i in feat_sum_dict.keys():
	
	# ...define a key for outout
	key = str(i)
	if row_count>0:
		# ...define a value for output
		value = str(feat_sum_dict[i]) + '_' + str(row_count)

		# emit the key-value pair
		print '%s:%s' % (key, value)

