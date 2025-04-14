from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import budget_router
from src.routes import guest_list_router
app = FastAPI(
    title="Financial Wedding Planner API",
    description="API para planejamento financeiro de casamentos",
    version="1.0.0"
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(budget_router.router, prefix="/api/v1", tags=["budget"])
app.include_router(guest_list_router.router, prefix="/api/v1", tags=["guest_list"])
@app.get("/")
async def root():
    return {"message": "Bem-vindo à API do Financial Wedding Planner"}
