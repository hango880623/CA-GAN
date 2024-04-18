#!/bin/bash

python main.py \
    --mode train \
    --dataset MT \
    --image_size 128 \
    --c_dim 3 \
    --sample_dir cagan_mt_crop/samples \
    --log_dir cagan_mt_crop/logs \
    --model_save_dir cagan_mt_crop/models \
    --result_dir cagan_mt_crop/results \
    --attr_path data/mt/makeup_clean.txt \
    --mt_image_dir data/mt/images/makeup_cropped \
    --sample_step 1000 \
    --resume_iters 150000 \
    --model_save_step 5000 \
    --lambda_cls 25 \
    --lambda_rec 200 \
    --lambda_gp 10 \
    --lambda_bkg 5 \
    --num_workers 2 \
    --num_iters_decay 20000
    