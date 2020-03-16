#!/bin/bash
#########################################################################
# File Name: run_sample.sh
# Author: Junyi Li
# Personal page: dukeenglish.github.io
# Created Time: 21:51:28 2020-03-16
#########################################################################
python run_pretraining.py \
      --input_file=./test/tf_examples.tfrecord \
        --output_dir=./test/pretraining_output \
          --init_checkpoint=robert/bert_model.ckpt \
            --do_train=True \
              --do_eval=True \
                --bert_config_file=robert/bert_config.json \
                  --train_batch_size=8 \
                    --max_seq_length=64 \
                      --max_predictions_per_seq=20 \
                        --num_train_steps=400 \
                          --num_warmup_steps=10 \
                            --learning_rate=2e-5

# mlm should be 1.0
