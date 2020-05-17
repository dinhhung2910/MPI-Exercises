import findspark
findspark.init()

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

  
    fileData = fileData.map(lambda line: line.split(",")).map(lambda x: (x[0], (x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13])))

    routesRDD = sc.textFile("./data/routes.dat")
    routesRDD = routesRDD.map(lambda line: line.split(",")).map(lambda x: (x[3], (x[0], x[1], x[2], x[4], x[5], x[6], x[7], x[8])))

    joinRDD = fileData.join(routesRDD)

    # flightGroup = routesRDD.groupBy(lambda line: line.split(",")[4])
    # flightCount = routesRDD.map(lambda line: (line.split(",")[4], 1)).reduceByKey(lambda a,b:a +b)
    # numberFlight = flightGroup.count()
    # print("Number flying " + str(flyingCount))

    