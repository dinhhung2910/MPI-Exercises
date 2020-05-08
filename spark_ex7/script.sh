export SPARK_HOME=~/Documents/TTPT/spark-3.0.0-preview2-bin-hadoop2.7
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH
export PATH=$SPARK_HOME/python:$PATH
# $SPARK_HOME/bin/spark-submit ~/Documents/sg/MPI-Exercises/spark_ex7/test.py 
$SPARK_HOME/bin/spark-submit ~/Documents/sg/MPI-Exercises/spark_ex7/kmer.py