#!/bin/bash

python main.py \
    --mode train \
    --dataset MT \
    --image_size 128 \
    --c_dim 3 \
    --sample_dir cagan_Data0421/samples \
    --log_dir cagan_Data0421/logs \
    --model_save_dir cagan_Data0421/models \
    --result_dir cagan_Data0421/results \
    --attr_path data/Data0421/clean.txt \
    --mt_image_dir data/Data0421/customized_cropped \
    --train_label data/Data0421/label.csv \
    --test_label data/Data0421/label.csv \
    --sample_step 1000 \
    --model_save_step 5000 \
    --lambda_cls 10 \
    --lambda_rec 200 \
    --lambda_gp 10 \
    --lambda_bkg 5 \
    --num_workers 2 \
    --num_iters_decay 20000 \
    --resume_iters 125000 \
    --g_lr 0.0003\
    