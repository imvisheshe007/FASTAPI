from fastapi import APIRouter
from app.schemas.prompt_schemas import PromptRequest, PromptResponse
from app.services.inference import generate_text

router = APIRouter()

@router.post("/generate", response_model=PromptResponse)
def generate_response(payload: PromptRequest):
    result = generate_text(payload.prompt, payload.max_tokens)
    return PromptResponse(result=result)
