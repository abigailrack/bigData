from __future__ import print_function
import sys
from operator import add
from pyspark.sql import SparkSession

# For running spark jobs locally using spark-submit, 
from pyspark import SparkConf, SparkContext


#def match

if __name__ == "__main__":
    if len(sys.argv) != 2:
            print("Usage: analyze.py <file>", file=sys.stderr)
            exit(-1)

    spark = SparkSession\
             .builder\
             .appName("PythonWordCount")\
             .getOrCreate()


    # Get all lines from file
    data = spark.read.text(sys.argv[1]).rdd \
            .map(lambda r: r[0]) \
            .map(lambda line: line.split('\t')) \
	    .map(lambda x: [x[0], (x[1], x[2])])\
#            .foreach(lambda x: print(x[1]))

    

    # Get list of user 1488844's movies
    input_user_id = '1488844'
    input_user_list = data.filter(lambda x: x[0] == input_user_id)


    # counts = lines.flatMap(lambda x: x.split(' ')) \
    #       .map(lambda x: (x, 1)) \
    #       .reduceByKey(add)

    # output = counts.collect()

    # for (word, count) in output:
    #       print("%s: %i" % (word, count))

spark.stop()

