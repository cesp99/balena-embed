from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import uvicorn

# Initialize model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Create API app
app = FastAPI()

# Request schema
class TextRequest(BaseModel):
    text: str

# Response schema
class EmbeddingResponse(BaseModel):
    embedding: list[float]

@app.post("/embed", response_model=EmbeddingResponse)
async def embed_text(request: TextRequest):
    embedding = model.encode(request.text)
    return EmbeddingResponse(embedding=embedding.tolist())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6700)
