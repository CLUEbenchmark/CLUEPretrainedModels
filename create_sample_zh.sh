#!/bin/bash
#########################################################################
# File Name: create_sample_zh.sh
# Author: Junyi Li
# Personal page: dukeenglish.github.io
# Created Time: 21:44:22 2020-03-16
#########################################################################

mkdir test
python create_pretraining_data.py \
      --input_file=./sample_text.txt \
        --output_file=./test/tf_examples.tfrecord \
          --vocab_file=robert/vocab.txt \
            --do_lower_case=True \
              --max_seq_length=64 \
                --max_predictions_per_seq=20 \
                  --masked_lm_prob=0.15 \
                    --random_seed=12345 \
                      --dupe_factor=5
