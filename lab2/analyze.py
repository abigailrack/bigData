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

    # given user
    given_user_id = '1488844'

    # Get all lines from file
    netflixRDD = spark.read.text(sys.argv[1]).rdd \
            .map(lambda r: r[0]) \
            .map(lambda line: line.split('\t')) \
            .map(lambda x: ((x[1], x[2]), x[0])) \
            .groupByKey() \
            .mapValues(list) \
            .filter(lambda x: given_user_id in x[1]) \
            .flatMap(lambda x: x[1]) \
            .map(lambda x: (x, 1)) \
            .reduceByKey(add)

    output = netflixRDD.collect()
    
    for (userID, count) in sorted(output, key=lambda x: x[1]):
        print("%s: %i" % (userID, count))
spark.stop()
