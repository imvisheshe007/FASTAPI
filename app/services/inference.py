from app.core.model_loader import load_model

model = load_model()

def generate_text(prompt: str, max_tokens: int = 100):
    return model(prompt, max_length=max_tokens)[0]['generated_text']
