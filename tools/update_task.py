import json

from dotenv import load_dotenv
from langchain.tools import tool

from db_config import tasks_collection

load_dotenv()

@tool
def update_task(updated_task: str) -> str:
    """
    Tu dois ici mettre à jour ou modifier ou changer la tâche dans la base de données.
    Tu vas donc pouvoir modifier la date de la tâche, le contenu de la tache ou encore le responsable.
    La tache est une string de type json.
    Voici le schéma de la tache updated_task en entrée:
    {
        "id": "identifiant de la tâche"
        "content": "nom de la tâche",
        "due_date": "date limite de la tâche" au format jj/mm/aaaa,
        "status": "statut de la tâche",
        "responsable": "responsable de la tâche"
    }
    Pour la mise à jour, tu dois effectuer les étapes suivantes :
    - récupérer les id des tâches à supprimer. Si il y a plusieurs id, ils seront séparés par des virgules sans espaces.
    (tu dois te poser la bonne question, par exemple :
     si la requete est : "Modifie la tache de Virginie pour le medecin pour le 10 janvier 2025."
     alors tu dois te demander
     "quelle est l'identifiant de la tâche de Virginie pour le medecin ?)
     Il doit y avoir le mot identifiant ou identifiants dans la requete.
    - Met à jour la tâche en appliquant les modifications dans MongoDB.
    :param updated_task: La tâche a modifier. Seulement le json de la tâche au format string.
    je ne veux pas de guillemets simples ' en debut et fin de la chaine.
    je ne veux pas de guillemets doubles " en debut et fin de la chaine.
    Je veux uniquement le json brut dans updated_task
    :return: la réponse de l'assistant
    """
    try:
        # Etape 1 : récupération de _id
        task_id = json.loads(updated_task)["id"]
        document = tasks_collection.find_one({"text": {"$regex": f"{task_id}"}})
        if not document:
            return f"Aucun document trouvé avec l'id {task_id}."

        # Etape 2 : Mise à jour de la tâche
        object_id = document["_id"]
        update_result = tasks_collection.update_one(
            {"_id": object_id}, {"$set": {"text": updated_task}}
        )

        if update_result.modified_count == 1:
            return "Task updated successfully."
        else:
            return "Task not found."
    except Exception as e:
        return f"Erreur lors de la mise à jour : {str(e)}"
