from datetime import datetime

from dotenv import load_dotenv
from langchain.agents import tool

load_dotenv()

@tool
def get_current_time(self) -> str:
    """
    Retourne la date actuelle au format ISO 8601 (YYYY-MM-DDTHH:MM:SS).
    A utiliser si un agent a besoin de la date actuelle pour faire des requetes relatives à la date du jour.
    exemple d'utilisation :
    "Quelle est la date actuelle ?"
    "Quelle est la date d'aujourd'hui ?"
    "dans 3 semaines, quelle sera la date ?"
    "la semaine prochaine, quelle est la date ?"
    :return: la date actuelle au format ISO 8601
    """
    current_date = datetime.now().date().isoformat()
    return f"La date actuelle est : {current_date}"
