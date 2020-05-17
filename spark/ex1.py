import sys
 
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":	
    sc = SparkContext("local","PySpark RDD")        
    # read data
    fileData = sc.textFile("./data/airports.dat")
    fileDataFilter = fileData.filter(lambda line: line.split(",")[3] == '"Papua New Guinea"')
    fileDataGroup = fileData.groupBy(lambda line: line.split(",")[3])
    airpotsCount = fileData.map(lambda line: (line.split(",")[3], 1)).reduceByKey(lambda a,b:a +b)

    num = fileData.count()
    print("Number Airport " + str(num))
    numberInCountry = fileDataFilter.count()
    numberCountry = fileDataGroup.count()

    airpotsCount.saveAsTextFile("./output/")
    print("Number Airport Papua New Guinea " + str(numberInCountry))
    print("Number Country " + str(numberCountry))
    