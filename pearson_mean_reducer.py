#!/usr/bin/env python
import sys

# reads the list of fields of the table as parameter
col_sum_dict={}
col_num_rows_dict={}

# Read a stream of records from standard input
for line in sys.stdin:
	
	# Extracts key-value pair
	key_value = line.rstrip("\n").split(':')
	value = key_value[1].split('_')
	
	# Extract feature number
	j = int(key_value[0])
	if not col_sum_dict.has_key(j):
		col_sum_dict[j]=0
		col_num_rows_dict[j]=0
	
	# Extract partial sum of values and number of rows and add to accumulators
	col_sum_dict[j] = float(value[0])
	col_num_rows_dict[j] = int(value[1])

# After the reducer is done reading rows.
# For every feature
for j in col_sum_dict.keys():
	
	# Define a new key
	new_key = str(j)
	if col_num_rows_dict[j] != 0:
		
		# ...compute the mean
		col_sum_dict[j] = col_sum_dict[j] / col_num_rows_dict[j]
		
		# ...define a value for output
		new_value="%f" % col_sum_dict[j]
		
		# emit the key-value pair
		print'%s:%s' % (new_key, new_value)
