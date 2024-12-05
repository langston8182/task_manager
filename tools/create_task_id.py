from bson import ObjectId
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()


@tool
def create_task_id(self) -> str:
    """
    Tu dois ici générer un identifiant unique pour une tache
    :return: L'identifiant unique de la tâche
    """
    return str(ObjectId())
