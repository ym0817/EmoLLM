import torch
from modelscope import snapshot_download, AutoModel, AutoTokenizer
import os
# model_dir = snapshot_download('EmoLLM_PT_InternLM1.8B-chat', cache_dir='./', revision='master')
snapshot_download("Shanghai_AI_Laboratory/internlm2-chat-1_8b",
                  cache_dir= './',
                  revision='v1.1.0')
# model_dir = snapshot_download('qwen/Qwen2-0.5B-Instruct', cache_dir='./', revision='master')

# model_dir = snapshot_download('qwen/Qwen2-14B', cache_dir='./', revision='master')


# model_dir = snapshot_download('qwen/Qwen2-72B-Instruct-GPTQ-Int8', cache_dir='./', revision='master')

# dataset = MsDataset.load('damo/zh_cls_fudan-news').to_hf_dataset()