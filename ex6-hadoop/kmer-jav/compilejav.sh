export HADOOP_CLASSPATH=$(hadoop classpath) \
&& javac -classpath ${HADOOP_CLASSPATH} -d classes/ *.java \
&& jar -cvf kmer.jar -C classes/ .