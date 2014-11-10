mapreduce_python
================

example to calculate the mean and sample variance column-wise if a matrix using mapreduce with python 

## 1. Deploy
### 1.1. Install hadoop
download hadoop, for example **http://mirrors.koehn.com/apache/hadoop/common/hadoop-2.2.0/hadoop-2.2.0.tar.gz** and decompress it (without further configuration it will run in standalone mode)

### 1.2. Setup the mapreduce code and example data
clone this repo to your computer and consider its local path and ${PATH_TO_REPO} as synonyms in the rest of this file.


## 2. Execution

### 2.1. Calculate Mean
Execute the following. The "3" passed as argument to the mapper is the number of columns of the input matrix
```bash
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.2.0.jar -file ${PATH_TO_REPO}/pearson_mean_mapper.py -mapper "./pearson_mean_mapper.py 3" -file ${PATH_TO_REPO}/pearson_mean_reducer.py -reducer "./pearson_mean_reducer.py"  -input ${PATH_TO_REPO}/input -output ${PATH_TO_REPO}/out-mean-01
```

To visualize the output <br>

```bash
cat ${PATH_TO_REPO}/out-mean-01/part-*
```




### 2.2. Calculate Mean
Execute the following. The "3" passed as argument to the mapper is the number of columns of the input matrix; the values "173,76.33,33.83" are the corresponding means of each column
```bash
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.2.0.jar -file ${PATH_TO_REPO}/pearson_variance_mapper.py -mapper "./pearson_variance_mapper.py 3 173,76.33,33.83" -file ${PATH_TO_REPO}/pearson_variance_reducer.py -reducer "./pearson_variance_reducer.py "  -input ${PATH_TO_REPO}/input -output ${PATH_TO_REPO}/out-variance-01
```

To visualize the output <br>

```bash
cat ${PATH_TO_REPO}/out-mean-01/part-*
```