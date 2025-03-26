# Deploy Unsloth BNB 4-bit Text-Generation Models on Hugging Face Spaces using Gradio

## Introduction
This repository provides a framework for deploying Unsloth bnb-4bit text generation models on Hugging Face Spaces using Gradio.

## Features
- Supports multiple Unsloth bnb-4bit models  
- Provides a Gradio-based interface for text generation  
- Designed for Hugging Face Spaces deployment  
- Optimized for low-memory inference  

## Disclaimer
This repository provides an easy way to deploy Unsloth bnb-4bit models. However, some models may require additional configuration due to RoPE scaling issues or outdated dependencies.

### 1. Phi-4-mini-instruct-unsloth-bnb-4bit
**Issue:** `rope_scaling`'s `short_factor` field must have length 64, got 48.  

**Fix:** Manually set `rope_scaling={"short_factor": 64}` when loading the model.  

### 2. Newer Unsloth Models & Dependencies
**Issue:** Some newer models may not work due to outdated dependencies.  

**Fix:** Ensure all dependencies are updated to the latest versions before running the deployment.  

## Deployment Instructions

### 1. Create a New Hugging Face Space
1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)  
2. Click **Create new Space**  
3. Give your Space a name  
4. Select **Gradio** as the Space SDK  
5. Choose **Blank** as the Gradio template  
6. Select the Space hardware of your choice  
7. Set the Space as **Private** if you don’t want others to see and use your model  
8. Click **Create Space**  

### 2. Clone the Repository & Upload Files
1. Clone this GitHub repository to your local machine:
```bash   
   git clone https://github.com/MuhammadSheesShoaib/Deploy-Unsloth-bnb-4-bit-Text-Generation-Models-on-Hugging-Face-Spaces-using-Gradio.git
```
### 3. Deploy Your Model
1. Upload the required files to your Hugging Face Space.  

2. Go to **Settings** on your Hugging Face Space.  

3. Find **Restart Session** and restart the session.  

4. Your model is now deploying.

### 4. Test & Use Your Model
After deployment, you can test the model directly on Hugging Face Spaces.  

To use it through the API:  

1. Click **Use via API**.  
2. Follow the instructions to run it locally using the API.  
3. If the model requires an HF token, use:  

```python
   from gradio_client import Client
   client = Client("api_url", hf_token=HF_TOKEN)
```  
