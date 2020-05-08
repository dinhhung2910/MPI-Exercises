from pyspark import SparkContext
import os
sc = SparkContext("local", "count app")

file = open(os.path.dirname(__file__)+"/bible+shakes.nopunc", "rt").read().replace("\n", " ").split(" ")
words = sc.parallelize (file)

counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("hdfs://127.0.0.1:9000/wc/input/wc_result")
