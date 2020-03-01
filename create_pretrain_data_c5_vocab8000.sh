#!/usr/bin/env bash
# convert c5 txt to tfrecords with clue vocab(8k), set t2s to True
echo $1,$2
PWD=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
j=0
if [ ! -d $PWD/log ];then
  mkdir $PWD/log
fi


for((i=$1;i<=$2;i++));
do
  #random_seed=`expr 12345 + $i `
  #echo $random_seed
  printf -v l "%07d" $i
  echo $l                                 # original: bert_base_128_vocab8k
  python3 create_pretraining_data.py  --input_file=gs://clue_pretrain_corpus/raw_txt_corpus/train/clue_pretrain_$l.txt \
    --output_file=gs://clue_pretrain_corpus/tfrecords/bert_base_128_c5_vocab8k/clue_pretrain128_$i.tfrecord \
    --vocab_file=./bert_base_dir/chinese_L-12_H-768_A-12/vocab_clue.txt  --t2s=True  \
    --do_lower_case=True --max_seq_length=128 --max_predictions_per_seq=20 --masked_lm_prob=0.15 --random_seed=12345 --dupe_factor=5 >$PWD/log_c5_vocab8k/tfrecord_$i.log 2>&1 &

  j=$[j+1]
  if [ $j -eq 20 ];then
    wait
    j=0
  fi
done
wait
echo "Finish"
