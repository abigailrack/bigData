from __future__ import print_function

import sys
from operator import add

from pyspark.sql import SparkSession

import re

if __name__ == "__main__":
    # Not enough arguments...
    if len(sys.argv) != 2:
	print("Usage: wordcount <file>", file=sys.stderr)
	exit(-1)

    spark = SparkSession\
	    .builder\
	    .appName("PythonWordCount")\
	    .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    
    print("```````")
    print(type(lines))
    print("```````")

    counts = lines.flatMap(lambda x: x.split(' '))\
		.map(lambda x: re.sub(r'[^\w]', '', x)) \
		.map(lambda x: re.sub(r'[0-9]', '', x)) \
		.map(lambda x: (x, 1))\
		.reduceByKey(add)
    output = counts.collect()

    
    # Sort list of words by number of occurrances
    for (word, count) in sorted(output, key=lambda x: x[1]):
	print("%s: %i" % (word, count))

spark.stop()
