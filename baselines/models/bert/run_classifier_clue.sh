# @Author: bo.shi
# @Date:   2020-03-15 16:11:00
# @Last Modified by:   bo.shi
# @Last Modified time: 2020-03-17 13:06:02
#!/usr/bin/env bash
CURRENT_DIR=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
CLUE_DATA_DIR=$CURRENT_DIR/../../CLUEdataset
CLUE_PREV_TRAINED_MODEL_DIR=$CURRENT_DIR/prev_trained_models

download_data(){
  TASK_NAME=$1
  if [ ! -d $CLUE_DATA_DIR ]; then
    mkdir -p $CLUE_DATA_DIR
    echo "makedir $CLUE_DATA_DIR"
  fi
  cd $CLUE_DATA_DIR
  if [ ! -d ${TASK_NAME} ]; then
    mkdir $TASK_NAME
    echo "make dataset dir $CLUE_DATA_DIR/$TASK_NAME"
  fi
  cd $TASK_NAME
  if [ ! -f "train.json" ] || [ ! -f "dev.json" ] || [ ! -f "test.json" ]; then
    rm *
    wget https://storage.googleapis.com/cluebenchmark/tasks/${TASK_NAME}_public.zip
    unzip ${TASK_NAME}_public.zip
    rm ${TASK_NAME}_public.zip
  else
    echo "data exists"
  fi
  echo "Finish download dataset."
}

download_model(){
  MODEL_NAME=$1
  if [ ! -d $CLUE_PREV_TRAINED_MODEL_DIR ]; then
    mkdir -p $CLUE_PREV_TRAINED_MODEL_DIR
    echo "make prev_trained_model dir $BERT_PRETRAINED_MODELS_DIR"
  fi
  cd $CLUE_PREV_TRAINED_MODEL_DIR
  if [ ! -d $MODEL_NAME ]; then
    mkdir -p $MODEL_NAME
  else
    cd $MODEL_NAME
    rm *
    if [ "$MODEL_NAME" = "RoBERTa-tiny-clue" ]; then
      wget -c https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-tiny-clue.zip
      unzip RoBERTa-tiny-clue.zip
      rm RoBERTa-tiny-clue.zip
    elif [ "$MODEL_NAME" = "RoBERTa-tiny-pair" ]; then
      wget -c https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-tiny-pair.zip
      unzip RoBERTa-tiny-pair.zip
      rm RoBERTa-tiny-pair.zip
    elif [ "$MODEL_NAME" = "RoBERTa-tiny3L768-clue" ]; then
      wget -c https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-tiny3L768-clue.zip
      unzip RoBERTa-tiny3L768-clue.zip
      rm RoBERTa-tiny3L768-clue.zip
    elif [ "$MODEL_NAME" = "RoBERTa-tiny3L312-clue" ]; then
      wget -c https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-tiny3L312-clue.zip
      unzip RoBERTa-tiny3L312-clue.zip
      rm RoBERTa-tiny3L312-clue.zip
    elif [ "$MODEL_NAME" = "RoBERTa-large-clue" ]; then
      wget -c https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-large-clue.zip
      unzip RoBERTa-large-clue.zip
      rm RoBERTa-large-clue.zip
    elif [ "$MODEL_NAME" = "RoBERTa-large-pair" ]; then
      wget -c https://storage.googleapis.com/cluebenchmark/pretrained_models/RoBERTa-large-pair.zip
      unzip RoBERTa-large-pair.zip
      rm RoBERTa-large-pair.zip
    else
      echo "unknown model_name, choose from [ RoBERTa-tiny-clue , RoBERTa-tiny-pair , RoBERTa-tiny3L768-clue , RoBERTa-tiny3L312-clue , RoBERTa-large-clue , RoBERTa-large-pair]"
    fi
  fi
}

run_task() {
  TASK_NAME=$1
  MODEL_NAME=$2
  download_data $TASK_NAME
  if [ ! -d $CLUE_PREV_TRAINED_MODEL_DIR/$MODEL_NAME ]; then
    download_model $MODEL_NAME
  fi
  DATA_DIR=$CLUE_DATA_DIR/${TASK_NAME}
  PREV_TRAINED_MODEL_DIR=$CLUE_PREV_TRAINED_MODEL_DIR/$MODEL_NAME
  MAX_SEQ_LENGTH=$3
  TRAIN_BATCH_SIZE=$4
  LEARNING_RATE=$5
  NUM_TRAIN_EPOCHS=$6
  SAVE_CHECKPOINTS_STEPS=$7
  # TPU_IP=$8
  OUTPUT_DIR=$CURRENT_DIR/${TASK_NAME}_output/
  COMMON_ARGS="
        --task_name=$TASK_NAME \
        --data_dir=$DATA_DIR \
        --vocab_file=$PREV_TRAINED_MODEL_DIR/vocab.txt \
        --bert_config_file=$PREV_TRAINED_MODEL_DIR/bert_config.json \
        --init_checkpoint=$PREV_TRAINED_MODEL_DIR/bert_model.ckpt \
        --max_seq_length=$MAX_SEQ_LENGTH \
        --train_batch_size=$TRAIN_BATCH_SIZE \
        --learning_rate=$LEARNING_RATE \
        --num_train_epochs=$NUM_TRAIN_EPOCHS \
        --save_checkpoints_steps=$SAVE_CHECKPOINTS_STEPS \
        --output_dir=$OUTPUT_DIR \
        --keep_checkpoint_max=0 \
  "
  cd $CURRENT_DIR
  echo "Start running..."
  python run_classifier.py \
        $COMMON_ARGS \
        --do_train=true \
        --do_eval=false \
        --do_predict=false

  echo "Start predict..."
  python run_classifier.py \
        $COMMON_ARGS \
        --do_train=false \
        --do_eval=true \
        --do_predict=true
}

download_model RoBERTa-tiny-clue

##command##task_name##model_name##max_seq_length##train_batch_size##learning_rate##num_train_epochs##save_checkpoints_steps##tpu_ip
run_task afqmc RoBERTa-tiny-clue 128 16 2e-5 3 300
run_task cmnli RoBERTa-tiny-clue 128 64 3e-5 2 300
run_task csl RoBERTa-tiny-clue 128 16 1e-5 5 100
run_task iflytek RoBERTa-tiny-clue 128 32 2e-5 3 300
run_task tnews RoBERTa-tiny-clue 128 16 2e-5 3 300
run_task wsc RoBERTa-tiny-clue 128 16 1e-5 10 10

