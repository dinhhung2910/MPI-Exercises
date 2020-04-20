rm -rf ~/hadoopdata \
&& $HADOOP_HOME/sbin/stop-all.sh \
&& $HADOOP_HOME/bin/hadoop namenode -format \
&& $HADOOP_HOME/sbin/start-all.sh \
&& $HADOOP_HOME/bin/hadoop fs -mkdir /kmer \
&& $HADOOP_HOME/bin/hadoop fs -mkdir /kmer/input \
&& hadoop fs -chmod -R 777 / \
&& $HADOOP_HOME/bin/hadoop fs -put ../input/ecoli.fa /kmer/input \
&& $HADOOP_HOME/bin/hadoop jar ./kmer.jar org.dataalgorithms.chap17.mapreduce.KmerCountDriver /kmer/input /kmer/output 3 \
&& hadoop fs -get /kmer/output output \
&& sort -k 2nr output/part-r-00000 | head -n 10 >> output.txt