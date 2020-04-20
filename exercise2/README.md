#open SSH LOCALHOST
ssh localhost

#set env var
export PDSH_RCMD_TYPE=ssh

#format
bin/hdfs namenode -format

#start hdfs
sbin/start-dfs.sh

#start yarn
sbin/start-yarn.sh

#mkdir
bin/hdfs dfs -mkdir /wc/input/
bin/hdfs dfs -mkdir /kmer/input/

#copy input from local
bin/hdfs dfs -copyFromLocal ./hadoop/input1/bible+shakes.nopunc /wc/input
bin/hdfs dfs -copyFromLocal ../ecoli.fa /kmer/input

#mapreduce
bin/hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -file ~/mapper.py -mapper ~/mapper.py -file ~/reducer.py -reducer ~/reducer.py -input /kmer/input/ecolitest.fs -output /kmer/output

#get output to local
bin/hdfs dfs -get /kmer/output output2

#sort and head
sort -r -k 2 ./output2/part-00000 > ./output2/sorted.txt && head ./output2/sorted.txt
head ./output/output/sorted.txt // sai cmnr



