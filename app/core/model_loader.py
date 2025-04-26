from transformers import pipeline

def load_model():
    return pipeline("text-generation", model="gpt2")
