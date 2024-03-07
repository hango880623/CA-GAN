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
    --mt_image_dir data/mt/images/makeup