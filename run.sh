#!/bin/bash

python main.py \
    --mode train \
    --dataset MT \
    --image_size 128 \
    --c_dim 3 \
    --sample_dir cagan_mt/samples \
    --log_dir cagan_mt/logs \
    --model_save_dir cagan_mt/models \
    --result_dir cagan_mt/results \
    --attr_path data/mt/makeup.txt \
    --mt_image_dir data/mt/images/makeup \
    --sample_step 1000 \
    --celeba_crop_size 192 \
    --model_save_step 5000 \
    --resume_iters 105000 \
    --lambda_cls 10 \
    --lambda_rec 200 \
    --lambda_gp 10 \
    --lambda_bkg 10 \
    --num_workers 2 
    