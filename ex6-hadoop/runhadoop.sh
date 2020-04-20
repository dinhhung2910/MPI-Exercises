rm -rf ~/hadoopdata \
&& $HADOOP_HOME/sbin/stop-all.sh \
&& $HADOOP_HOME/bin/hadoop namenode -format \
&& $HADOOP_HOME/sbin/start-all.sh \
&& $HADOOP_HOME/bin/hadoop fs -mkdir /wordcount \
&& $HADOOP_HOME/bin/hadoop fs -mkdir /wordcount/input \
&& hadoop fs -chmod -R 777 / \
&& $HADOOP_HOME/bin/hadoop fs -put ./input/bible+shakes.nopunc /wordcount/input \
&& $HADOOP_HOME/bin/hadoop jar ./WordCount.jar WordCount /wordcount/input /wordcount/output \
&& hadoop fs -get /wordcount/output output \
&& sort -k 2nr output/part-r-00000 | head -n 10 >> output.txt