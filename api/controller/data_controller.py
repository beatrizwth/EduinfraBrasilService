from typing import Optional
from api.app import app
from fastapi import HTTPException
from api.dto.data_schema import DataSchema
from api.service.data_service import MeuService


@app.get('/ler', response_model=list[DataSchema])
async def ler_csv():
    dados = MeuService.ler_dados_csv()
    return dados


@app.get('/ler/{estado}', response_model=Optional[DataSchema])
async def ler_csv_estado(estado: str):
    dados = MeuService.ler_dados_csv()

    # Encontrar o primeiro item com a abreviação do estado correspondente
    dado_estado = next(
        (item for item in dados if item.SG_UF == estado.upper()), None)

    if dado_estado is None:
        raise HTTPException(
            status_code=404, detail=f"Data not found for state: {estado}")

    return dado_estado
