from typing import List

from api.dao.data_dao import CSVDAO
from api.dto.data_schema import DataSchema


class MeuService:
    @staticmethod
    def ler_dados_csv() -> List[DataSchema]:
        dados_csv = CSVDAO.ler_csv()
        lista_dto = []

        for linha in dados_csv:
            item_dto = DataSchema(**linha)
            lista_dto.append(item_dto)

        return lista_dto
