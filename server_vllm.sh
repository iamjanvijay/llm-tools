model_ckpt=/shared/storage-01/users/jvsingh2/dummy_train/train_cache/ckpts/checkpoint-113
model_name=meta-llama/Llama-3.2-3B-Instruct
model_len=16000
tp=1
CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server --model ${model_ckpt} --served-model-name ${model_name} --tokenizer ${model_name} --port 10010 --dtype bfloat16 --gpu-memory-utilization 0.9 --tensor-parallel-size ${tp} --trust-remote-code --enable-prefix-caching --max-model-len ${model_len}