package org.dataalgorithms.chap17.mapreduce;

import java.io.IOException;
//
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.mapreduce.Mapper.Context;

/**
 * Counts the kmers in each sequence.
 *
 * For each sequence, identify all k-mers 
 * and emit them as (<b>kmer</b>, <b>1</b>).
 *
 * @author Mahmoud Parsian
 * Định nghĩa kiểu giá trị đầu vào và trung gian
 */

public class KmerCountMapper
   extends Mapper<LongWritable, Text, Text, IntWritable> {
   
   private final static IntWritable ONE = new IntWritable(1);

   private int k; // k in k-mer 

   private final Text kmerKey = new Text();

   @Override
   protected void setup(Context context)
      throws IOException,InterruptedException {
      Configuration conf = context.getConfiguration();    
      this.k = conf.getInt("k.mer", 3); // default k=3 
   }

   @Override
   public void map(LongWritable key, Text value, Context context)
      throws IOException, InterruptedException {
      String sequence = value.toString();
      for (int i=0; i < sequence.length() -k+1; i++) {
         String kmer = KmerUtil.getKmer(sequence, i, k);
         kmerKey.set(kmer);
         // Ghi ra cặp giá trị mới
         context.write(kmerKey, ONE);
      }
   }
   
}