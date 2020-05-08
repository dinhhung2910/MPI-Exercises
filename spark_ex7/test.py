from pyspark import SparkContext
sc = SparkContext("local", "count app")

# file = open("/home/linh/Downloads/hadoop/hadoop/input1/bible+shakes.nopunc", "rt")
# data = file.read().split()
# words = sc.parallelize (data)

text_file = sc.textFile("hdfs://127.0.0.1:9000/wc/input/bible+shakes.nopunc")
counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("hdfs://127.0.0.1:9000/wc/input/wc_result")
