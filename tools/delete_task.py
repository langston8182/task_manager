from dotenv import load_dotenv
from langchain.tools import tool

from db_config import tasks_collection

load_dotenv()


@tool
def delete_task(id: str) -> str:
    """
    Tu dois supprimer la ou les tâches dans la base de données et tu dois faire ca en deux etapes.
    Pour cela en entrée tu as la requete de l'utilisateur tu vas:
    - récupérer les id des tâches à supprimer. Si il y a plusieurs id, ils seront séparés par des virgules sans espaces.
    (tu dois te poser la bonne question, par exemple :
     quelle sont les identifiants des tâches de Virginie ?)
     Il doit y avoir le mot identifiant ou identifiants dans la requete.
    - Supprimer la ou les tâches de la base de données
    Important : En aucun cas tu dois supprimer les tâches sauf si c'est explicitement demandé par l'utilisateur.
    :param id: l'identifiant de la tâche à supprimer. Il peut y avoir plusieurs identifiants séparés par des virgules sans espaces.
    :return: le résultat de la suppression
    """
    try:
        print("Deleting task")
        task_ids = id.split(",")
        regex_pattern = "|".join(task_ids)
        delete_filter = {"text": {"$regex": regex_pattern}}
        tasks_collection.delete_many(delete_filter)
        return "Tasks deleted successfully."
    except ValueError:
        return "Error when deleting task."
