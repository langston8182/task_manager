import os
from datetime import datetime

from bson import ObjectId
from dotenv import load_dotenv
from langchain_core.tools import StructuredTool

load_dotenv()


def get_task_id(start_date: datetime, end_date: datetime) -> str:
    """
    Vous êtes un assistant qui gère des tâches. Vos outils attendent des arguments structurés.
    Quand une commande est donnée, reformulez-la pour qu'elle corresponde aux outils.
    Tu dois ici récupérer les taches qui ont une date due_date comprise entre start_date et end_date.
    Si la requete est une date relative comme par exemple "aujourd'hui", "demain", "hier", le start_date est la date du jour.
    Sinon le start_date est la date de début comme précisé dans la requete.
    :param start_date: La date de début de la recherche
    :param end_date: La date de fin de la recherche
    :return: la réponse a la requete
    """
    return str(ObjectId())


tool_get_task_with_dates = StructuredTool.from_function(get_task_with_dates)
