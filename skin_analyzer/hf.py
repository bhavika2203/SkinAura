import os
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

# Authenticate using the token from environment variable
HF_TOKEN = os.getenv('HUGGINGFACE_TOKEN')
if not HF_TOKEN:
    raise ValueError("Please set HUGGINGFACE_TOKEN environment variable")
login(HF_TOKEN)

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf", use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf", use_auth_token=True)
