export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7;

accelerate launch --multi-gpu --num-machines 1 --num-processes 8 --main_process_port 29500 --same-network --rdzv_backend  static --mixed_precision bf16 -m axolotl.cli.train /jvsingh2/dummy_train/config/llama-3-3b-fft.yaml;