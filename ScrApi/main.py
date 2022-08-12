from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn 
from functions import getCoin

app = FastAPI(
    title="ScrApi 🕷️",
    description='API de cotações de moedas com dados raspados da Web',
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/scrapi/coin/{id}",tags=["Buscar cotação da moeda"])
def findCoin(id:int):
    return(getCoin(id))
    

if __name__ == "__main__":
    uvicorn.run(app, host="IP Host", port="Port") 