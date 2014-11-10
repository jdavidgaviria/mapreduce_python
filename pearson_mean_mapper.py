#!/usr/bin/env python
import sys

# reads the num of features on the table as parameter
n_feat=int(sys.argv[1])

# partial counter for rows processed
row_count=0

# OPTIMIZATION:
# initializes a dict to use as accumulator for partial sums of feature
col_sum_dict={}
for j in range(n_feat):
	col_sum_dict[j]=float(0)


# reads a stream of rows from standard input
for row in sys.stdin:
		
	# splits the row into features
	feats = row.rstrip("\n").split(' ')
	row_count+=1
	
	# For every feature...
	for j in col_sum_dict.keys():		

		# ...sum it to the accumulator values
		col_sum_dict[j] += float(feats[j])

# OPTIMIZATION:
# After the mapper is done reading rows.
# For evey feature...
for j in col_sum_dict.keys():
	
	# ...define a key for outout
	key = str(j)
	if row_count>0:
		# ...define a value for output
		value = str(col_sum_dict[j]) + '_' + str(row_count)

		# emit the key-value pair
		print '%s:%s' % (key, value)

