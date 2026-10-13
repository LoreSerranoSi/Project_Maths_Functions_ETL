
from fastapi import FastAPI, HTTPException
from src.read import get_results

app = FastAPI(
    title="Math Functions ETL API",
    description="API para consultar los resultados del proceso ETL",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Math Functions ETL API funcionando"}


@app.get("/results")
def read_results():
    try:
        return get_results()
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Error al consultar los resultados de SQLite"
        ) from error
    