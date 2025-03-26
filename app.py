import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from unsloth.chat_templates import get_chat_template
from unsloth import FastLanguageModel

# Load model and tokenizer
model_name = "unsloth/DeepSeek-R1-Distill-Qwen-7B-unsloth-bnb-4bit"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
    load_in_4bit=True
)

# Initialize model for inference
model = FastLanguageModel.for_inference(model)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

def chat(user_input):
    messages = [{"role": "user", "content": user_input}]
    
    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt"
    )
    
    input_ids = inputs.to(device)
    
    outputs = model.generate(
        input_ids=input_ids,
        max_new_tokens=200,  # Increased from 80 to 200
        use_cache=False,  # Disabled cache to avoid early stopping
        pad_token_id=tokenizer.eos_token_id,
    )
    
    decoded_output = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    
    # Extract the assistant's response properly
    assistant_index = decoded_output.lower().rfind("assistant")
    if assistant_index != -1:
        response = decoded_output[assistant_index:].split("\n", 1)[-1].strip()
    else:
        response = decoded_output.strip()
    
    return response

# Define Gradio interface
demo = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(lines=2, placeholder="Enter your message here..."),
    outputs=gr.Textbox(label="Assistant Response"),
    title="AI Assistant",
    description="Chat with an AI assistant."
)

demo.launch()
