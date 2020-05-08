cd ~/Downloads/hadoop
export PDSH_RCMD_TYPE=ssh
bin/hdfs namenode -format
sbin/start-dfs.sh
sbin/start-yarn.sh
bin/hdfs dfs -mkdir /wc/
bin/hdfs dfs -mkdir /wc/input/
bin/hdfs dfs -mkdir /kmer/
bin/hdfs dfs -mkdir /kmer/input/
bin/hdfs dfs -copyFromLocal ./hadoop/input1/bible+shakes.nopunc /wc/input 
bin/hdfs dfs -copyFromLocal ../ecoli.fa /kmer/input
# ~/Documents/sg/MPI-Exercises/spark_ex7/script.sh 
# bin/hdfs dfs -get /wc/input/wc_result output2
# sort -r -k 2 ./output2/wc_result/part-00000 > ./output2/wc_result/sorted.txt && head ./output2/wc_result/sorted.txt