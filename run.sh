#!/bin/bash

source activate vision_lang
python -u src/zero_shot_classification.py --fixed_embedding $1 --subtype $2 --dataset $3  --context_lambda $4
