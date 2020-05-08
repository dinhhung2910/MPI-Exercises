from pyspark import SparkContext
import os
sc = SparkContext("local", "count app")

file = open(os.path.dirname(__file__)+"/ecoli.fa", "rt").read().replace("\n", "")

words = []

for i in range(len(file) - 9):
    words.append(file[i:i+9])
list_kmer = sc.parallelize (words)
counts = list_kmer.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("hdfs://127.0.0.1:9000/kmer/input/result")
